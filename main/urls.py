"""locacaodecarros URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from .import views

# defina o nome do app como namespace
# logo, sempre que um namespace for passado no gerenciador de url
# saberá de qual aplicativo está tratando
# e qual arquivo urls deverá buscar o roteamento de urls
app_name = 'main'

# urlpatterns irá conter a lista de roteamento no gerenciador de urls
urlpatterns = [
    path('', views.index, name='index'),
]
