from django.forms import ModelForm, CharField, TextInput, DateInput, DateField
from .models import Tag, Authors, Quotes


class TagForm(ModelForm):
    name = CharField(min_length=3, max_length=25, required=True, widget=TextInput())
    
    class Meta:
        model = Tag
        fields = ['name']


class AuthorsForm(ModelForm):
    fullname = CharField(min_length=3, max_length=25, required=True, widget=TextInput())
    born_date = DateField(required=True, widget=DateInput())
    born_location = CharField(max_length=50, required=True, widget=TextInput())
    description = CharField(max_length=150, required=True, widget=TextInput())

    class Meta:
        model = Authors
        fields = ['fullname', 'born_date', 'born_location', 'description']


class QuotesForm(ModelForm):
    quote = CharField(required=True, widget=TextInput())

    class Meta:
        model = Quotes
        fields = ['quote']
        exclude = ['tags', 'author']