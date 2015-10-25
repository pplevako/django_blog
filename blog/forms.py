from django import forms


class ArticleForm(forms.Form):
    title = forms.CharField(label='Title', max_length=200)
    text = forms.CharField(widget=forms.Textarea)
