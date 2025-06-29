"""
Create a new user/superuser
"""

from django.contrib.auth import get_user_model
from core.apps.accounts.models import StudentModel, ParentModel
from core.apps.accounts.choices import RoleChoice


class UserSeeder:
    def run(self):
        parent = get_user_model().objects.create_superuser("998888112309", "2309", role=RoleChoice.PARENT)
        student = get_user_model().objects.create_user("998943990509", "2309", role=RoleChoice.STUDENT)
        StudentModel.objects.get_or_create(user=student)
        ParentModel.objects.get_or_create(user=parent)
