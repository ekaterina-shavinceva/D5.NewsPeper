from django_filters import FilterSet, ModelChoiceFilter, DateTimeFilter, ChoiceFilter
from .models import Post, Category
from django.forms import DateTimeInput
from .resources import CONTENT

class PostFilter(FilterSet):
    category = ModelChoiceFilter(
        field_name='postcategory__category',
        queryset=Category.objects.all(),
        label='Category',
        empty_label='все категории',

    )
    added_after = DateTimeFilter(
        field_name='post_time',
        lookup_expr='gt',
        label='Date',
        widget=DateTimeInput(
            format='%Y-%m-%d',
            attrs={'type': 'datetime-local'},
        ),
    )


    class Meta:
       model = Post
       fields = {
           'title': ['icontains'],
       }