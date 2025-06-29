from django.contrib.auth import models as auth_models
from django.db import models
from django_core.models import AbstractBaseModel
from ..choices import RoleChoice
from ..managers import UserManager
from django.utils.translation import gettext_lazy as _


class User(auth_models.AbstractUser):
    phone = models.CharField(max_length=255, unique=True)
    username = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    validated_at = models.DateTimeField(null=True, blank=True)
    role = models.CharField(
        max_length=255,
        choices=RoleChoice,
        default=RoleChoice.STUDENT,
    )

    USERNAME_FIELD = "phone"
    objects = UserManager()

    @classmethod
    def _create_fake(self):
        return self.objects.create(
            phone="123456789",
            username="123456789",
            first_name="John",
            last_name="Doe",
        )

    def __str__(self):
        return self.phone


class StudentModel(AbstractBaseModel):
    user = models.OneToOneField(User, verbose_name=_("user"), on_delete=models.CASCADE, related_name="student")
    balance = models.PositiveIntegerField(default=0)
    ball = models.PositiveIntegerField(default=0)
    avatar = models.ImageField(null=True, blank=True, upload_to="avatar/default.jpg")
    ice = models.PositiveIntegerField(default=0)

    def __str__(self):
        return str(self.pk)

    @classmethod
    def _create_fake(self):
        return self.objects.create(
            user=User._create_fake(),
            balance=100,
            ball=0,
            ice=0,
        )

    class Meta:
        db_table = "student"
        verbose_name = _("StudentModel")
        verbose_name_plural = _("StudentModels")


class ParentModel(AbstractBaseModel):
    user = models.OneToOneField(User, verbose_name=_("user"), on_delete=models.CASCADE, related_name="parent")
    children = models.ManyToManyField(
        "StudentModel", verbose_name=_("children"), through="ChildrenModel", through_fields=("parent", "student")
    )

    def __str__(self):
        return str(self.pk)

    @classmethod
    def _create_fake(self):
        return self.objects.create(
            user=User._create_fake(),
        )

    class Meta:
        db_table = "parent"
        verbose_name = _("ParentModel")
        verbose_name_plural = _("ParentModels")


class ChildrenModel(AbstractBaseModel):
    parent = models.ForeignKey(ParentModel, verbose_name=_("parent"), on_delete=models.CASCADE)
    student = models.ForeignKey(StudentModel, verbose_name=_("student"), on_delete=models.CASCADE)
    is_confirmed = models.BooleanField(default=False)

    def __str__(self):
        return str(self.pk)

    @classmethod
    def _create_fake(self):
        return self.objects.create(
            parent=ParentModel._create_fake(),
            student=StudentModel._create_fake(),
        )

    class Meta:
        db_table = "children"
        verbose_name = _("ChildrenModel")
        verbose_name_plural = _("ChildrenModels")
