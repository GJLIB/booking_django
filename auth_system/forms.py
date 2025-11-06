from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from auth_system.models import User

class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields  = "__all__"
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control mb-3'})

class RegisterForm(UserCreationForm):
    class Meta:
        date_of_birth = forms.DateField(widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control mb-3'}))
        model = User
        fields  = ['first_name', 'last_name', 'username', 'email', 'phone', 'date_of_birth', 'password1', 'password2']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control mb-3'})

        self.field['date_of_birth'].widget.attrs.update({'type:' 'date'})