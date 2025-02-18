## Exercício para Consolidar conteúdo em LTP1

**1. Correção de Código e Compreensão**

a) Analise o seguinte código Python que tenta calcular a média de uma lista de números:

```python
numeros = [10, 20, 30, 40]
soma = 0
for i in range(1, len(numeros) + 1):
    soma += numeros[i]
media = soma / len(numeros)
print("A média é:", media)
```

- Identifique o erro presente no código e corrija-o.

b) Após a correção, qual será a saída do programa?

**2. Estruturas Condicionais e Looping**

a) Escreva um programa em Python que solicite ao usuário um número inteiro positivo e exiba todos os números pares de 0 até esse número (inclusive).

b) Explique a diferença entre o loop `for` e o loop `while` em Python, fornecendo um exemplo de quando seria mais apropriado usar cada um.

**3. Dicionários em Python**

a) Crie um dicionário em Python que armazene os nomes de cinco cidades como chaves e suas respectivas populações como valores. Em seguida, escreva um código que exiba o nome da cidade com a maior população.

b) Como você pode verificar se uma determinada chave existe em um dicionário? Forneça um exemplo de código para ilustrar sua resposta.

**4. Manipulação de Dicionários**

Considere o seguinte dicionário que armazena informações sobre alunos e suas notas:

```python
alunos = {
    "Ana": [8.5, 7.0, 9.5],
    "Bruno": [5.5, 6.0, 7.0],
    "Carla": [9.0, 8.0, 10.0]
}
```
a) Escreva um código que calcule a média de notas de cada aluno e armazene essas médias em um novo dicionário chamado `medias`.

b) Como você poderia adicionar um novo aluno, "Daniel", com as notas [7.5, 8.0, 8.5] ao dicionário `alunos`?


**5. Funções em Python**

a) Escreva uma função chamada `soma_lista` que receba uma lista de números como parâmetro e retorne a soma desses números.

Essas questões abrangem uma variedade de tópicos relevantes e devem proporcionar uma prática abrangente para os estudantes.


**6. Classes e Objetos**

a) Crie uma classe chamada `Pessoa` que possua os atributos `nome`, `idade` e `profissao`. Implemente um método que exiba essas informações em uma única linha.

b) Instancie três objetos da classe `Pessoa` com diferentes valores e chame o método para exibir as informações de cada um.

**7. Herança**

a) Implemente uma classe base chamada `Veiculo` com atributos `marca` e `modelo`, e um método `informacoes` que exiba esses dados.

b) Crie uma classe derivada chamada `Carro` que herde de `Veiculo` e adicione o atributo `numero_portas`. Sobrescreva o método `informacoes` para incluir o número de portas.

c) Instancie um objeto da classe `Carro` e chame o método `informacoes`.


**8. Compreensão de API REST**

a) Explique o que é o método HTTP PATCH e como ele difere do método PUT em uma API REST.

b) Em uma API RESTful, qual código de status HTTP geralmente indica que uma requisição foi bem-sucedida e resultou na criação de um novo recurso?


**9. Django Rest Framework: Serializers**

Considere o seguinte modelo Django representando um Produto:

```python
from django.db import models

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    estoque = models.IntegerField()
```

a) Crie um serializer para o modelo `Produto` usando o Django Rest Framework.

b) Como você pode modificar o serializer para garantir que o campo `preco` seja sempre positivo?

**10. Relacionamentos em Django**

Suponha que você tenha os seguintes modelos Django para `Autor` e `Livro`:

```python
from django.db import models

class Autor(models.Model):
    nome = models.CharField(max_length=100)

class Livro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
```

a) Explique o tipo de relacionamento entre `Autor` e `Livro`.

b) Como você poderia modificar os modelos para que um livro possa ter múltiplos autores e um autor possa ter escrito múltiplos livros?


**11. Criação de Endpoints no Django Rest Framework**

Suponha que você tenha um modelo `Categoria` e deseja criar um endpoint que liste todas as categorias e permita a criação de novas categorias.

a) Qual classe genérica de view do Django Rest Framework você utilizaria para esse propósito?

b) Como você configuraria as URLs para esse endpoint?
