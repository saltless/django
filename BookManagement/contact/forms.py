from django import forms

class ContactForm(forms.Form):
	subject = forms.CharField(max_length = 10)
	email = forms.EmailField(required = False, label = 'Your e-mail address')
	message = forms.CharField(widget = forms.Textarea)

	def clean_message(self):
		message = self.cleaned_data['message']
		lenth = len(message.split())
		if lenth < 4:
			raise forms.ValidationError('Not enough words!')
		return message
