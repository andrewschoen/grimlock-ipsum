from django import forms

CASE_CHOICES = (
    ('quiet', 'Quiet Grimlock'),
    ('loud', 'FULL GRIMLOCK'),
    
)
PARAGRAPH_CHOICES = [(x + 1, x + 1) for x in range(5)]

class GrimlockIpsumForm(forms.Form):
    paragraphs = forms.ChoiceField(label="PARAGRAPH?",
                            choices=PARAGRAPH_CHOICES, initial=3)
    type = forms.ChoiceField(label="TYPE?", choices=CASE_CHOICES,
                            initial="quiet", widget=forms.RadioSelect)
    