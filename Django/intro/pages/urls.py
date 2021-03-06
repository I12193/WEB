from django.urls import path
from . import views

urlpatterns = [
     path('index/', views.index),
    path('hello/<name>/', views.hello),
    # 두 수를 입력 받아 곱한 결과를 보여주는 페이지
    path('times/<num1>/<num2>/', views.times),
    path('dtl/', views.dtl),
    # Is it your birthday? 오늘이 생일이면, '예', 아니면 '아니오'
    path('bday/', views.bday),
    path('throw/', views.throw),
    path('catch/', views.catch),
    # [로또 번호 생성기]
    # 로또 번호 몇 개를 생성할 것인지 input 으로 입력 받고,
    # 그 개수만큼 번호를 random으로 생성하여 보여주기
    path('lotto/', views.lotto),
    path('generate/', views.generate),
    path('user_new', views.user_new),
]