from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse             # url처리를 위해서 reverse()함수 import.
from polls.models import Choice, Question


def index(request):
    latest_question_list = Question.objects.all().order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    # get_object_or_404()함수의 첫번째 인자는 모델 클래스, 두번째 인자부터는 검색 조건을 여러개사용가능
    # question 모델 클래스로부터 pk=question_id 검색 조건에 맞는 객체를 조회함.
    # 조건에 맞는 객체가 없을 경우, Http404익셉션을 발생시킴.
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        # request.POST는 제출된 폼의 데이터를 담고 있는 객체로서, 파이썬 사전처럼 키로 그 값을 구할 수 있음.
        # request.POST['choice']는 폼데이터에서 키가 'choice'에 해당하는 값인 choice.id를 스트링으로 리턴함.
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # 설문 투표 폼을 다시 보여준다.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # POST 데이터를 정상 처리하면,
        # 항상 HTTPResponseRedirect를 반환하여 리다이렉션 처리함.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})

# 함수형 뷰로 http GET 메소드 정의
def my_view(request):
    if request.method == 'GET':
        # 뷰 로직 생성
        return HttpResponse('result')

