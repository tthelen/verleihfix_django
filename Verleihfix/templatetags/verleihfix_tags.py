from django import template

register = template.Library()


@register.inclusion_tag('lending_form.tmpl')
def lending_form(lending):
    """Render a partial template with a lending form."""
    return {'new': False, 'lending': lending, 'thing': lending.thing}

@register.inclusion_tag('lending_form.tmpl')
def new_lending_form(thing):
    """Render a partial template with a lending form."""
    return {'new': True, 'thing': thing}

@register.inclusion_tag('thing_card.tmpl')
def thing_card(thing):
    """Render a partial template with a lending form."""
    return {'thing': thing}

@register.inclusion_tag('type_card.tmpl')
def type_card(type):
    """Render a partial template with a lending form."""
    return {'type': type, 'num_things': type.thing_set.count()}


@register.simple_tag
def appname():
    return "Verleih<em>fix</em>"