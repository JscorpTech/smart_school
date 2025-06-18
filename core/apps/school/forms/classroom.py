from django import forms

from core.apps.school.models import ClassroomModel


class ClassroomForm(forms.ModelForm):

    class Meta:
        model = ClassroomModel
        fields = "__all__"
