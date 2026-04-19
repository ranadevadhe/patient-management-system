from django.contrib import admin
from django.urls import path, include
from hospital.views import login_view
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', login_view, name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('', include('hospital.urls')),
]
