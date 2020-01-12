from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.contrib.auth.models import User
from .models import Question
from .forms import QuestionForm


def get_questions(request):
    questions = Question.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'all_question.html', {'questions': questions})


def questions_detail(request, id):
    question = Question.objects.get(id=id)
    return render(request, 'one_question.html', {"question": question})


def create_questions(request):
    if request.method == "POST":
        form = QuestionForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()
            return redirect(get_questions)
    else:
        form = QuestionForm()
    return render(request, 'questions.html', {'form': form})
