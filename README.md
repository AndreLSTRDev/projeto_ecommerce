# Projeto E-commerce

Este é um projeto de e-commerce desenvolvido para fins de aprendizado e demonstração de habilidades em desenvolvimento web.

## Tecnologias Utilizadas

- **Backend:** Python (Django)
- **Frontend:** HTML, CSS, JavaScript
- **Banco de Dados:** SQLite (pode ser alterado para PostgreSQL ou MySQL)
- **Controle de Versão:** Git e GitHub

## Funcionalidades

- Cadastro e autenticação de usuários
- Catálogo de produtos
- Carrinho de compras
- Processamento de pedidos
- Dashboard de administração

## Como Executar o Projeto

1. Clone o repositório:
   ```bash
   git clone https://github.com/SeuUsuario/projeto_ecommerce.git
   ```
2. Acesse o diretório do projeto:
   ```bash
   cd projeto_ecommerce
   ```
3. Crie um ambiente virtual e ative-o:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Para Linux/Mac
   venv\Scripts\activate  # Para Windows
   ```
4. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
5. Execute as migrações do banco de dados:
   ```bash
   python manage.py migrate
   ```
6. Inicie o servidor local:
   ```bash
   python manage.py runserver
   ```
7. Acesse o sistema pelo navegador: `http://127.0.0.1:8000`

## Melhorias Futuras

- Integração com API de pagamento
- Implementação de avaliações de produtos
- Melhorias na responsividade do design

## Contribuição

Caso queira contribuir, sinta-se à vontade para abrir uma issue ou enviar um pull request!

## Autor

Desenvolvido por André Rocha (https://github.com/AndreLSTRDev).
