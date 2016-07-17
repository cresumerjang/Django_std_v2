from django.db import models
from django.conf import settings

class Member(models.Model):
    # OneToOneField는 기존 테이블을 확장해서 다른 테이블을 만들 때 유용
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    # 모델의 제약조건 매개변수의 name은 실제 테플릿 필드에서 꺼내쓸때 사용가능
    # ->즉 queryset에서 참조 가능한 맵핑된 이름
    # name = models.CharField(name='이름', max_length=30, blank=False, null=False)
    # age = models.IntegerField(name='나이', blank=True, null=True)
    # sex = models.CharField(name='성별', max_length=2, blank=True, null=True)
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    sex = models.CharField(max_length=2)
