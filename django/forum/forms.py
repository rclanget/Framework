from django import forms

class AddArtcile(forms.Form):
    sujet = forms.CharField(max_length=150)
