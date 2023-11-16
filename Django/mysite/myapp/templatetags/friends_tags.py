from django import template
import myapp.views as views
from myapp.models import TagFriends


register = template.Library()


@register.inclusion_tag("myapp/list_tags.html")
def show_all_tags():
    return {"tags": TagFriends.objects.all()}
