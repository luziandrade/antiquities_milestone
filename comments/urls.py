from django.urls import path
from . import views

urlpatterns = [
    path('', views.create_questions, name='create_questions'),
    path('ask_questions', views.get_questions, name='get_questions'),
    path('questions/<int:id>', views.questions_detail, name='questions_detail')

]