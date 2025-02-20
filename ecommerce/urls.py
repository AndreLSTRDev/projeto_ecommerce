from django.contrib import admin  # Importa o módulo de administração do Django
from django.urls import path, include  # Importa as funções para definir rotas
from rest_framework.routers import DefaultRouter  # Importa o roteador para a API REST
from loja.views import CategoriaViewSet, ProdutoViewSet  # Importa as views da aplicação

# Criação de um roteador para registrar automaticamente as rotas da API
router = DefaultRouter()
router.register(r'categorias', CategoriaViewSet)  # Registra a rota para categorias
router.register(r'produtos', ProdutoViewSet)  # Registra a rota para produtos

# Definição das URLs da aplicação
urlpatterns = [
    path('admin/', admin.site.urls),  # Rota para acessar o painel administrativo do Django
    path('api/', include(router.urls)),  # Inclui todas as rotas registradas no roteador da API
]
