# **Tutorial: Relacionamentos entre Modelos no Django**

## **1. Introdução aos Relacionamentos**

Na modelagem de banco de dados, relacionamentos ajudam a conectar diferentes tabelas. No Django, isso é feito entre modelos para organizar os dados e facilitar o trabalho com informações relacionadas.

### Tipos de Relacionamentos:
1. **One-to-One**: Um registro de um modelo está ligado a um único registro de outro modelo.
2. **Many-to-One**: Vários registros de um modelo podem estar ligados a um único registro de outro modelo.
3. **Many-to-Many**: Muitos registros de um modelo podem estar ligados a muitos registros de outro modelo.

---

## **2. Relacionamento One-to-One**

### Quando usar:
- Quando cada item em um modelo só pode estar ligado a um único item em outro modelo.

### Exemplo:
Vamos criar dois modelos: **Author** (autor) e **Profile** (perfil), onde cada autor tem um único perfil.

```python
from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Profile(models.Model):
    author = models.OneToOneField(Author, on_delete=models.CASCADE)
    bio = models.TextField()
    website = models.URLField()

    def __str__(self):
        return f"Profile of {self.author.name}"
```

### Explicação:
- `OneToOneField`: Cria um vínculo de 1 para 1 entre os modelos.
- `on_delete=models.CASCADE`: Apaga o perfil se o autor for deletado.

---

## **3. Relacionamento Many-to-One**

### Quando usar:
- Quando muitos itens em um modelo estão relacionados a um único item em outro modelo.

### Exemplo:
Vamos criar dois modelos: **Book** (livro) e **Publisher** (editora), onde vários livros podem ser publicados por uma única editora.

```python
class Publisher(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=255)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} by {self.publisher.name}"
```

### Explicação:
- `ForeignKey`: Cria um vínculo de muitos para um.
- `on_delete=models.CASCADE`: Apaga todos os livros se a editora for deletada.

---

## **4. Relacionamento Many-to-Many**

### Quando usar:
- Quando muitos itens em um modelo podem estar relacionados a muitos itens em outro modelo.

### Exemplo:
Vamos criar dois modelos: **Book** (livro) e **Category** (categoria), onde um livro pode pertencer a várias categorias e uma categoria pode incluir vários livros.

```python
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=255)
    categories = models.ManyToManyField(Category)

    def __str__(self):
        return self.title
```

### Explicação:
- `ManyToManyField`: Cria um vínculo de muitos para muitos.
- O Django cria automaticamente uma tabela intermediária para gerenciar os relacionamentos.

---

## **5. Trabalhando com Relacionamentos no Shell**

### Criando Objetos:
1. Crie um autor e um perfil:
   ```python
   author = Author.objects.create(name="J.K. Rowling")
   profile = Profile.objects.create(author=author, bio="Author of Harry Potter", website="https://example.com")
   ```

2. Crie uma editora e livros:
   ```python
   publisher = Publisher.objects.create(name="Penguin Books")
   book1 = Book.objects.create(title="1984", publisher=publisher)
   book2 = Book.objects.create(title="Animal Farm", publisher=publisher)
   ```

3. Crie categorias e vincule a livros:
   ```python
   category1 = Category.objects.create(name="Fiction")
   category2 = Category.objects.create(name="Classic")
   book1.categories.add(category1, category2)
   book2.categories.add(category2)
   ```

---

## **6. Dicas Importantes**

- Use `related_name` no campo de relacionamento para personalizar como acessar os objetos relacionados.
- Use `prefetch_related` e `select_related` para melhorar a performance ao trabalhar com relacionamentos.

---

## **7. Desafio para Prática**

Crie um sistema onde:
- Um modelo **Student** está relacionado a **Classroom** (Many-to-One).
- Um modelo **Teacher** está relacionado a **Classroom** (One-to-One).
- Um modelo **Classroom** pode ter várias **Subjects** (Many-to-Many).

---