from django.db import models

# Modelo para armazenar categorias de produtos
class Categoria(models.Model):
    nome = models.CharField(max_length=255)  # Nome da categoria

    def __str__(self):
        return self.nome  # Representação em texto da categoria

# Modelo para armazenar os produtos do e-commerce
class Produto(models.Model):
    nome = models.CharField(max_length=255)  # Nome do produto
    descricao = models.TextField()  # Descrição detalhada do produto
    preco = models.DecimalField(max_digits=10, decimal_places=2)  # Preço do produto
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)  # Relacionamento com a categoria

    def __str__(self):
        return self.nome  # Representação em texto do produto
