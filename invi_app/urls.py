from django.urls import path, include

from . import views

urlpatterns = [
    path('about/', views.about, name="about"), #about(소개) 페이지
    path('search/', views.search, name="search"), #검색 페이지
    path('search/highhits/', views.search_highhits, name="search_highhits"), #검색 조회수 정렬 페이지
    path('search/highprice/', views.search_highprice, name="search_highprice"), #검색 높은가격순 정렬 페이지
    path('search/lowprice/', views.search_lowprice, name="search_lowprice"), #검색 낮은가격순 정렬 페이지
    path('save/', views.save, name="save"), # 좋아요 저장
    path('mypage/', views.mypage, name="mypage"), # 좋아요 저장한 후 마이페이지로 이동
    path('signup/', views.signup, name="signup"), #회원가입 페이지
    path('login/', views.login, name="login"), #로그인 페이지
    path('findpw/', views.findpw, name="findpw"), #비밀번호찾기 페이지
    path('changepw/', views.changepw, name="changepw"), #비밀번호 재설정 페이지
    path('auth_number/', views.auth_number, name="auth_number"), #인증번호 입력 페이지
    path('logout/', views.logout, name='logout'), # 로그아웃 페이지
    path('likedlecture/',views.likedlecture, name='likedlecture'), #좋아요한 강의 페이지
    path('selectkeyword/',views.selectkeyword, name='selectkeyword'), #선호하는 키워드 페이지
    path('mytype/',views.mytype, name='mytype'), #나의 강의타입 페이지
    path('accounts/', include('allauth.urls')), #소셜로그인
    path('hackathon_event/',views.hackathon_event, name="hackathon_event"), #해커톤 이벤트 페이지
]


    
    
   