from django.contrib.auth.forms import (
    UserCreationForm,
    UserChangeForm,
)

from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    """Custome User Creaton Form"""

    class Meta:
        """This is the Meta class. it contains information"""

        # about how to get an instance of class created.
        # it is not common to se this, but Django dose for
        # certain things. Like this

        model = CustomUser
        fields = (
        "username", 
        "first_name", 
        "last_name", 
        "email", 
        "date_of_birth",
        )


class CustomUserChangeForm(UserChangeForm):
    """Custome User Change Form"""

    class Meta:
        """meta"""

        model = CustomUser
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
            "date_of_birth",
        )
