from django import forms

class AppoinmentForm(forms.Form):
    customerName = forms.CharField(label='Tên khách hàng', max_length=100)

    email = forms.EmailField(label="Email", max_length= 100)

    phoneNumber = forms.CharField(max_length=200)
