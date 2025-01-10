from django import forms


class ReviewForm(forms.Form):
    username = forms.CharField(
        label="Your Name",
        min_length=2,
        max_length=100,
        error_messages={"required": "Username is required."},
    )

    review = forms.CharField(
        label="Your Feedback",
        widget=forms.Textarea,
        max_length=200,
        error_messages={"required": "Review is required."},
    )

    rating = forms.IntegerField(
        label="Your Rating",
        min_value=1,
        max_value=5,
        error_messages={"required": "Rating is required."},
    )
