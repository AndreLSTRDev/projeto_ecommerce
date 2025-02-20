

from django.contrib import admin  # Importa o módulo de administração do Django
from .models import Categoria, Produto  # Importa os modelos que serão registrados no painel administrativo

# Registra o modelo Categoria para que possa ser gerenciado pelo painel administrativo do Django
@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome')  # Define os campos exibidos na lista de categorias
    search_fields = ('nome',)  # Adiciona um campo de busca baseado no nome

# Registra o modelo Produto para gerenciamento no painel administrativo
@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'preco', 'categoria')  # Define os campos exibidos na lista de produtos
    search_fields = ('nome',)  # Permite buscar produtos pelo nome
    list_filter = ('categoria',)  # Adiciona um filtro baseado na categoria dos produtos
