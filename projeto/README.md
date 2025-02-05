### Projeto: API para Sistema de Venda de Lanches

**Objetivo**: Criar uma API RESTful para o sistema de venda de lanches utilizando Django e Django Rest Framework (DRF). A API permitirá gerenciar clientes, produtos e pedidos, além de fornecer endpoints para registro e consulta de dados no sistema.

---

### Funcionalidades da API

1. **Gerenciamento de Clientes**: (2,5)
    - **Endpoint para listar clientes**. (0,5)
    - **Endpoint para recuperar cliente específico**. (0,5)
    - **Endpoint para cadastrar clientes**. (1,0)
    - **Endpoint para excluir clientes**. (0,5)

2. **Gerenciamento de Produtos**: (2,5)
    - **Endpoint para listar produtos**. (0,5)
    - **Endpoint para recuperar produto específico**. (0,5)
    - **Endpoint para cadastrar produtos**. (1,0)
    - **Endpoint para excluir produtos**. (0,5)

3. **Gerenciamento de Pedidos**: (5,0)
    - **Endpoint para criar pedidos**, associando um cliente e uma lista de produtos. (1,5)
    - **Endpoint para listar pedidos**, incluindo informações do cliente, produtos no pedido e o tipo de entrega (entrega ou retirada). (1,5)
    - **Endpoint para recuperar pedido específico**, incluindo informações do cliente, produtos no pedido e o tipo de entrega (entrega ou retirada). (2,0)

4. **Funcionalidades Extras**:
    - Cada pedido deve calcular automaticamente o total a ser pago com base nos preços dos produtos. (1,0)
    - Um endpoint para consultar o **histórico de pedidos de um cliente específico**. (1,0)

---

### Estrutura de Modelos

- **Cliente**:
    - `nome`: CharField
    - `cpf`: CharField
    - `endereco`: TextField
    - `historico_pedidos`: Relação com o modelo de pedidos (extra)

- **Produto**:
    - `nome`: CharField
    - `preco`: DecimalField

- **Pedido**:
    - `cliente`: ForeignKey (Cliente)
    - `produtos`: ManyToManyField (Produto)
    - `tipo_entrega`: CharField (opções: "entrega", "retirada")
    - `total`: DecimalField (calculado automaticamente com base nos produtos) (extra)

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
