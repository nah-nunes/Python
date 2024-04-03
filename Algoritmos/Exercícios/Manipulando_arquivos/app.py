# Abrindo o arquivo para leitura
arquivo = open("Aula12/test.txt","r")
# função que verifica se o arquivo pode ser lido
print(arquivo.readable())
#retorna todo o arquivo
print(arquivo.read())
# le a primeira linha do arquivo
print(arquivo.readline())
# transforma em uma lista
list = arquivo.readlines()
print(list)
#print(list[3])

arquivo.close()
# a - adicionar mais coisas num arquivo já existente
# w - apaga tudo e escreve outro

arquivo = open("Manipulando_arquivos/test.txt","a")
arquivo.write("C\n")

#arquivo2 = open("Aula12/test2.txt", "w")


#arquivo2.close()


arquivo.close()


import os
if os.path.exists("Manipulando_arquivos/test.txt"):
  os.remove("Manipulando_arquivos/test.txt")
else:
  print("O arquivo não existe")