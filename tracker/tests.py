import datetime
from decimal import Decimal
from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.utils import timezone
from django.urls import reverse


from .models import Measurement


def createMeasurement(
    user,
    pub_date=timezone.now(),
    chest=0,
    waist=0,
    hips=0,
    weight=0,
):
    return Measurement.objects.create(
        user=user,
        pub_date=pub_date,
        chest=chest,
        waist=waist,
        hips=hips,
        weight=weight,
    )


def createUser(username, password):
    return User.objects.create_user(username, password=password)


class MeasurementListViewTests(TestCase):
    def logIn(self, user):
        self.client.force_login(user)

    def setUp(self):
        self.user = createUser("user", "pass")
        self.logIn(self.user)

    def test_no_measurements(self):
        """
        If no measurements exist, an empty page is displayed.
        """
        response = self.client.get(reverse("tracker:history"))

        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context["measurement_list"], [])

    def test_single_measurement(self):
        """
        Single measurement is properly displayed on the page.
        """
        measurement = createMeasurement(user=self.user)

        response = self.client.get(reverse("tracker:history"))

        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context["measurement_list"], [measurement])

    def test_two_empty_measurements(self):
        """
        Two measurements are listed in the correct order by pub_date.
        """
        measurement1 = createMeasurement(
            user=self.user, pub_date=timezone.now() - datetime.timedelta(days=3)
        )
        measurement2 = createMeasurement(
            user=self.user, pub_date=timezone.now() - datetime.timedelta(days=1)
        )

        response = self.client.get(reverse("tracker:history"))

        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(
            list(response.context["measurement_list"]), [measurement2, measurement1]
        )

    def test_empty_measurement_has_not_difference_attributes(self):
        """
        Single empty measurement hasn't got a difference attributes.
        """
        createMeasurement(user=self.user)

        response = self.client.get(reverse("tracker:history"))

        self.assertEqual(response.status_code, 200)
        self.assertFalse(
            hasattr(response.context["measurement_list"][0], "chest_difference")
        )
        self.assertFalse(
            hasattr(response.context["measurement_list"][0], "waist_difference")
        )
        self.assertFalse(
            hasattr(response.context["measurement_list"][0], "hips_difference")
        )
        self.assertFalse(
            hasattr(response.context["measurement_list"][0], "weight_difference")
        )

    def test_two_empty_measurements_has_not_a_difference_attributes(self):
        """
        Two empty measurements hasn't got a difference attributes.
        """
        createMeasurement(
            user=self.user,
            pub_date=timezone.now() - datetime.timedelta(days=3),
        )
        createMeasurement(
            user=self.user,
            pub_date=timezone.now() - datetime.timedelta(days=1),
        )

        response = self.client.get(reverse("tracker:history"))

        self.assertEqual(response.status_code, 200)
        self.assertFalse(
            hasattr(response.context["measurement_list"][0], "chest_difference")
        )
        self.assertFalse(
            hasattr(response.context["measurement_list"][0], "waist_difference")
        )
        self.assertFalse(
            hasattr(response.context["measurement_list"][0], "hips_difference")
        )
        self.assertFalse(
            hasattr(response.context["measurement_list"][0], "weight_difference")
        )
        self.assertFalse(
            hasattr(response.context["measurement_list"][1], "chest_difference")
        )
        self.assertFalse(
            hasattr(response.context["measurement_list"][1], "waist_difference")
        )
        self.assertFalse(
            hasattr(response.context["measurement_list"][1], "hips_difference")
        )
        self.assertFalse(
            hasattr(response.context["measurement_list"][1], "weight_difference")
        )

    def test_single_non_empty_measurement_has_not_difference_attributes(self):
        """
        Single non-empty measurement hasn't got a difference attributes.
        """
        createMeasurement(
            user=self.user, chest=12.0, waist=32.32, hips=3.03, weight=44.54
        )

        response = self.client.get(reverse("tracker:history"))

        self.assertEqual(response.status_code, 200)
        self.assertFalse(
            hasattr(response.context["measurement_list"][0], "chest_difference")
        )
        self.assertFalse(
            hasattr(response.context["measurement_list"][0], "waist_difference")
        )
        self.assertFalse(
            hasattr(response.context["measurement_list"][0], "hips_difference")
        )
        self.assertFalse(
            hasattr(response.context["measurement_list"][0], "weight_difference")
        )

    def test_two_non_empty_measurements_has_difference_attributes(self):
        """
        The second of two non-empty measurements has got the correct difference
        attributes.
        """
        createMeasurement(
            user=self.user,
            pub_date=timezone.now() - datetime.timedelta(days=3),
            chest=12.0,
            waist=32.32,
            hips=2,
            weight=32.12,
        )
        createMeasurement(
            user=self.user,
            pub_date=timezone.now() - datetime.timedelta(days=1),
            chest=12.0,
            waist=22.11,
            hips=3.03,
            weight=44.54,
        )

        response = self.client.get(reverse("tracker:history"))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["measurement_list"][0].chest_difference, 0)
        self.assertEqual(
            response.context["measurement_list"][0].waist_difference, Decimal("-10.21")
        )
        self.assertEqual(
            response.context["measurement_list"][0].hips_difference, Decimal("1.03")
        )
        self.assertEqual(
            response.context["measurement_list"][0].weight_difference, Decimal("12.42")
        )

        self.assertFalse(
            hasattr(response.context["measurement_list"][1], "chest_difference")
        )
        self.assertFalse(
            hasattr(response.context["measurement_list"][1], "waist_difference")
        )
        self.assertFalse(
            hasattr(response.context["measurement_list"][1], "hips_difference")
        )
        self.assertFalse(
            hasattr(response.context["measurement_list"][1], "weight_difference")
        )

    def test_two_measurements_with_equal_date_and_different_time(self):
        """
        Two measurements with equal time and difference time of publication
        are listed in the correct order.
        """
        measurement1 = createMeasurement(
            user=self.user,
            pub_date=timezone.now()
            - datetime.timedelta(days=1, hours=3, minutes=12, seconds=33),
        )
        measurement2 = createMeasurement(
            user=self.user,
            pub_date=timezone.now()
            - datetime.timedelta(days=1, hours=6, minutes=33, seconds=56),
        )

        response = self.client.get(reverse("tracker:history"))

        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(
            list(response.context["measurement_list"]), [measurement1, measurement2]
        )

    def test_logged_in_user_measurements_only(self):
        """
        Only logged in user measurements are displayed on the page.
        """
        user2 = createUser("user2", "pass")

        measurement1 = createMeasurement(user=self.user)
        measurement2 = createMeasurement(user=self.user)
        createMeasurement(user=user2)
        createMeasurement(user=user2)

        response = self.client.get(reverse("tracker:history"))

        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(
            list(response.context["measurement_list"]), [measurement1, measurement2]
        )


