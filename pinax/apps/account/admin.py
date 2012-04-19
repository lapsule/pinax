from django.contrib import admin

from pinax.apps.account.models import Account, PasswordReset


class PasswordResetAdmin(admin.ModelAdmin):
    list_display = ["user", "temp_key", "timestamp", "reset"]


class MyUserCreationForm(UserCreationForm):
    username = forms.RegexField(
            label = 'Username',
            max_length = 30,
            regex = u"^[\w-]+|[\u4e00-\u9fa5]+$",
            help_text = 'Required. 30 characters or fewer. Alphanumeric characters only (letters, digits, hyphens and underscores).',
            error_message = 'This value must contain only letters, numbers, hyphens and underscores.')

class MyUserChangeForm(UserChangeForm):
    username = forms.RegexField(
        label = 'Username',
        max_length = 30,
        regex = u'^[\w-]+|[\u4e00-\u9fa5]+$',
        help_text = 'Required. 30 characters or fewer. Alphanumeric characters only (letters, digits, hyphens and underscores).',
        error_message = 'This value must contain only letters, numbers, hyphens and underscores.')

class MyUserAdmin(UserAdmin):
    form = MyUserChangeForm
    add_form = MyUserCreationForm


admin.site.unregister(User)
admin.site.register(User,MyUserAdmin)


admin.site.register(Account)
admin.site.register(PasswordReset, PasswordResetAdmin)
