from django import template

register = template.Library()


@register.filter
def to_bn_number(number):
    number = number.replace('0', r'০') \
        .replace('1', r'১') \
        .replace('2', r'২') \
        .replace('3', r'৩') \
        .replace('4', r'৪') \
        .replace('5', r'৫') \
        .replace('6', r'৬') \
        .replace('7', r'৭') \
        .replace('8', r'৮') \
        .replace('9', r'৯')
    return number
