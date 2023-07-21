from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AdminPasswordChangeForm

from .models import User


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ("email","password1","password2")


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = User
        fields = ("email",)


class CustomUserPassForm(AdminPasswordChangeForm):
#    is_staff = forms.BooleanField(initial=False)
 #   is_superuser = forms.BooleanField(initial=False)

    #fields = ['is_staff','is_superuser']
    def save(self, commit=True):
        password = self.cleaned_data["password1"]
        self.user.set_password(password)
        print(self.user)
        if commit:
            self.user.save()
        return self.user