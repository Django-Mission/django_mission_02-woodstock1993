from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import RegexValidator
User = get_user_model() 

class Inquiry(models.Model):
    CATEGORY_A = 'A'
    CATEGORY_B = 'B'
    CATEGORY_C = 'C'
    CATEGORY_D = 'D'

    CATEGORY_CHOICES =(
        (CATEGORY_A,'category A'),
        (CATEGORY_B,'category B'),
        (CATEGORY_C,'category C'),
        (CATEGORY_D,'category D'),
    )
    
    category = models.CharField(max_length=256, choices=CATEGORY_CHOICES, default='others')
    question = models.CharField(verbose_name='문의 질문', max_length=80)
    comment = models.TextField(verbose_name='문의 내용')
    email = models.CharField(verbose_name='작성자 이메일', max_length=80)
    phone_number = models.CharField(
        max_length = 13,
        validators = [RegexValidator(r'^01([0|1|6|7|8|9]?)-([0-9]{3,4})-([0-9]{4})', message="Wrong format enter")],
        null = True,
        blank = True,
        verbose_name='전화번호',
        help_text = ("format: 010-1234-1234"),
    )
    writer =  models.ForeignKey(to=User, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(verbose_name='작성일', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='최종 수정일', auto_now=True)
    image = models.ImageField(verbose_name='이미지', null=True, blank=True)

class Answer(models.Model):
    writer = models.ForeignKey(to=User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(verbose_name='생성 일시')
    updated_at = models.DateTimeField(verbose_name='최종 수정 일시', auto_now=True)
    content = models.TextField(verbose_name='답변 내용')
    question_answer = models.ForeignKey(to='Inquiry', db_column='Inquiry_id', on_delete=models.CASCADE)