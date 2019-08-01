from django.urls import path
from . import views

app_name='blog'
urlpatterns=[
    path('login/',views.login,name='login'),
    path('login/log_action',views.log_action,name='log_action'),
    path('login/regist_action',views.regist_action,name='regist_action'),
    path('index/',views.index,name='index'),
    path('article/<int:article_id>/',views.article_page,name='article_page'),
    path('edit/<int:article_id>/',views.edit_page,name='edit_page'),
    path('edit/action/',views.edit_action,name='edit_action'),
    path('delete/<int:article_id>',views.deleteArticle,name='delete_page')
]