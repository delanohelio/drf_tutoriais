### Projeto: API para Sistema de Venda de Lanches

**Objetivo**: Criar uma API RESTful para o sistema de venda de lanches utilizando Django e Django Rest Framework (DRF). A API permitirá gerenciar clientes, produtos e pedidos, além de fornecer endpoints para registro e consulta de dados no sistema.

---

### Funcionalidades da API

1. **Gerenciamento de Clientes**:
    - **Endpoint para listar clientes**.
    - **Endpoint para recuperar cliente específico**.
    - **Endpoint para cadastrar clientes**.
    - **Endpoint para excluir clientes**.

2. **Gerenciamento de Produtos**:
    - **Endpoint para listar produtos**.
    - **Endpoint para recuperar produto específico**.
    - **Endpoint para cadastrar produtos**.
    - **Endpoint para excluir produtos**.

3. **Gerenciamento de Pedidos**:
    - **Endpoint para criar pedidos**, associando um cliente e uma lista de produtos.
    - **Endpoint para listar pedidos**, incluindo informações do cliente, produtos no pedido e o tipo de entrega (entrega ou retirada).
    - **Endpoint para recuperar pedido específico**, incluindo informações do cliente, produtos no pedido e o tipo de entrega (entrega ou retirada).

4. **Funcionalidades Extras**:
    - Cada pedido deve calcular automaticamente o total a ser pago com base nos preços dos produtos.
    - Um endpoint para consultar o **histórico de pedidos de um cliente específico**.

---

### Estrutura de Modelos

- **Cliente**:
    - `nome`: CharField
    - `cpf`: CharField
    - `endereco`: TextField
    - `historico_pedidos`: Relação com o modelo de pedidos

- **Produto**:
    - `nome`: CharField
    - `preco`: DecimalField

- **Pedido**:
    - `cliente`: ForeignKey (Cliente)
    - `produtos`: ManyToManyField (Produto)
    - `tipo_entrega`: CharField (opções: "entrega", "retirada")
    - `total`: DecimalField (calculado automaticamente com base nos produtos)

---

### Endpoints Sugeridos

1. **Clientes**:
    - `GET /clientes/`: Lista todos os clientes.
    - `GET /clientes/<id>`: Recupera um cliente.
    - `POST /clientes/`: Cadastra um novo cliente.
    - `DELETE /clientes/<id>/`: Remove um cliente.

2. **Produtos**:
    - `GET /produtos/`: Lista todos os produtos.
    - `GET /produtos/<id>`: Recupera um produto.
    - `POST /produtos/`: Cadastra um novo produto.
    - `DELETE /produtos/<id>/`: Remove um produto.

3. **Pedidos**:
    - `GET /pedidos/`: Lista todos os pedidos.
    - `GET /pedidos/<id>`: Recupera um pedido.
    - `POST /pedidos/`: Cria um novo pedido.

4. **Extras**:
    - `GET /clientes/<id>/historico/`: Retorna o histórico de pedidos de um cliente específico.

---

### Passos do Projeto

1. **Configuração do Projeto**:
    - Criar um projeto Django chamado `sistema_lanches`.
    - Criar um app chamado `api_lanches`.

2. **Criação dos Modelos**:
    - Criar os modelos `Cliente`, `Produto` e `Pedido` conforme a estrutura definida.

3. **Serializers**:
    - Criar serializers para os modelos, permitindo conversão entre JSON e objetos Django.

4. **Views**:
    - Implementar views usando `@api_view` ou `APIView` para lidar com as operações dos endpoints.

5. **Rotas**:
    - Configurar URLs para os endpoints no arquivo `urls.py` do app `api_lanches`.
