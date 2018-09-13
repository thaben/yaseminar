from django import forms
from django.contrib.auth.models import User
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit, Field
from django.forms.widgets import HiddenInput
from crispy_forms.bootstrap import PrependedAppendedText

from userprofile.models import Profile
  

class UserForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ('first_name', 'last_name')

	def __init__(self, *args, **kwargs):
		super(UserForm, self).__init__(*args, **kwargs)
		self.fields['first_name'].required = True
		self.fields['last_name'].required = True
		self.helper = FormHelper(self)
		self.helper.form_tag = False # xreiazete otan exoume 2 forms, gia na min gini render to tag <form> 2 fores, CRISPY FORMS
		#self.helper.form_class = 'form-horizontal'
		#self.helper.label_class = 'col-lg-2'
		#self.helper.field_class = 'col-lg-8'


class ProfileForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ('bio', 'affiliate', 'birth_date')


	def __init__(self, *args, **kwargs):
		super(ProfileForm, self).__init__(*args, **kwargs)
		self.fields['birth_date'].widget.attrs['placeholder'] = '12/12/1966'
		#hide_condition = kwargs.pop('hide_condition',None)
		#if hide_condition:
		#	self.fields['affiliate'].widget = HiddenInput()
		#if  self.instance.pk:
			# Since the pk is set this is not a new instance
			#del self.fields['affiliate']
		self.helper = FormHelper(self)
		self.helper.form_tag = False   # xreiazete otan exoume 2 forms, gia na min gini render to tag <form> 2 fores  , CRISPY FORMS
		self.helper.add_input(Submit('submit', 'Submit'))
		self.helper.layout = Layout(
            Field('bio', css_class="black-fields", rows="5"),
            Field('affiliate', css_id="black-fields"),
            Field('birth_date')
           		)

#eftiaksa auto edw epidi den mporousa naftiaksw sinthiki apo panw not DRY
class ProfileEditForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ('bio', 'birth_date')
	def __init__(self, *args, **kwargs):
		super(ProfileEditForm, self).__init__(*args, **kwargs)
		self.fields['birth_date'].widget.attrs['placeholder'] = '12/12/1966'
		self.helper = FormHelper(self)
		self.helper.form_tag = False   # xreiazete otan exoume 2 forms, gia na min gini render to tag <form> 2 fores  , CRISPY FORMS
		self.helper.add_input(Submit('submit', 'Submit'))