from django.db.models import Count
from django.shortcuts import render, redirect
from .models import *
from .forms import *



def question_form(request):
    '''Форма подачи вопроса, добавляем заданный вопрос в таблицу 1'''
    if request.method == 'POST':
        form_add_question = AddQuestionForm(request.POST)
        form_enterprise = EnterpriseForm(request.POST)
        if form_add_question.is_valid() and form_enterprise.is_valid():
            form_add_question.save()
            form_enterprise.save()
            return redirect('question_list')
    else:
        form_add_question = AddQuestionForm()
        form_enterprise = EnterpriseForm()
    context = {
        'form_enterprise': form_enterprise,
        'form_add_question': form_add_question,
    }
    return render(request, 'app_question/question_form.html', context)


def question_list(request):
    '''выводим таблицу вопросы и статистику поданных вопросов'''
    questions = Question.objects.all()
    stats = Question.objects.select_related(
        'enterprise__division').values(
        'enterprise__division__name',
        'enterprise__name').annotate(
        question_count=Count('question')
    )
        # SELECT "app_question_division"."name",
        #     "app_question_enterprise"."name",
        #     COUNT("app_question_question"."question") AS "question_count"
        # FROM "app_question_question"
        # INNER JOIN "app_question_enterprise"
        #     ON ("app_question_question"."enterprise_id" = "app_question_enterprise"."id")
        # INNER JOIN "app_question_division"
        #     ON ("app_question_enterprise"."division_id" = "app_question_division"."id")
        # GROUP BY "app_question_division"."name",
        #         "app_question_enterprise"."name"
        # LIMIT 21
    context = {
        'questions': questions,
        'stats': stats,
    }
    return render(request, 'app_question/question_list.html', context)


