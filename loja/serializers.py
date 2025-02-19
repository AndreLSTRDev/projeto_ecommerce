

from rest_framework import serializers
from .models import Produto, Categoria, Cliente, Pedido

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'

class ProdutoSerializer(serializers.ModelSerializer):
    categoria = CategoriaSerializer()  # Serializa a categoria aninhada
    class Meta:
        model = Produto
        fields = '__all__'

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

class PedidoSerializer(serializers.ModelSerializer):
    produtos = ProdutoSerializer(many=True)  # Serializa os produtos aninhados
    cliente = ClienteSerializer()  # Serializa o cliente aninhado
    class Meta:
        model = Pedido
        fields = '__all__'