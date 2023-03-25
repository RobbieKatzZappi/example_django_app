from django import forms

class RequestDocumentForm(forms.Form):
    document_type = forms.CharField(label='Document type', max_length=100)
