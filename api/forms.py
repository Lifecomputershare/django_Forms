from django import forms

class RegisterForm(forms.Form):
    name = forms.CharField(max_length=100,required=True, label='Full Name',widget=forms.TextInput(attrs={'class':'block w-full rounded-md  py-1.5 text-base  outline-1 -outline-offset-1 outline-white/10 placeholder:text-gray-500 focus:outline-2 focus:-outline-offset-2 focus:outline-indigo-500 sm:text-sm/6', 'placeholder':'Enter your Full name','name':'fullname'}))

    email  = forms.EmailField(required=True, widget= forms.EmailInput(attrs={'type':'email','placeholder':'Enter your email','class':'block w-full rounded-md py-1.5 text-base  outline-1 -outline-offset-1 outline-white/10 placeholder:text-gray-500 focus:outline-2 focus:-outline-offset-2 focus:outline-indigo-500 sm:text-sm/6'}) )