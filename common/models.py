from django.db import models

# 모든 어플리케이션에서 공통으로 사용하는 속성: Common
class CommonModel(models.Model):

    """ Common Model Definition """
    created_at = models.DateTimeField(auto_now_add=True) # 필드의 값을 해당 object가 처음 생성되었을 때의 시간으로 설정
    updated_at = models.DateTimeField(auto_now=True) # Object가 저장될 때마다 해당 필드를 현재 date로 설정

# # common model은 데이터베이스에서 실제 데이터로 사용되지 않는다!
class Meta:
    abstract = True