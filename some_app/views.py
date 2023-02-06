from django.shortcuts import render
from django.views.generic import TemplateView
import logging

logger = logging.getlogger('mylogger')

def my_view(request, arg1, arg, bad_mojo=none):
    if bad_mojo:
        # error레벨의 로그 레코드를 생성함
        logger.error('Something went wrong!')

class AboutView(TemplateView):
    template_name = 'about.html'
