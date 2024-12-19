"""
URL configuration for TaskPro project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path, include
from django.http import HttpResponse
from django.urls import reverse

def some_view(request):
    # Correct reverse usage with 'id' as the keyword argument
    client_url = reverse('client_detail', kwargs={'id': 1})
    return HttpResponse(f'Client detail URL: {client_url}')

# Define a simple root view for "/"
def home(request):
    return HttpResponse("<h1>Welcome to TaskPro</h1><p><a href='/clients/'>View Clients</a></p>")

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin panel URL
    path('', home, name='home'),  # Root URL handler
    path('', include('TaskApp.urls')),  # Include app's URLs
    path('accounts/', include('django.contrib.auth.urls'))

]