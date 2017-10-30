from django import template
from django.utils.safestring import mark_safe

register = template.Library()

@register.simple_tag
def subscription_button(user, question_id):
    if user.subscribed.filter(id=question_id):
        subsribe_button_html = '''<a href="unsubscribe/{}" >unsubscribe</a>'''.format(question_id)
        return mark_safe(subsribe_button_html)

    unsubsribe_button_html = '''<a href="subscribe/{}" >subscribe</a>'''.format(question_id)
    return mark_safe(unsubsribe_button_html)
