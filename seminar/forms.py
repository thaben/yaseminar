from django import forms

from seminar.models import Seminar,Category
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit, Field
from crispy_forms.bootstrap import PrependedAppendedText, AppendedText


class SeminarForm(forms.ModelForm): 
	#Category = forms.ModelChoiceField(queryset=Category.objects.all())  
	class Meta:        
		model = Seminar        
		fields = ('title', 'category', 'location', 'description', 'users_max')


	def __init__(self, *args, **kwargs):
		super(SeminarForm, self).__init__(*args, **kwargs)
		self.fields['location'].widget.attrs['placeholder'] = 'Athens,Greece'		
		self.helper = FormHelper(self)
		self.helper.form_tag = False 
		self.helper.layout = Layout( 
					Fieldset(
		                '',
		                'title',
		                'category',
		 	            AppendedText('location', '$', active=True),
		                'description',
		                'users_max'
            )		  
       	)
		