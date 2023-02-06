from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View

# 클래스형 뷰로 HTTP GET 메소드 정의
class MyView(View):
    def get(self, request):
        # 뷰 로직 작성
        return HttpResponse('result')