class MeasurementChartViewTests(TestCase):
    def logIn(self, user):
        self.client.force_login(user)

    def setUp(self):
        self.user = createUser("user", "pass")
        self.logIn(self.user)

    def test_no_measurements(self):
        """
        If no measurements exist, an appropriate message is displayed.
        """
        response = self.client.get(reverse("tracker:charts"))

        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context["measurement_list"], [])
        self.assertContains(response, "No measurements are available!")

    def test_with_measurements(self):
        """
        If measurements exists, a chart is displayed.
        """
        measurement1 = createMeasurement(
            user=self.user,
            pub_date=timezone.now() - datetime.timedelta(days=3),
            chest=12.0,
            waist=32.32,
            hips=2,
            weight=32.12,
        )
        measurement2 = createMeasurement(
            user=self.user,
            pub_date=timezone.now() - datetime.timedelta(days=1),
            chest=12.0,
            waist=22.11,
            hips=3.03,
            weight=44.54,
        )

        response = self.client.get(reverse("tracker:charts"))

        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(
            response.context["measurement_list"], [measurement2, measurement1]
        )
        self.assertContains(response, '<canvas id="chart">')

    def test_logged_in_user_measurements_only(self):
        """
        Only logged in user measurements are displayed on the chart.
        """
        user2 = createUser("user2", "pass")

        measurement1 = createMeasurement(user=self.user)
        measurement2 = createMeasurement(user=self.user)
        createMeasurement(user=user2)
        createMeasurement(user=user2)

        response = self.client.get(reverse("tracker:charts"))

        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(
            list(response.context["measurement_list"]), [measurement1, measurement2]
        )


