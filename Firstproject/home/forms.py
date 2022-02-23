from attr import fields
from home.models import Blog
from django.forms import ModelForm
from django import forms

class BlogFrom(ModelForm):
    class Meta:
        model=Blog
        fields='__all__'

    def __init__(self, *args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['title'].widget.attrs.update({'class':'form-control','placeholder':'title','style':'margin-top:10px;margin-left:100px;'})