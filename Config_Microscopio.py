print("Sistema para controle e configuração de um Aparelho de Microscopia. Esse sistema tem como objetivo auxiliar o pesquisador na contagem de celulas.")

autorExperimento = "Exemplo-1"
iluminação = 0
filtro = "Exemplo-1"
foco = 50
objetiva  = 2
campo = 1
tipoCelula = "Neurônios Unipolares"
resolucaoImagens = 960
qtd_frames = 30
ligarMicroscopio = 0

autorExperimentoInput = input("Qual o nome do autor do Projeto:")
print(f"Houve alteração no nome do autor? {autorExperimentoInput != autorExperimento}.")

print("\n" + "\n" + f"Bem vindo a mais um experimento senhor(a) {autorExperimentoInput}.")

print("\n" + "Por favor configure o Aparelho:" + "\n")

iluminaçãoInput = input("Qual a intensideda da iluminação de 0 a 100:")
print(f"Houve alteração na variável inserida? {int(iluminaçãoInput) != iluminação}. A iluminação está na intensidade:", iluminaçãoInput)

filtroInput = input("\n" +"Qual o tipo de filtro: (Defina o canal R, G ou B)")
print(f"Houve alteração na variável inserida? {filtroInput != filtro}. O filtro escolhido foi no canal:", filtroInput)

focoInput = input("\n" +"Qual a distancia do foco:")
print(f"Houve alteração na variável inserida? {int(focoInput) != foco}. Distancia do foco:", focoInput)

objetivaInput = input("\n" +"Qual a objetiva: (2x, 4x, 16x, 32x, 64x)")
print(f"Houve alteração na variável inserida? {int(objetivaInput) != objetiva}. Objetiva:", objetivaInput)

campoInput = input("\n" +"Defina o campo: (1 - Claro ou 0 - Escuro)")
print(f"Houve alteração na variável inserida? {int(campoInput) != campo}. Campo:", campoInput)

tipoCelulaInput = input("\n" +"Determine o tipo de celular:")
print(f"Houve alteração na variável inserida? {tipoCelulaInput != tipoCelula}. O projeto será a partir de imagens da celula:", tipoCelulaInput)

resolucaoImagensInput = input("\n" +"Qual a resolução desejada: (720p, 960p ou 1080p)")
print(f"Houve alteração na variável inserida? {int(resolucaoImagensInput) != resolucaoImagens}. A resolução da imagem possui:", resolucaoImagensInput)

qtd_framesInput = input("\n" +"Defina quantas imagens serão utilizadas para montar o masaico:")
print(f"Houve alteração na variável inserida? {int(qtd_framesInput) != qtd_frames}. O mosaico da imagem possuira {qtd_framesInput} quantidade de celular")

ligarMicroscopio = int(input("\n" +"Quer ligar o microscopio: (1 = ligar, 0 = desligar)"))
if(ligarMicroscopio == 1):
  print("O microscopio estava desligado.")
  print("Espere 10 min. O microscopio está ligando.")
elif(ligarMicroscopio == 0):
  print("O Microscopio já está desligado.")
else:
  print("Que maquina é essa que tem esse terceito botão?")


print("\n" + "As informações de configurações setadas pelo usuário são:")

print("\n" + "Autor:" + autorExperimentoInput)
print("\n" + "iluminação:" + iluminaçãoInput)
print("\n" + "filtro:" + filtroInput)
print("\n" + "foco:" + focoInput)
print("\n" + "objetiva:" + objetivaInput)
print("\n" + "campo:" + campoInput)
print("\n" + "tipoCelula:" + tipoCelulaInput)
print("\n" + "resolucaoImagens:" + resolucaoImagensInput)
print("\n" + "qtd_frames:" + qtd_framesInput)
print("\n" + "Status do Microscopio:" + str(ligarMicroscopio))

print("Use a primeira e a ultima letra do seu nome para calibrar o equipamento no eixo horizontal:")
print("Digite  à primeira letra do seu nome 10x e à última letra do seu nome 10x.")

v1 = input("Qual a primeira letra do seu nome? ")
f1 = input("Qual a ultima letra do seu nome? ")

cont = 1
prime = input(f"primeira letra - repetição {cont}:")
print("O Valor está correto:", v1 == prime)
print("O caracter precionado foi:", prime)

cont += 1
prime = input(f"primeira letra - repetição {cont}:")
print("O Valor está correto:", v1 == prime)
print("O caracter precionado foi:", prime)

cont += 1
prime = input(f"primeira letra - repetição {cont}:")
print("O Valor está correto:", v1 == prime)
print("O caracter precionado foi:", prime)

cont += 1
prime = input(f"primeira letra - repetição {cont}:")
print("O Valor está correto:", v1 == prime)
print("O caracter precionado foi:", prime)

cont += 1
prime = input(f"primeira letra - repetição {cont}:")
print("O Valor está correto:", v1 == prime)
print("O caracter precionado foi:", prime)

cont += 1
prime = input(f"primeira letra - repetição {cont}:")
print("O Valor está correto:", v1 == prime)
print("O caracter precionado foi:", prime)

cont += 1
prime = input(f"primeira letra - repetição {cont}:")
print("O Valor está correto:", v1 == prime)
print("O caracter precionado foi:", prime)

cont += 1
prime = input(f"primeira letra - repetição {cont}:")
print("O Valor está correto:", v1 == prime)
print("O caracter precionado foi:", prime)

