# - [Sumário](#guia-para-uso-de-markdowns-para-github)
- [- Sumário](#ullisumárioliul)
- [Guia para uso de Markdowns para Github](#guia-para-uso-de-markdowns-para-github)
- [Cabeçalho 1](#cabeçalho-1)
  - [Cabeçalho 2](#cabeçalho-2)
    - [Cabeçalho 3](#cabeçalho-3)
      - [Cabeçalho 4](#cabeçalho-4)
        - [Cabeçalho 5](#cabeçalho-5)
          - [Cabeçalho 6](#cabeçalho-6)
  - [Enfase em textos](#enfase-em-textos)
    - [Negrito](#negrito)
    - [Itálico](#itálico)
    - [Riscado](#riscado)
    - [Linha horizontal](#linha-horizontal)
  - [Blocos de citação](#blocos-de-citação)
  - [Links](#links)
  - [Imagens](#imagens)
  - [Listas Não Ordenadas](#listas-não-ordenadas)
  - [Listas Ordenadas](#listas-ordenadas)
  - [Comentários de Códigos](#comentários-de-códigos)
    - [Uma linha de código em forma de comentário](#uma-linha-de-código-em-forma-de-comentário)
    - [Várias linhas de código em forma de comentário](#várias-linhas-de-código-em-forma-de-comentário)
      - [Html](#html)
      - [Bash](#bash)
      - [Prompt de Comando](#prompt-de-comando)
      - [Python](#python)
  - [Tabelas](#tabelas)
  - [Lista de Tarefas](#lista-de-tarefas)

# Guia para uso de Markdowns para Github

Para cabeçalhos, utilizamos `#` e a cada # adicionado representa um nível, indo de 1 a 6, seguindo exemplo abaixo:

# Cabeçalho 1 
## Cabeçalho 2 
### Cabeçalho 3 
#### Cabeçalho 4 
##### Cabeçalho 5 
###### Cabeçalho 6

## Enfase em textos

Para enfase em um texto, podemos utilizar algumas atribuições como: Negrito, Itálico, Riscado... entre outros, conforme exemplo abaixo:

### Negrito
<!-- Strong -->

Este é um texto em **negrito**. Para utilizar essa marcação é necessário utilizar a palavra entre asteriscos `**<texto_aqui>**`

### Itálico

Este é um texto em _itálico_. Para utilizar essa marcação é necessário utilizar a palavra entre underlines `_<texto_aqui>_`


### Riscado

Este é um texto em ~~itálico~~. Para utilizar essa marcação é necessário utilizar a palavra entre tiõs `~~<texto_aqui>~~`


### Linha horizontal

Se você deseja fazer uma linha horizontal para dividir conteúdos, você pode utilizar `---` ou `___` 

---
_**Texto entre as linhas**_
___

## Blocos de citação

Para criar blocos de citações é necessário utilizar o `>`

> Lorem ipsum, dolor sit amet consectetur adipisicing elit. Nemo laboriosam voluptatum nesciunt
perspiciatis itaque id adipisci a, dolores debitis eos? Error eligendi aspernatur ipsam
exercitationem quae temporibus nam asperiores.


>>  Lorem ipsum, dolor sit amet consectetur adipisicing elit. Nemo laboriosam voluptatum nesciunt
perspiciatis itaque id adipisci a, dolores debitis eos? Error eligendi aspernatur ipsam
exercitationem quae temporibus nam asperiores. Qui?

## Links

O texto que queremos utilizar para o link vai entre `[]` e o link vai entre `()` logo após o texto.

[Ricardo's Github](https://github.com/ricardo-cas)

Se você deseja adicionar um título par ao link que você está criando (para aparecer quando você posiciona o mouse no link), é só você dar um espaço após o `()` e adicionar o texto do título entre aspas `[Ricardo's Github](https://github.com/ricardo-cas "Título do link")`.

[Ricardo's Github](https://github.com/ricardo-cas "Pagina do GitHub do Ricardo")

## Imagens

A imagem deve estar depois de `![texto_legenda]` seguido por entre `()` com o link da imagem.

![imagem](https://source.unsplash.com/random/200x200)

## Listas Não Ordenadas

Para criação de listas não ordenadas é necessário colocar o asterisco `* Item` antes do item para criar a lista. Exemplo:

* Item 1
* Item 2
* Item 3

Se você deseja criar **_sub itens_** dentro da lista, é só realizar a identação na lista, conforme exemplo:

* Item 1
* Item 2
  * Sub item 1
    * Sub item 2
      * Sub item 3

## Listas Ordenadas

Para listas ordenadas, é necessário colocar os números `1. Item 1`  antes do item para criar a lista. Exemplo:

1. Item 1
2. Item 2
   1. Sub 1
   2. Sub 2
3. Item 3
   1. Sub 1
      a. Sub 1
      b. Sub 2

## Comentários de Códigos

### Uma linha de código em forma de comentário

Para colocar uma linha de códigos em forma comentários, é necessário utilizar  \`código` que o resultado será:

`<p> Este é um paragrafo em html</p>`

### Várias linhas de código em forma de comentário
Para colocar um bloco de códigos em forma comentários, é necessário utilizar  \```html
código```  e também é **_recomendado_** que você coloque a linguagem em que aquele bloco de código está escrito, para facilitar a marcação de palavras reservadas daquela linguagem.

#### Html
``` html
<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Página</title>
</head>
<body>
  
</body>
</html>
```

#### Bash
```bash
ls

pip install pandas

pip install --upgrade --user pandas

```

#### Prompt de Comando
```cmd
cd C:\\User\YourUser\Desktop

mkdir Folder
```

#### Python
```python
def hello():
    print('Hello World')

if __name__ == "__main__":
    hello()
```

## Tabelas

Para criar tabelas é necessário utilizar um formato específico para o Github, conforme bloco de códigos abaixo:

```bash
| Cabeçalho | Cabeçalho | Cabeçalho |
| --- | --- | --- |
| conteúdo | conteúdo | conteúdo |
| conteúdo | conteúdo | conteúdo |

```

| Nome | Tipo | Ataque |
| --- | --- | --- |
| Pikachu | Elétrico | 50 |
| Charmander | Fogo | 50 |

## Lista de Tarefas

Para fazer uma lista de tarefas é necessário utilizar um formato específico para o Github, conforme bloco de códigos abaixo:

```bash
*[x] Item completado
*[x] Item completado
*[ ] Item não completado
```


*[X] Criar arquivo guia para Readme no Github
*[x] Commit das mudanças
*[ ] Envio das mudanças para o repositório