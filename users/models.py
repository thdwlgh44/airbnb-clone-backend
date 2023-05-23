from django.db import models
from django.contrib.auth.models import AbstractUser # custom User로 사용할 수 있도록 해주는 패키지

# Create your models here.
class User(AbstractUser):
    # 성과 이름을 덮어쓰고 한국식 이름을 새로 만든다.
    first_name = models.CharField(max_length=150, editable=False)
    last_name = models.CharField(max_length=150, editable=False)
    name = models.CharField(max_length=150, default="")
    is_host = models.BooleanField(default=False) # non-nullableField