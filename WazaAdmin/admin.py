from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.urls import path
from .models import User, Message
from .forms import CustomUserChangeForm, CustomUserCreationForm,CustomUserPassForm,AdminPasswordChangeForm
from django.utils.translation import gettext_lazy as _
from .views import AdminStatsView,MessageAdminView

# SITE
class WazaAdminSite(admin.AdminSite):
    site_header = "My admin"
    site_title = 'My admin'
    # custom_urls = []
    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            
            path('stats/', self.admin_view(AdminStatsView.as_view()), name='stats'),
            path("messages/",self.admin_view(MessageAdminView.as_view()),name='messages')
        ]
            # Add more custom URLs as needed
        
        return custom_urls + urls
    
    
    def add_url(self,endpoint,view,name):
        self.custom_urls.append(path(endpoint,self.admin_view(view),name=name))

waza_admin = WazaAdminSite(name='waza_admin')
# Register your models here.
# @waza_admin.register(User)

class CustomUserAdmin(admin.ModelAdmin):
    add_form = CustomUserCreationForm
    
    form = CustomUserChangeForm
    change_password_form = AdminPasswordChangeForm
    model = User
    list_display = ("username","email", "is_staff", "is_active",)
    list_filter = ("email", "is_staff", "is_active",)
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (_("Personal info"), {"fields": ("first_name", "last_name", "email")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
        ("Other Details", {"fields": ('profile_pic','role')})

    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("username", "password1", "password2"),
            },
        ),
    )
    search_fields = ("username", "first_name", "last_name", "email")
    
  
  
class MessageAdmin(admin.ModelAdmin):
    pass

waza_admin.register(Message,MessageAdmin)
waza_admin.register(User,CustomUserAdmin)