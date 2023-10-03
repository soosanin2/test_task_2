
from django import template
from comments.models import Commentary

register = template.Library()

@register.inclusion_tag('comments/detail_page.html')
def comments_for_parent(comments, parent_id=None):
    # Отфильтровать комментарии, которые являются ответами на родительский комментарий
    if parent_id is not None:
        child_comments = [comment for comment in comments if comment.binding_com == parent_id]
    else:
        # Если parent_id отсутствует, это корневые комментарии
        child_comments = [comment for comment in comments if comment.binding_com is None]

    return {'comments': child_comments}
