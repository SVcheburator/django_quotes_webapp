from django import template

register = template.Library()


def author(quote_author):
    return ''.join([str(name) for name in quote_author.all()])


register.filter('author', author)
