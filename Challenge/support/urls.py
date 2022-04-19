from django.urls import path
from .views import faq, support_index, answer

app_name = 'support'

urlpatterns = [
    path('', support_index, name='support_index'),
    path('faq/', faq, name='faq'),
    path('answer/', answer, name='answer')
]