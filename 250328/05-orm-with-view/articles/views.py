from django.shortcuts import render, redirect
from .models import Article


# 메인 페이지를 응답하는 함수 (+ 전체 게시글 목록)
def index(request):
    # DB에 전체 게시글 요청 후 가져오기
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)

#특정 단일 게시물의 상세 페이지를 응답 (+단일 게시물 조회 기능이 필요)
def detail(request, pk):
    #pk로 들어온 정수 값을 활용해서 db에 id==pk인 게시글을 조회 요청
    article = Article.objects.get(pk=pk) #모델클래스.매니저(쿼리셋 api의 메서드 제공).get(pk=pk)
    context = {
        'article' : article,
    }
    return render(request, 'articles/detail.html', context)
#게시글 작성을 위한 페이지를 제공하는 함수
def new(request):
    return render(request, 'articles/new.html')

#사용자로부터 데이터를 받아 저장하고 저장이 완료되었따는 페이지를 제공하는 함수수
def create(request):
    #사용자로부터 받은 데이터 추출출(request가 그 데이터임임)
    title = request.POST.get('title')
    content = request.POST.get('content')
    
    #DB에 저장 요청(3가지 방법)
    # #1.
    # article = Article()
    # article.title = title
    # article.content = content
    # article.save() 

    # #2.
    article = Article(title=title, content=content) #초기값을 넣은 상태에서 인스턴스 생성
    #유효성검사
    article.save()
    return redirect('articles:detail', article.pk)

    #3.
    # Article.objects.create(title=title, content=content)
    # return render(request, 'articles/create.html')
    #유효성검사가 필요없는 경우에만 3번 방법 사용용


def delete(request, pk):
    # 어떤 게시글을 지우는지 먼저 조회
    article = Article.objects.get(pk=pk)
    #DB에 삭제 요청
    article.delete()
    return redirect('articles:index') 

def edit(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article' : article,
    }
    return render(request, 'articles/edit.html', context)