from django import forms


class ProfileForm(forms.Form):
    # This is taking the place of the form in the template, which for us right now is ONLY the file upload input.
    user_image = forms.ImageField()
