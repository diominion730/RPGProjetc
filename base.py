#Chaves e valores iniciais obrigatorios
heroi = {'Nivel': 0, 'Xp': 0}
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
  try:
    classeOp = int(input("Qual sera a classe do seu heroi:")) #Permitir o usario digitar apenar 1 2 ou 3
    classeEscolhida = classe[f'Classe{classeOp}']
  except:
    print("Por favor, digite apenas as classes listadas!!!")
    
  print(f"Voce selecionou a classe {classeEscolhida['Nome']}") #Mudança para evitar repetição
  confirmacao = str.upper(input("\nDeseja confirmar? S/N")) #Permitir letras maiusculas e minusculas(precisa)
  if confirmacao == "S":
    #Vinicius: Atribuindo status diretamento ao dic "heroi"
    heroi['Classe'] = classeEscolhida['Nome']
    heroi['Força'] = classeEscolhida['Força']
    heroi['Defesa'] = classeEscolhida['Defesa']
    heroi['Vida'] = classeEscolhida['Vida']
    heroi['Mana'] = classeEscolhida['Mana']

    condicaoClasse = False

  else:
    if confirmacao == "N":
      continue
    else:
      print("Por favor, digite apenas 'S' ou 'N'")
   
print(heroi.items())
""
#print("----MENU PRINCIPAL-----" \ IDEIA DE MENU SIMPLES
#"1- Ver status" \
#"2- Inventario" \
#"3- Batalhar" \
#"4- Loja" \
#"5- Sair")
