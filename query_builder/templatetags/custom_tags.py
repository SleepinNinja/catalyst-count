from django import template
register = template.Library()


@register.filter(name='to_string')
def to_string(value):
	bytes_literal = value
	return bytes_literal.decode('utf-8')


@register.filter(name='num_to_string')
def num_to_string(value):
	bytes_literal = value
	return int(bytes_literal.decode('utf-8'))