cont += 1
prime = input(f"primeira letra - repetição {cont}:")
print("O Valor está correto:", v1 == prime)
print("O caracter precionado foi:", prime)



cont = 1
ult = input("\n" + "\n" + f"Ultima letra - repetição {cont}:")
print("O Valor está correto:", f1 == ult)
print("O caracter precionado foi:", ult)

cont += 1
ult = input(f"Ultima letra - repetição {cont}:")
print("O Valor está correto:", f1 == ult)
print("O caracter precionado foi:", ult)

cont += 1
ult = input(f"Ultima letra - repetição {cont}:")
print("O Valor está correto:", f1 == ult)
print("O caracter precionado foi:", ult)

cont += 1
ult = input(f"Ultima letra - repetição {cont}:")
print("O Valor está correto:", f1 == ult)
print("O caracter precionado foi:", ult)

cont += 1
ult = input(f"Ultima letra - repetição {cont}:")
print("O Valor está correto:", f1 == ult)
print("O caracter precionado foi:", ult)

cont += 1
ult = input(f"Ultima letra - repetição {cont}:")
print("O Valor está correto:", f1 == ult)
print("O caracter precionado foi:", ult)

cont += 1
ult = input(f"Ultima letra - repetição {cont}:")
print("O Valor está correto:", f1 == ult)
print("O caracter precionado foi:", ult)

cont += 1
ult = input(f"Ultima letra - repetição {cont}:")
print("O Valor está correto:", f1 == ult)
print("O caracter precionado foi:", ult)

cont += 1
ult = input(f"Ultima letra - repetição {cont}:")
print("O Valor está correto:", f1 == ult)
print("O caracter precionado foi:", ult)

cont += 1
ult = input(f"Ultima letra - repetição {cont}:")
print("O Valor está correto:", f1 == ult)
print("O caracter precionado foi:", ult)

print("\n" + "\n" + "Fim da caliração Horaizontal.")

print("Use à segunda letra do seu nome 10x e à penúltima letra do seu nome 10x calibrar o equipamento no eixo horizontal:")

v1 = input("Qual a segunda letra do seu nome? ")
f1 = input("Qual a penúltima letra do seu nome? ")

cont = 1
prime = input(f"segunda letra - repetição {cont}:")
print("O Valor está correto:", v1 == prime)
print("O caracter precionado foi:", prime)

cont += 1
prime = input(f"segunda letra - repetição {cont}:")
print("O Valor está correto:", v1 == prime)
print("O caracter precionado foi:", prime)

cont += 1
prime = input(f"segunda letra - repetição {cont}:")
print("O Valor está correto:", v1 == prime)
print("O caracter precionado foi:", prime)

cont += 1
prime = input(f"segunda letra - repetição {cont}:")
print("O Valor está correto:", v1 == prime)
print("O caracter precionado foi:", prime)

cont += 1
prime = input(f"segunda letra - repetição {cont}:")
print("O Valor está correto:", v1 == prime)
print("O caracter precionado foi:", prime)

cont += 1
prime = input(f"segunda letra - repetição {cont}:")
print("O Valor está correto:", v1 == prime)
print("O caracter precionado foi:", prime)

cont += 1
prime = input(f"segunda letra - repetição {cont}:")
print("O Valor está correto:", v1 == prime)
print("O caracter precionado foi:", prime)

cont += 1
prime = input(f"segunda letra - repetição {cont}:")
print("O Valor está correto:", v1 == prime)
print("O caracter precionado foi:", prime)

cont += 1
prime = input(f"segunda letra - repetição {cont}:")
print("O Valor está correto:", v1 == prime)
print("O caracter precionado foi:", prime)


cont = 1
ult = input("\n" + "\n" + f"penúltima letra - repetição {cont}:")
print("O Valor está correto:", f1 == ult)
print("O caracter precionado foi:", ult)

cont += 1
ult = input(f"penúltima letra - repetição {cont}:")
print("O Valor está correto:", f1 == ult)
print("O caracter precionado foi:", ult)

cont += 1
ult = input(f"penúltima letra - repetição {cont}:")
print("O Valor está correto:", f1 == ult)
print("O caracter precionado foi:", ult)

cont += 1
ult = input(f"penúltima letra - repetição {cont}:")
print("O Valor está correto:", f1 == ult)
print("O caracter precionado foi:", ult)

cont += 1
ult = input(f"penúltima letra - repetição {cont}:")
print("O Valor está correto:", f1 == ult)
print("O caracter precionado foi:", ult)

cont += 1
ult = input(f"penúltima letra - repetição {cont}:")
print("O Valor está correto:", f1 == ult)
print("O caracter precionado foi:", ult)

cont += 1
ult = input(f"penúltima letra - repetição {cont}:")
print("O Valor está correto:", f1 == ult)
print("O caracter precionado foi:", ult)

cont += 1
ult = input(f"penúltima letra - repetição {cont}:")
print("O Valor está correto:", f1 == ult)
print("O caracter precionado foi:", ult)

cont += 1
ult = input(f"penúltima letra - repetição {cont}:")
print("O Valor está correto:", f1 == ult)
print("O caracter precionado foi:", ult)

cont += 1
ult = input(f"penúltima letra - repetição {cont}:")
print("O Valor está correto:", f1 == ult)
print("O caracter precionado foi:", ult)

print("\n" + "\n" + "Fim da caliração Vertical.")
