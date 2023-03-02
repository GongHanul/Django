from django.shortcuts import render
from .models import Question
# from django.http import HttpRespons

def index(request):
    question_list = Question.objects.order_by('-create_date')
    context = {'question_list': question_list}
    return render(request, 'pybo/question_list.html', context)    
    # return HttpResponse("안녕하세요 pybo에 오신 것을 환영합니다.")

