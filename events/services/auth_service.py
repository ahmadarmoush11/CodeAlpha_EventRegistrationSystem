from django.contrib.auth.models import User
from django.db import transaction

from events.models.user_profile import UserProfile, UserRole


class AuthService:

    @staticmethod
    @transaction.atomic
    def register_user(
        username,
        email,
        password,
        first_name="",
        last_name="",
    ):
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name,
        )

        UserProfile.objects.create(
            user=user,
            role=UserRole.ATTENDEE,
        )

        return user