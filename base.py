heroi = {}
classe = {
    "Classe1": {
        'Nome': 'Guerreiro', 
        "Força": 18,
        "Defesa": 16,
        "Vida": 150,
        "Mana": 30
    },
    "Classe2":{
        'Nome': 'Mago',
        "Força": 6,
        "Defesa": 8,
        "Vida": 80,
        "Mana": 180
        },
    "Classe3":{
        "Nome": "Arqueiro",
        "Força": 12,
        "Defesa": 10,
        "Vida": 100,
        "Mana": 60
          }} 

#Criação de personagem
#Nome do heroi
nome_heroi = str(input("Qual o nome do seu heroi?"))
heroi['Nome'] = nome_heroi 

condicaoClasse = True
while condicaoClasse:
  print(
"Selecione sua classe:\n"
#Vinicius: Modifiquei colocando os nomes diretamente dos valores da lista
f"1- {(classe['Classe1']['Nome'])} \n"
f"2- {(classe['Classe2']['Nome'])} \n"
f"3- {(classe['Classe3']['Nome'])} \n"
 )
  
  classeOp = int(input("Qual sera a classe do seu heroi:"))
    
  if classeOp == 1:
    #Vinicius: Arrumei a linha de baixo pq nao estava dando pra testar o resto do código
    print(f"Voce selecionou a classe {classe['Classe1']['Nome']}") #ERRO
    confirmacao = input("\nDeseja confirmar? S/N") #Permitir letras maiusculas e minusculas 
    if confirmacao == "S" or confirmacao == "s" or confirmacao == "sim" or confirmacao == "Sim":
      #Vinicius: Atribuindo status diretamento ao dic "heroi"
      heroi['Classe'] = classe['Classe1']['Nome']
      heroi['Força'] = classe['Classe1']['Força']
      heroi['Defesa'] = classe['Classe1']['Defesa']
      heroi['Vida'] = classe['Classe1']['Vida']
      heroi['Mana'] = classe['Classe1']['Mana']

      condicaoClasse = False
    else:
      continue
    
  if classeOp == 2:
    #Vinicius: Arrumei a linha de baixo pq nao estava dando pra testar o resto do código
    print(f"Voce selecionou a classe {classe['Classe2']['Nome']}") #LOGICA ERRADA
    confirmacao = input("\nDeseja confirmar? S/N") #Permitir letras maiusculas e minusculas sem precisar tratar no "OR"
    if confirmacao == "S" or confirmacao == "s" or confirmacao == "sim" or confirmacao == "Sim":
      #Vinicius: Atribuindo status diretamento ao dic "heroi"
      heroi['Classe'] = classe['Classe2']['Nome']
      heroi['Força'] = classe['Classe2']['Força']
      heroi['Defesa'] = classe['Classe2']['Defesa']
      heroi['Vida'] = classe['Classe2']['Vida']
      heroi['Mana'] = classe['Classe2']['Mana ']
      condicaoClasse = False
    else:
      continue

  if classeOp == 3:
    #Vinicius: Arrumei a linha de baixo pq nao estava dando pra testar o resto do código
    print(f"Voce selecionou a classe {classe['Classe3']['Nome']}")
    confirmacao = input("\nDeseja confirmar? S/N") #Permitir letras maiusculas e minusculas 
    if confirmacao == "S" or confirmacao == "s" or confirmacao == "sim" or confirmacao == "Sim":
      #Vinicius: Inves de colocar a Dic "classe" dentro do diciniorio heroi, copio os atributos para a o Dic "heroi"
      heroi['Classe'] = classe['Classe3']['Nome']
      heroi['Força'] = classe['Classe3']['Força']
      heroi['Defesa'] = classe['Classe3']['Defesa']
      heroi['Vida'] = classe['Classe3']['Vida']
      heroi['Mana'] = classe['Classe3']['Mana']
      condicaoClasse = False
    else:
      continue

print(heroi.items())


#print("----MENU PRINCIPAL-----" \ IDEIA DE MENU SIMPLES
#"1- Ver status" \
#"2- Inventario" \
#"3- Batalhar" \
#"4- Loja" \
#"5- Sair")
