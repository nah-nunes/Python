## Manipulando arquivos 
  - ### Abrindo e fechando arquivos: 

Para abrir arquivos em Python pode-se usar a função open(), que aceita dois argumentos: o caminho do arquivo e o modo de abertura(leitura, escrita, etc).
- r - read/leitura
- a - Append/incrementar
- w - Writing/ escrita
- x - criar arquivo
- r+ - Leitura + escrita
Depois de trabalhar com o arquivo, é uma prática recomendada fechá-lo utilizando o método close().

  - ### Remover arquivos
  Para remover os arquivos, é necessário importar o módulo 'os' ou 'os.path', que fornecem uma função chamada 'remove()' que permite excluir arquivos. 

```python
import os

# Especifica o caminho do arquivo a ser removido
caminho_arquivo = "arquivo_a_remover.txt"

try:
    # Remove o arquivo
    os.remove(caminho_arquivo)
    print(f"O arquivo '{caminho_arquivo}' foi removido com sucesso.")
except FileNotFoundError:
    print(f"O arquivo '{caminho_arquivo}' não foi encontrado.")
except PermissionError:
    print(f"Permissão negada para remover o arquivo '{caminho_arquivo}'.")
except Exception as e:
    print(f"Ocorreu um erro ao tentar remover o arquivo '{caminho_arquivo}': {e}")

```
- Removendo uma pasta 

```python

os.rmdir("Aula12/nova_pasta")

```