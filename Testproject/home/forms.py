from attr import fields
from home.models import Tag
from home.models import Blog
from django.forms import ModelForm
from django import forms
from home import widgets

class BlogFrom(ModelForm):
    class Meta:
        model=Blog
        fields='__all__'

    def __init__(self, *args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['title'].widget.attrs.update({'class':'form-control','placeholder':'title'})
        self.fields['username'].widget.attrs.update({'class':'form-control','placeholder':'username','type':'hidden'})
        
        self.fields['date'].widget = widgets.DateInput()
        self.fields['title'].widget = widgets.PasswordInput()
        self.fields['user_id'].widget = widgets.HiddenInput()
        self.fields['username'].widget = widgets.HiddenInput()
        self.fields['date'].widget.attrs.update({'class':'form-control'})
        self.fields['title'].widget.attrs.update({'class':'form-control','placeholder':'title'})
        self.fields['tags'].widget.attrs.update({'class':'form-control'})


class TagForm(ModelForm):
    class Meta:
        model=Tag
        fields='__all__'
    def __init__(self, *args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['title'].widget.attrs.update({'class':'form-control','placeholder':'title'})