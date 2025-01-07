from django import forms


class ReviewForm(forms.Form):
    username = forms.CharField(
        label="Your Name",
        max_length=100,
        error_messages={"required": "Username is required."},
    )
    # review = forms.CharField(
    #     label="Your Review",
    #     widget=forms.Textarea,
    #     error_messages={"required": "Review is required."},
    # )
