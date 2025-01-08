from django import forms


class ReviewForm(forms.Form):
    username = forms.CharField(
        label="Your Name",
        max_length=100,
        min_length=2,
        error_messages={"required": "Username is required."},
    )
