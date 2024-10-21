from django import forms
class BookForm(forms.Form):
    s_name=forms.CharField(max_length=30,label='Title')
    s_class=forms.CharField(max_length=30,label='author')
    s_address=forms.CharField(max_length=30,label='pblished date')
    s_School=forms.CharField(max_length=30,label='isbn')
    


class BForm(forms.Form):
    s_name=forms.CharField(max_length=30,label='Student name')
    