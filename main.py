#imports de bibliotecas que irei utilizar
import os

#Comando print
print("Olá Mundo!")

#Variaveis // as variaveis em python não necessitam de identificação
nome = "Daniel"
idade = 18
altura = 1.80
#Variaveis booleana
BananaEAmarelo = True
BananaEVermelho = False
#Comparação(utilizando if/else) de variaveis com input e especificação de variavel
ingressos = int (input("Digite quantos ingressos tem a disposição:"))
compradores = int (input("Agora digite quantos compradores tem:"))
if ingressos >= compradores:
    print("Tem ingressos suficiente!")
else:
    print("Tem muitos compradores para poucos ingressos!")
print("_________________________________________________________")
#comparação usando if/elif/else
salario = int (input("Digite o seu salario sem casas decimais: "))
if salario < 3100:
    print("Dev Junior/Estagiario")
elif salario >= 3100 and salario < 5400:
    print("Dev pleno")
elif salario >= 5400 and salario < 15000:
    print("Dev senior")
else:
    print("Gerente de projetos")
print("_________________________________________________________")
#Listas e usando for para ver cada casa da lista
ListaNum = [1,2,3]
for x in range(len(ListaNum)):
    print(ListaNum[x])
print("_________________________________________________________")
#Adicionando mais dados dentro de uma lista(mais avançado)
ListNumTest = [6,5,4]
for y in range(len(ListaNum)):
    print("Os valores dentro da lista são:")
    print(ListaNum[y])
confirmacao = str(input("Você deseja acrescentar mais numeros a lista? s/n: "))
if confirmacao == "s":
    w = int(0)
    while w <= 3:
        if confirmacao == str("s"):
            NumADD = int(input("Digite um numero inteiro para adicionar a lista: "))
            ListNumTest.append(NumADD)
        confirmacao = str(input("Você deseja acrescentar mais numeros a lista? S/N: "))
        if confirmacao == str("n"):
            break
print(len(ListNumTest))
for z in range(len(ListNumTest)):
    print(ListNumTest[z])
print("_________________________________________________________")
#Dicionario no python
pessoa = {
    "nome":"Daniel",
    "idade":18,
    "altura":1.80
}
print(pessoa['nome'])
print(pessoa['idade'])
print(pessoa['altura'])
print("_________________________________________________________")
#Lista dentro de Lista
Player = {
    "Nickname":"ZIKI",
    "Level":"1",
    "Vida":"100",
    "XP":"0"
}
Mobs = [
    {"Nome":"Zumbie","Level":"1","Vida":"100", "Drop": {"Arma1":"Espada Longa","Arma2":"Machado Pesado"}},
    {"Nome":"Esqueleto","Level":"5","Vida":"150", "Drop": {"Arma1":"Arco","Arma2":"Besta"}}
]
#Fazendo um chat para 1 pessoa apenas com tudo que aprendi e utilizando a biblioteca (OS) do python
#para ajudar com algumas funcionalidades

mensagens = []

nome = input("Nome: ")

while True:
    #limpar o terminal
    os.system('cls')

    if len(mensagens) > 0:
        for m in mensagens:
            print(m['nome'], "-", m['texto'])
    print("_____________")
    #Obtendo texto
    texto = input("Mensagem: ")
    if texto == "fim":
        break
    #Adicionando mensagem na lista
    mensagens.append({
        "nome": nome,
        "texto": texto 
    })