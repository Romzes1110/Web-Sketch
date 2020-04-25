"""
Definition of forms.
"""

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _
from.models import Comment
from.models import Blog

class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'Имя пользователя'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Пароль'}))

class CommentForm (forms.ModelForm):
    class Meta:
        model = Comment     #Используемая модель
        fields = ('text',)  #Требуется заполнить только поле текст
        labels = {'text':"Комментарий"} #Метка к полю формы text
        widgets = {
            'text':forms.Textarea(attrs={'rows': 10,'class': 'form-control'})
            }

class BlogForm (forms.ModelForm):
    class Meta:
        model = Blog      #Используемая модель
        fields = ('title','description','content','posted','author','image',)
        labels = {'title':"Заголовок",'description':"Краткое описание",'content':"Содержание",'posted':"Дата",'author':"Автор",'image':"Изображение"}