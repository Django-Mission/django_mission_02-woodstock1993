from django.shortcuts import render
from .models import Inquiry, Answer


def support_index(request):
    return render(request, 'index.html')


def faq(request):
    inquire_list = Inquiry.objects.all()
    context = {'inquire_list': inquire_list}
    return render(request, 'support/faq.html', context)


def answer(request):
    answer_list = Answer.objects.all()
    context = {'answer_list': answer_list}
    return render(request, 'support/answer.html', context)