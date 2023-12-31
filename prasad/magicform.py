from django import forms
from prasad.models import*

class ContactInfoForm(forms.ModelForm):
    class Meta:
        model = ContactInfo
        fields = ['name','mobile','message']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Add a placeholder for the 'name' field
        self.fields['name'].widget.attrs.update({'placeholder': 'Enter your full name..'})    
        self.fields['mobile'].widget.attrs.update({'placeholder': 'Enter your mobile number ...'})        
        self.fields['message'].widget.attrs.update({'placeholder': 'write your message..'})    
        # Make label of the form empty 
        self.fields['name'].label=''
        self.fields['message'].label=''
        self.fields['mobile'].label=''
        