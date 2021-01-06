from django.urls import path

from .views import (AskQuestionView,
                    QuestionDetailView,
                    CreateAnswerView,
                    UpdateAnswerAcceptance,
                    DailyQuestionList,
                    TodaysQuestionList,
                    SearchView, )

app_name = 'qanda'
urlpatterns = [
    path('ask', AskQuestionView.as_view(), name='ask'),
    path('q/search', SearchView.as_view(), name='question_search'),
    path('q/<int:pk>', QuestionDetailView.as_view(), name='question_detail'),
    path('q/<int:pk>/answer', CreateAnswerView.as_view(), name='answer_question'),
    path('a/<int:pk>/accept', UpdateAnswerAcceptance.as_view(), name='update_answer_acceptance'),
    path('daily/<int:year>/<int:month>/<int:day>/', DailyQuestionList.as_view(), name='daily_questions'),

    path('', TodaysQuestionList.as_view(), name='index'),

]
