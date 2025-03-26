from django.contrib import admin
#명시적 상대경로 '.' 현재위치에 잇는 models 모듈에서 Article 가져오기
from .models import Article
# Register your models here.
admin.site.register(Article)
