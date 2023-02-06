from django.contrib import admin

# 생성한 모델 등록하기.
from polls.models import Question, Choice
from django import forms

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 2

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date Information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]                            # choice 모델 클래스 같이 보기
    list_display = ('question_text', 'pub_date')        # 레코드 리스트 컬럼 항목 지정
    list_filter = ['pub_date']                          # 필터 사이드 바 추가
    search_fields = ['question_text']                   # 검색 박스 추가

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)

class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)


