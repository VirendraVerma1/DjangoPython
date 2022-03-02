from attr import fields
from home import widgets
from home.models import Blog
from django.forms import ModelForm, SelectDateWidget
from django import forms

class BlogFrom(ModelForm):
    class Meta:
        model=Blog
        fields='__all__'

    def __init__(self, *args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['date'].widget=widgets.DateInput()
        self.fields['title'].widget.attrs.update({'class':'form-control','placeholder':'title'})
        self.fields['desc'].widget.attrs.update({'class':'form-control','placeholder':'description'})
        self.fields['image'].widget.attrs.update({'class':'form-control'})
        self.fields['date'].widget.attrs.update({'class':'form-control','type':'date'})
        self.fields['user_id'].widget.attrs.update({'class':'form-control'})
        self.fields['username'].widget.attrs.update({'class':'form-control'})