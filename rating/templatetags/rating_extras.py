from django import template

register = template.Library()


@register.inclusion_tag('rating/album_list.html')
def album_list(a_list):
    return {'album_list': a_list}


@register.inclusion_tag('rating/performer_list.html')
def performer_list(p_list):
    return {'performer_list': p_list}
