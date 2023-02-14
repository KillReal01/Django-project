from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  path('', views.index, name='home'),
                  path('employee', views.list, name='employee'),
                  path('sort/<slug:sort_slug>/', views.sort, name='sort'),
                  path('register', views.Registration.as_view(), name='register'),
                  path('verify', views.Login.as_view(), name='verify'),
                  path('logout', views.logout_user, name='logout'),
                  path('private', views.private, name='private'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
