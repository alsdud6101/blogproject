from django.shortcuts import render, get_object_or_404, redirect
from .models import Blog
from django.core.paginator import Paginator
from django.utils import timezone
from .form import BlogPost

def home(request):
    blogs = Blog.objects
    #블로그의 모든 글들을 대상으로
    blog_list = Blog.objects.all()
    #블로그 객체 세 개를 한 페이지로 자르기
    paginator = Paginator(blog_list,3)
    #request된 페이지가 뭔지를 알아내고 (request페이즈를 변수에 담아내고)
    page = request.GET.get('page')
    #request된 페이지를 얻어온 뒤 return 해준다
    posts = paginator.get_page(page)
    return render(request, 'home.html', {'blogs':blogs, 'posts':posts})

def detail (request, blog_id):
    details = get_object_or_404(Blog, pk = blog_id)
    return render(request, 'detail.html', {'details':details})

def new(request):
    return render(request, 'new.html')


def create(request):
    blog = Blog()
    blog.title = request.GET['title']
    blog.body = request.GET['body']
    blog.pub_date = timezone.datetime.now()
    blog.save()
    return redirect('/blog/'+str(blog.id))


def blogpost(request):
    #1. 입력된 내용을 처리하는 기능 POST
    #2. 빈 페이지를 띄워주는 기능 GET
    if request.method =='POST':
        form = BlogPost(request.POST)
        #form이라는 변수에 post방식으로 request된 데이터를 담아준다.
        if form.is_valid():
            #form에 올바른 입력값이 들어왔는지 검사하는 함수
            post = form.save(commit=False)
            #모델객체를 반환하지만 아직 저장하지 않고 가져온다.
            #post가 blog형 객체가 되었음
            post.pub_date = timezone.now()
            #현재 시간 넣어줌
            post.save()
            return redirect('home')
    else:
        form = BlogPost()
        return render(request, 'new.html', {'form':form})