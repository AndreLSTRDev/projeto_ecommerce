from django.test import TestCase

# loja/tests.py
from django.test import TestCase
from .models import Produto

class ProdutoTestCase(TestCase):
    def setUp(self):
        Produto.objects.create(nome="Produto 1", descricao="Descrição do produto 1", preco=10.00, categoria=None)

    def test_produto_criado(self):
        produto = Produto.objects.get(nome="Produto 1")
        self.assertEqual(produto.preco, 10.00)

    def test_produto_nome(self):
        produto = Produto.objects.get(nome="Produto 1")
        self.assertEqual(produto.nome, "Produto 1")