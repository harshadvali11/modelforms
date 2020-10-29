from django import forms

from app.models import *

from django.utils.translation import gettext_lazy as l


#labels={'name':gettext_lazy('enter name')}

class TopicForm(forms.ModelForm):
    class Meta:
        model=Topic
        fields='__all__'

    
class WebpageForm(forms.ModelForm):
    class Meta:
        model=Webpage
        fields='__all__'
        #fields=['topic_name','name']
        #exclude=['name','url']
        widgets={'name':forms.Textarea(attrs={'cols':5,'rows':5}),'url':forms.PasswordInput}
        
        labels={'name':l('enter urname')}
        help_texts={'name':l('correct name')}
class AccessForm(forms.ModelForm):
    class Meta:
        model=Access_Records
        fields='__all__'