from django import template

register = template.Library()


@register.filter
def get_measurement_attr_diff(obj, attr):
    return getattr(obj, attr + "_difference", None)


@register.filter
def get_measurement_attr_value(obj, attr):
    return getattr(obj, attr, None)
