import requests

BASE_URL = "http://127.0.0.1:8000"  # Altere se necessário

# Armazena IDs criados para dependências entre endpoints
cliente_id = None
produto_id = None
pedido_id = None

# Estrutura de testes organizada na ordem correta
testes = {
    "Gerenciamento de Clientes": [
        ("Cadastrar cliente", "POST", "/clientes/", 1.0, {"nome": "João", "cpf": "12345678900", "endereco": "Rua A, 123"}),
        ("Listar clientes", "GET", "/clientes/", 0.5),
        ("Recuperar cliente específico", "GET", None, 0.5),
    ],
    "Gerenciamento de Produtos": [
        ("Cadastrar produto", "POST", "/produtos/", 1.0, {"nome": "Hamburguer", "preco": 15.50}),
        ("Listar produtos", "GET", "/produtos/", 0.5),
        ("Recuperar produto específico", "GET", None, 0.5),
    ],
    "Gerenciamento de Pedidos": [
        ("Criar pedido", "POST", "/pedidos/", 1.5, None),
        ("Listar pedidos", "GET", "/pedidos/", 1.5),
        ("Recuperar pedido específico", "GET", None, 2.0),
    ],
    "Funcionalidades Extras": [
        ("Calcular total do pedido automaticamente", "GET", None, 1.0),
        ("Consultar histórico de pedidos de um cliente", "GET", None, 1.0),
    ],
    "Exclusão de Dados": [
        ("Excluir pedido", "DELETE", None, 0.5),
        ("Excluir cliente", "DELETE", None, 0.5),
        ("Excluir produto", "DELETE", None, 0.5),
    ],
}

def testar_endpoint(metodo, url, nota, data=None):
    """Faz uma requisição HTTP e retorna (status, resposta)."""
    full_url = BASE_URL + url
    try:
        if metodo == "GET":
            response = requests.get(full_url)
        elif metodo == "POST":
            response = requests.post(full_url, json=data)
        elif metodo == "DELETE":
            response = requests.delete(full_url)
        else:
            print(f"Método {metodo} não suportado.")
            return False, None

        return response.status_code in [200, 201, 204], response.json() if response.status_code in [200, 201] else None
    except requests.exceptions.RequestException:
        return False, None

def testar_api():
    global cliente_id, produto_id, pedido_id
    total_pontos = 0
    total_maximo = sum(nota for categoria in testes.values() for _, _, _, nota, *_ in categoria)

    print("\n=== Resultados dos Testes ===\n")

    for categoria, casos in testes.items():
        print(f"\n{categoria}:\n" + "-" * len(categoria))
        for caso in casos:
            nome, metodo, url, nota, *data = caso

            # Ajustar URLs e dados para chamadas dependentes
            if nome == "Recuperar cliente específico":
                if cliente_id:
                    url = f"/clientes/{cliente_id}/"
                else:
                    print(f"{nome}: ❌ NÃO TESTADO (Cliente não criado)\n")
                    continue
            elif nome == "Recuperar produto específico":
                if produto_id:
                    url = f"/produtos/{produto_id}/"
                else:
                    print(f"{nome}: ❌ NÃO TESTADO (Produto não criado)\n")
                    continue
            elif nome == "Criar pedido":
                if cliente_id and produto_id:
                    data = [{"cliente_id": cliente_id, "produtos": [produto_id], "tipo_entrega": "entrega"}]
                else:
                    print(f"{nome}: ❌ NÃO TESTADO (Cliente ou Produto ausente)\n")
                    continue
            elif nome == "Recuperar pedido específico" or nome == "Calcular total do pedido automaticamente":
                if pedido_id:
                    url = f"/pedidos/{pedido_id}/"
                else:
                    print(f"{nome}: ❌ NÃO TESTADO (Pedido não criado)\n")
                    continue
            elif nome == "Consultar histórico de pedidos de um cliente":
                if cliente_id:
                    url = f"/clientes/{cliente_id}/historico/"
                else:
                    print(f"{nome}: ❌ NÃO TESTADO (Cliente não criado)\n")
                    continue
            elif nome == "Excluir pedido":
                if pedido_id:
                    url = f"/pedidos/{pedido_id}/"
                else:
                    print(f"{nome}: ❌ NÃO TESTADO (Pedido não criado)\n")
                    continue
            elif nome == "Excluir cliente":
                if cliente_id:
                    url = f"/clientes/{cliente_id}/"
                else:
                    print(f"{nome}: ❌ NÃO TESTADO (Cliente não criado)\n")
                    continue
            elif nome == "Excluir produto":
                if produto_id:
                    url = f"/produtos/{produto_id}/"
                else:
                    print(f"{nome}: ❌ NÃO TESTADO (Produto não criado)\n")
                    continue

            # Correção para evitar erro de índice
            dados_para_envio = data[0] if data and len(data) > 0 and isinstance(data[0], dict) else None

            passou, resposta = testar_endpoint(metodo, url, nota, dados_para_envio)
            status = "✅ PASSOU" if passou else "❌ FALHOU"
            if passou:
                total_pontos += nota

                # Captura IDs para dependências
                if nome == "Cadastrar cliente" and resposta and isinstance(resposta, dict):
                    cliente_id = resposta.get("id")
                elif nome == "Cadastrar produto" and resposta and isinstance(resposta, dict):
                    produto_id = resposta.get("id")
                elif nome == "Criar pedido" and resposta and isinstance(resposta, dict):
                    pedido_id = resposta.get("id")

            print(f"{nome}: {status} (+{nota} pontos)")

    print("\n=== Nota Final ===")
    print(f"Pontuação obtida: {total_pontos:.1f}/{total_maximo:.1f}")

if __name__ == "__main__":
    testar_api()
