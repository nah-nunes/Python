### Algoritmos e Estruturas de Dados com Python 


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

**if, elif, else**
As estruturas condicionais permitem que o programa execute diferentes blocos de código com base em condições específicas.
```python
if condição1:
    # Verifica se uma condição é verdadeira e executa um bloco de código se ela for
elif condição2:
    # Permite verificar múltiplas condições em sequência
else:
    # Executa um bloco de código se nenhuma das condições anteriores for verdadeira
#exemplo:
idade = 20
if idade < 18:
    print("Menor de idade")
elif idade >= 18 and idade < 65:
    print("Adulto")
else:
    print("Idoso")

```

**LOOPS**
**for**
Itera sobre os elementos de uma sequência.
```python
for elemento in sequência:
    # Bloco de código executado para cada elemento na sequência
for i in range(5):
    print(i)
```
**while**
Executa um bloco de código enquanto uma condição específica for verdadeira.
```python
while condição:
  # Bloco de código executado enquanto a condição for verdadeira
x = 0
while x < 5:
    print(x)
    x += 1
#break: Interrompe imediatamente a execução do loop e sai dele.
#continue: Pula o restante do código no loop e vai para a próxima iteração.

```

**Coleções**
   - **set** 
é uma estrutura de dados que armazena itens únicos e não ordenados. Isso significa que não pode conter elementos duplicados e não mantém a ordem em que os elementos foram inseridos. São muito úteis quando vc precisa armazenar uma coleção de itens onde a ordem não importa e cada item é único.  
- Itens únicos
- Não ordenado
- mutável (adicionar ou remover elementos)
Pode-se criar um set utilizando chaves {} ou a função set()

```python

frutas ={"maçã", "laranja", "abacaxi"}
frutas.add("Pera")
frutas.remove("maçã")
frutas.pop()
for fruta in frutas:
    print(fruta)
```
    - **Dictionary**

Estrutura de dados que mapeia chaves e valores. É uma coleção mutável e indexada de itens, onde cada item é uma associação de uma chave única a um valor. 
- chaves únicas
- não ordenado
- mutável
Cria-se um dicionário utilizando {} e especificando os pares chave-valor, separados por vírgula. 

```python
meses ={
    "jan":"Janeiro",
    "fev":"Fevereiro",
    "mar":"Março",
    "apr":"Abril",
    "may":"Maio",
    "jun":"Junho",
    "jul":"Julho",
    "aug":"Agosto",
}
print(meses.get("abc", "Valor Padrão"))# invalido
print(meses.get["Abc"])# quebra
print(len(meses)) #retorna o tamanho da estrutura de dados
```
### Tratando exceções 
Lidando com erros ou condições excepcionais que podem ocorrer durante a execução de um programa. Isso evita que o programa pare abruptamente e fornece uma maneira de lidar com essas situações de forma controlada. O tratamento de exceções é feito usando blocos 'try', 'except', 'else' e 'finally'.

**Bloco try e except**
O código que pode gerar uma exceção é colocado dentro de um bloco 'try'. Se uma exceção ocorre o controle é transferido para o bloco 'except' que contém o código para lidar com a exceção. 
```python
try:
    # Código que pode gerar uma exceção
    resultado = 10 / 0
except ZeroDivisionError:
    # Lidando com a exceção ZeroDivisionError
    print("Divisão por zero não é permitida.")
```

**Bloco else**
é executado se nenhum erro ocorrer dentro do bloco try. Isso é útil para executar código que deve ser executado somente se nenhuma exceção ocorrer. 
```python
try:
    resultado = 10 / 2
except ZeroDivisionError:
    print("Divisão por zero não é permitida.")
else:
    print("O resultado da divisão é:", resultado)

```

**Bloco finally**
é opcional e sempre executado, independentemente de ocorrer uma exceção ou não. 
Util para ações de limpeza, como fechar arquivos ou conexões de banco de dados, que devem ser conectadas independentemente de ocorrerem erros. 
```python
try:
    arquivo = open("arquivo.txt", "r")
    # Operações de leitura/gravação no arquivo
except FileNotFoundError:
    print("O arquivo não foi encontrado.")
finally:
    arquivo.close()  # Garante que o arquivo seja fechado, mesmo se ocorrer uma exceção
```
**Capturando exceções genéricas**
Pode-se também capturar exceções genéricas para lidar com qualquer tipo de exceção que ocorra. 

```python
try:
    # Código que pode gerar uma exceção
    resultado = 10 / 0
except Exception as e:
    # Lidando com qualquer exceção que ocorra
    print("Ocorreu uma exceção:", e)

```