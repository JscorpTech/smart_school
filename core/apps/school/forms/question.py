from django import forms

from core.apps.school.models import BobModel, QuestionModel, QuestionSetModel, TopicModel


class BobForm(forms.ModelForm):

    class Meta:
        model = BobModel
        fields = "__all__"


class TopicForm(forms.ModelForm):
    class Meta:
        model = TopicModel
        fields = "__all__"


class QuestionForm(forms.ModelForm):
    class Meta:
        model = QuestionModel
        fields = "__all__"


class QuestionsetForm(forms.ModelForm):

    class Meta:
        model = QuestionSetModel
        fields = "__all__"
