from django import forms
from .models import Blog

#모델을 기반으로 한 입력 공간을 만들기 위해서
class BlogPost(forms.Form):
    
        email = forms.EmailField()
        files = forms.FileField()
        url = forms.URLField()
        words = forms.CharField(max_length=200)
        max_number = forms.ChoiceField(choices=[('1','one'), ('2','two'),('3','three')])

#임의의 공간을 기반으로 한 입력공간을 위해서
#class BlogPost(form.form)