class DashboardViewTests(TestCase):
    def logIn(self, user):
        self.client.force_login(user)

    def setUp(self):
        self.user = createUser("user", "pass")
        self.logIn(self.user)

    def test_no_measurements(self):
        """
        If no measurements exist, an appropriate message is displayed.
        """
        response = self.client.get(reverse("tracker:home"))

        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context["measurement_list"], [])
        self.assertEquals(response.context["summary_data"], None)
        self.assertEquals(response.context["latest_measurements"], None)
        self.assertContains(response, "No measurements are available!")

    def test_with_measurements(self):
        """
        If measurements exists, a dashboard content is displayed.
        """
        measurement1 = createMeasurement(
            user=self.user,
            pub_date=timezone.now() - datetime.timedelta(days=3),
            chest=12.0,
            waist=32.32,
            hips=2,
            weight=32.12,
        )
        measurement2 = createMeasurement(
            user=self.user,
            pub_date=timezone.now() - datetime.timedelta(days=1),
            chest=12.0,
            waist=22.11,
            hips=3.03,
            weight=44.54,
        )

        response = self.client.get(reverse("tracker:home"))

        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(
            response.context["measurement_list"], [measurement1, measurement2]
        )
        self.assertQuerysetEqual(
            response.context["latest_measurements"], [measurement2, measurement1]
        )
        self.assertEqual(response.context["summary_data"], measurement2)
        self.assertContains(
            response,
            '<canvas id="measurementsChart" class="dashboard-measurements-chart"></canvas>',
        )
        self.assertContains(
            response,
            '<canvas id="weightChart"></canvas>',
        )

    def test_logged_in_user_measurements_only(self):
        """
        Only logged in user measurements are displayed on the dashboard.
        """
        user2 = createUser("user2", "pass")

        measurement1 = createMeasurement(user=self.user)
        measurement2 = createMeasurement(user=self.user)
        createMeasurement(user=user2)
        createMeasurement(user=user2)

        response = self.client.get(reverse("tracker:home"))

        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(
            list(response.context["measurement_list"]), [measurement1, measurement2]
        )
        self.assertQuerysetEqual(
            list(response.context["latest_measurements"]), [measurement1, measurement2]
        )
        self.assertEqual(response.context["summary_data"], measurement1)


class MeasurementDetailViewTests(TestCase):
    def logIn(self, user):
        self.client.force_login(user)

    def setUp(self):
        self.user = createUser("user", "pass")
        self.logIn(self.user)

    def test_no_measurement_with_the_given_id(self):
        """
        If no measurement with the given id exist, a 404 status code is returned.
        """
        response = self.client.get(
            reverse("tracker:measurement-detail", kwargs={"pk": 1})
        )

        self.assertEqual(response.status_code, 404)

    def test_no_measurement_for_the_logged_user_(self):
        """
        If no measurement with the given id exist for the logged user,
        a 403 status code is returned.
        """
        user2 = createUser("user2", "pass")
        createMeasurement(user=user2)

        response = self.client.get(
            reverse("tracker:measurement-detail", kwargs={"pk": 1})
        )

        self.assertEqual(response.status_code, 403)

    def test_with_measurement(self):
        """
        If measurement with given id exists, a detail view content is displayed.
        """
        pub_date = timezone.now() - datetime.timedelta(days=3)
        chest = 12.0
        waist = 32.32
        hips = 2
        weight = 32.12

        createMeasurement(
            user=self.user,
            pub_date=pub_date,
            chest=chest,
            waist=waist,
            hips=hips,
            weight=weight,
        )
        response = self.client.get(
            reverse("tracker:measurement-detail", kwargs={"pk": 1})
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["object"].pub_date, pub_date)
        self.assertEqual(response.context["object"].chest, chest)
        self.assertEqual(response.context["object"].waist, round(Decimal(waist), 2))
        self.assertEqual(response.context["object"].hips, hips)
        self.assertEqual(response.context["object"].weight, round(Decimal(weight), 2))
