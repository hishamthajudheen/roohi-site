from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'comment']
        widgets = {
            'rating': forms.Select(attrs={
                'class': 'w-full p-2 border border-gray-300 rounded-md focus:ring-2 focus:ring-red-400 focus:border-red-400'
            }),
            'comment': forms.Textarea(attrs={
                'class': 'w-full p-2 border border-gray-300 rounded-md focus:ring-2 focus:ring-red-400 focus:border-red-400',
                'rows': 4,
                'placeholder': 'Leave a comment...'
            }),
        }
