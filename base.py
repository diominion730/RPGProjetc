#CODIGO COM ERRO POIS N FOI ADICIONADO ARMA INICIAL NA CLASSE 1 E 2(acredito eu)


heroi = {'Nivel': 0, 'Xp': 0}

heroi['inventario'] = {  #Cria uma chave inventario, dentro dessa chave tera outro dicionario com as chaves: "armas" e "items" com valores sendo listas
#Assim da pra criar categorias dentro do inventario
  'armas': [],
  'items': []
} 

inimigo = {
  
}
"Uma lista, e cada elemento da lista é um dicionario"
classe = [
  {
  "Nome": "Guerreiro",
  "Força": 18,
  "Defesa": 16,
  "Vida": 150,
  "Mana": 30
  },
  {
  "Nome": "Mago",
  "Força": 6,
  "Defesa": 6,
  "Vida": 80,
  "Mana": 180,
  },
  {
  "Nome": "Arqueiro",
  "Força": 12,
  "Defesa": 10,
  "Vida": 100, 
  "Mana": 60,
  "arma inicial": "Cajado Quebrado"
  }
]

nome_heroi = str(input("Qual o nome do seu heroi?"))
heroi['Nome'] = nome_heroi 

condicaoClasse = True
while condicaoClasse:
  print(
  "\nSelecione sua classe:\n"
  f"1- {classe[0]['Nome']} \n"
  f"2- {classe[1]['Nome']} \n"
  f"3- {classe[2]['Nome']} \n"
  )
  try:
    classeOp = int(input("Qual sera a classe do seu heroi:"))
  except:
    print("Por favor, digite apenas as classes listadas!!!")
    
  print(f"Voce selecionou a classe {classe[classeOp - 1]['Nome']}") 
  confirmacao = str.upper(input("\nDeseja confirmar? S/N")) 
  if confirmacao == "S":
    #Vinicius: Atribuindo status diretamento ao dic "heroi"
    heroi['Classe'] = classe[classeOp - 1]['Nome']
    heroi['Força'] = classe[classeOp - 1]['Força']
    heroi['Defesa'] = classe[classeOp - 1]['Defesa']
    heroi['Vida'] = classe[classeOp - 1]['Vida']
    heroi['Mana'] = classe[classeOp - 1]['Mana']
    heroi['Vida'] = classe[classeOp - 1]['Vida']

    condicaoClasse = False

  else:
    if confirmacao == "N":
      continue
    else:
      print("Por favor, digite apenas 'S' ou 'N'")

<<<<<<< HEAD
heroi['inventario']['armas'].append(classe[classeOp - 1]['arma inicial']) #O código acessa o dicionário heroi, entra na chave inventario, depois acessa a chave armas dentro desse inventário e usa o método append() para adicionar a arma inicial da classe escolhida nessa lista.S
print(f"Parabéns!! Como presente de boas vindas voce ganhou um {classe[classeOp - 1]['arma inicial']}!")
verStatus = str.upper(input(f"Deseja ver os stats do item: {classe[classeOp - 1]['arma inicial']}? S/N"))
if verStatus == "S":  #pode quebrar aqui
=======
status = {"Armas": {"Cajado Quebrado": {"Dano": 28}}, "Items": {}}

heroi['inventario']['armas'].append(classeEscolhida['arma inicial']) #O código acessa o dicionário heroi, entra na chave inventario, depois acessa a chave armas dentro desse inventário e usa o método append() para adicionar a arma inicial da classe escolhida nessa lista.S
status.append(heroi['inventario']['armas'](classeEscolhida['arma inicial']))
print(f"Parabéns!! Como presente de boas vindas voce ganhou um {classeEscolhida['arma inicial']}!")
verStatus = str.upper(input(f"Deseja ver os stats do item: {classeEscolhida['arma inicial']}? S/N"))
if verStatus == "S":
>>>>>>> 305d40a6b281304fdcd9a292171c95904dfe88d3
  print("stats") #Precisa ser criado de algum jeito ai!

#1- Ideia em ordem sequencial com nivel se dificuldade na minha visão
#2- Arma inicial para outras classes (facil)
#3- Status para cada arma (facil/medio de estruturar)
#4- Dicionario para o inimigo com os mesmo stats do heroi (facil)
#5- Batalha simples de turno com algum inimigo(Apenas com ataque com dano fixo) versao inicial (facil/medio)
#6- Poder usar itens de cura durante a batalha (facil)
#7- Evoluir para dano baseado nos status de ataque (e arma do heroi pensando alto - faz parte da ideia 11) (dificil)
#8- Calcuar dano com base na defesa do inimigo (dificl)
#9- Dano crítico (medio)
#10- Chance de dropar itens/armar/armaduras ao derrotar monstros (medio)
#11- Atributos de dano para cada arma(Fisico ou magico dependendo da arma) (médio)
#


#print("----MENU PRINCIPAL-----" \ IDEIA DE MENU SIMPLES
#"1- Ver status" \
#"2- Inventario" \
#"3- Batalhar" \
#"4- Loja" \
#"5- Sair")
