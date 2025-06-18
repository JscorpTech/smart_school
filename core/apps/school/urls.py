from django.urls import path, include
from rest_framework.routers import DefaultRouter
from core.apps.school import views

router = DefaultRouter()
router.register("classroom", views.ClassroomView, basename="classroom")
router.register("question", views.QuestionView, basename="question")
router.register("questionset", views.QuestionSetView, basename="questionset")
router.register("topic", views.TopicView, basename="topic")
router.register("bob", views.BobView, basename="bob")

urlpatterns = [
    path("", include(router.urls)),
]
