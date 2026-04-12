from django.contrib import admin
from django.urls import path, include
from sistema.views import Login

urlpatterns = [
    path('', Login.as_view(), name='index'),
    path('admin/', admin.site.urls),
    path('veiculo/', include('veiculo.urls'), name='veiculo'),
]
