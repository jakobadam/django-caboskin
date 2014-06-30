from django import template
register = template.Library()

@register.simple_tag
def url_replace(request, field, value):
    dict = request.GET.copy()
    dict[field] = value
    return dict.urlencode()
