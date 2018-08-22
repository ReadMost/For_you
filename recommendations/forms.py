from django import forms
from django.forms import formset_factory

class RecommendationForm(forms.Form):
    rec_title = forms.CharField(
        label = 'Recommendation title',
        widget = forms.TextInput()
    )
    rec_description = forms.CharField(
        label = 'Recommendation description',
        widget = forms.TextInput()
    )
    # rec_profession = forms.ChoiceField(choices = [])

class StepForm(forms.Form):
    step_title = forms.CharField(
        label = 'Title for the Step',
        widget = forms.TextInput()
    )

class BulletForm(forms.Form):
    description = forms.CharField(
        label = 'Қысқа сипаттамасы',
        widget = forms.TextInput()
    )
    link = forms.CharField(
        label = 'Дерек көзіне ссылка',
        widget = forms.TextInput()
    )
BulletFormset = formset_factory(BulletForm, extra = 2)


class CommentForm(forms.Form):
    text = forms.CharField(
        label = '',
        widget = forms.TextInput(attrs={
            'placeHolder':'Оставьте комментарий'
        })
    )