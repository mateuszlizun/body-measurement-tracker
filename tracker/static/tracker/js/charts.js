const measurementsData = {
    labels: measurementsLabels,
    datasets: measurementsDatasets
};

const measurementsConfig = {
    type: 'line',
    data: measurementsData,
    options: { maintainAspectRatio: false }
};

const measurementsChart = new Chart(
    document.getElementById('measurementsChart'),
    measurementsConfig
);

const weightData = {
    labels: weightLabels,
    datasets: weightDatasets
};

const weightConfig = {
    type: 'line',
    data: weightData,
    options: { maintainAspectRatio: false }
};

const weightChart = new Chart(
    document.getElementById('weightChart'),
    weightConfig
);