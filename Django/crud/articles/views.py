from django.shortcuts import render, redirect
from .models import Article
# 모델에서 아티클을 가져와라

# Create your views here.
def index(request):
    # Database 조회
    articles = Article.objects.all() # 모든 데이터

    context = {
        'articles': articles,

    }
    return render(request, 'articles/index.html', context)

def new(request): # GET
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')

        # Database에 저장
        # 1. Article 인스턴스 생성
        article = Article(title=title, content=content)
        # 2. 저장!
        article.save()

        # context = {
        #     'title': title,
        #     'content': content,
        # }    
        return redirect('articles:detail', article.pk)
    else:
        context = {
            
        }    
        return render(request, 'articles/new.html', context)

def create(request): # POST
    title = request.POST.get('title')
    content = request.POST.get('content')

    # Database에 저장
    # 1. Article 인스턴스 생성
    article = Article(title=title, content=content)
    # 2. 저장!
    article.save()

    # context = {
    #     'title': title,
    #     'content': content,
    # }    
    return redirect('articles:detail', article.pk)
    # return render(request, 'articles/create.html', context)    

def detail(request, pk):
    # Database 조회 : 단 하나의 data
    article = Article.objects.get(pk=pk)

    context = {
        'article': article,
    }
    return render(request, 'articles/detail.html', context)

def delete(request, pk): # POST
    # Database 삭제
    # 1. 조회
    article = Article.objects.get(pk=pk)
    # 2. 삭제
    article.delete()

    return redirect('articles:index')

def edit(request, pk): # GET
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        
        # 게시글 수정!
        title = request.POST.get('title')
        content = request.POST.get('content')

        # Database 조회 + 수정 + 저장
        # 1. 조회
        
        # 2. 수정
        article.title = title
        article.content = content    
        # 3. 저장
        article.save()

        return redirect('articles:detail', article.pk)
    else:
        # 게시글 수정 양식!

        # Database 조회( + 저장)
        # 1. 조회
        
        
        context = {
            'article' : article
        }
        return render(request, 'articles/edit.html', context)

def update(request, pk): # POST
    title = request.POST.get('title')
    content = request.POST.get('content')

    # Database 조회 + 수정 + 저장
    # 1. 조회
    article = Article.objects.get(pk=pk)
    # 2. 수정
    article.title = title
    article.content = content    
    # 3. 저장
    article.save()

    return redirect('articles:detail', article.pk)
