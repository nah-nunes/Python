### Algoritmos e Estruturas de Dados com Python 
https://docs.google.com/document/u/7/d/e/2PACX-1vQMHEmdOg_3TTLcsxUwB2he57ycYN-fw8RupPX-GcV4c0hOTu46vxbKouzf6HcqUIHQ_8JbPpW2lBmb/pub

### Estudos

  [Variáveis](#variavel)<br>
  [Tipos de Dados ](#dados)<br>
  [Operadores](#operadores)<br>
  [Estruturas de Controle](#controle)<br>
  [Funções](#funcoes)<br>
 






<hr>

 ### Variáveis 
 São usadas para armazenar dados e podem conter diferentes tipos de valores.

 ```python
  x= 5 # é uma variável do tipo inteiro (int)
  nome = "João" # nome é uma variável do tipo string (str)
  lista = [1, 2, 3]  # lista é uma variável do tipo lista (list)

 ```
### Tipos de Dados 

Python possui vários tipos de dados embutidos, incluindo:
<ul>
<li> Inteiro(int): Números inteiros, como 5,-3, 100. 
<li> Float(float): Números de ponto flutuante, como 3.14, -0,0001, 2.0.
<li>String(str): Sequência de caracteres, como "Olá mundo!", "Python é bom"
<li>Lista(list): Sequência mutável de elementos, como [1,2,3], ["a","b","c"]
<li>Tupla (tuple): Sequência imutável de elementos, como (1, 2, 3), ("a", "b", "c").
<li> Dicionário (dict): Coleção de pares chave-valor, como {"nome": "João", "idade": 25}
<li>Booleano (bool): Valores verdadeiro (True) ou falso (False).

### Operadores

**Operadores aritméticos**

Adição (+): Realiza a adição de dois valores.
Subtração (-): Subtrai o segundo valor do primeiro.
Multiplicação (*): Multiplica dois valores.
Divisão (/): Divide o primeiro valor pelo segundo, retornando um resultado de ponto flutuante.
Divisão Inteira (//): Divide o primeiro valor pelo segundo e retorna um resultado inteiro, truncando qualquer parte decimal.
Módulo (%): Retorna o resto da divisão do primeiro valor pelo segundo.
Exponenciação ():** Eleva o primeiro valor à potência do segundo.

```python
a = 10
b = 3
print(a + b)  # Saída: 13
print(a - b)  # Saída: 7
print(a * b)  # Saída: 30
print(a / b)  # Saída: 3.3333333333333335
print(a // b) # Saída: 3
print(a % b)  # Saída: 1
print(a ** b) # Saída: 1000
```

**Operadores de comparação**

Igual a (==): Verifica se dois valores são iguais.
Diferente de (!=): Verifica se dois valores são diferentes.
Maior que (>): Verifica se o primeiro valor é maior que o segundo.
Menor que (<): Verifica se o primeiro valor é menor que o segundo.
Maior ou igual (>=): Verifica se o primeiro valor é maior ou igual ao segundo.
Menor ou igual (<=): Verifica se o primeiro valor é menor ou igual ao segundo.

```python
x = 5
y = 10
print(x == y)  # Saída: False
print(x != y)  # Saída: True
print(x > y)   # Saída: False
print(x < y)   # Saída: True
print(x >= y)  # Saída: False
print(x <= y)  # Saída: True

```
**Operadores Lógicos**
E (and): Retorna True se ambas as condições forem verdadeiras.
OU (or): Retorna True se pelo menos uma das condições for verdadeira.
NÃO (not): Inverte o resultado da expressão.
```python
a = True
b = False
print(a and b)  # Saída: False
print(a or b)   # Saída: True
print(not a)    # Saída: False
```
### Estruturas de controle 