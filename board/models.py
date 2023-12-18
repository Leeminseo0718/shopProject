from django.db import models
from django.utils import timezone


# Create your models here.
#-----------------------
# Board 모델(테이블)은
#-----------------------
#제목(subject)
#내용(content) 그리고
#작성일시 (crate_data)를 속성
#---------------------------
class Board(models.Model):
    # 상품명
    subject = models.CharField(max_length=200)
    # 가격
    price = models.IntegerField(default=0)
    # 이미지
    photo = models.ImageField(upload_to='shop/images/', default=timezone.now)
    # 카테고리
    category = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.subject









