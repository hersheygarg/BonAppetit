from django import template
register = template.Library()

@register.simple_tag()
def multiply(price, qty):
    return price*qty