"""
URL configuration for mkr2 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from books.views import author_list,author_detail,book_list,book_detail

urlpatterns = [
    path('admin/', admin.site.urls),
    path('author_list/',author_list, name='author_list' ),
    path('<int:author_id>/',author_detail, name='author_detail' ),
    path('book_list/',book_list, name='book_list' ),
    path('<int:book_id>/',book_detail, name='book_detail' ),
]
