from typing import Any
from django import  forms

class SignUpForm(forms.Form):
    username = forms.CharField(label='Usuario:', min_length=6, max_length=12, required=True, 
                               widget=forms.TextInput(attrs={'placeholder': 'Ej. mpachacama'}))#widget=componenet en el html 
    
    email=forms.CharField(label='Email:',max_length=75,required=True, 
                          widget=forms.EmailInput(attrs={'placeholder':'maypachacama@hotmail.com'}))
    
    nombres=forms.CharField(label='Nombres:',max_length=50,required=True, 
                          widget=forms.TextInput(attrs={'placeholder':'Mayra Alexandra'}))
    
    apellidos=forms.CharField(label='Apellidos:',max_length=50,required=True, 
                          widget=forms.TextInput(attrs={'placeholder':'Pachacama Cuzco'}))
    
    

    password = forms.CharField(label='Password:', min_length=8, max_length=12, required=True, 
                               widget=forms.PasswordInput(attrs={'placeholder': 'Ej. tuContrasen@'}))

    password2 = forms.CharField(label='Repita Contraseña:', min_length=8, max_length=12, required=True, 
                               widget=forms.PasswordInput(attrs={'placeholder': 'Ej. tuContrasen@'}))

    def clean(self):  #recoge los datos de los campos anteriores despues de las validaciones
        cleaned_data=super(SignUpForm,self).clean()
        password=cleaned_data.get('password')
        confirm_password=cleaned_data.get('password2')
        if password != confirm_password:
            self.add_error('password2', 'Las contraseñas no coinciden') #sobre el campo, se presenta el mensaje

        return cleaned_data