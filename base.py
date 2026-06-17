heroi = {}
classe = {
    "Classe1": {
        'Nome:': 'Guerreiro', 
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
        'Nome': 'Arqueiro',
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

altura_heroi = float(input("Qual a altura do seu heroi?"))
heroi['Altura'] = altura_heroi

peso_heroi = float(input("Qual o peso do seu heroi?"))
heroi['Peso'] = peso_heroi

print("\n")

condicaoClasse = True
while condicaoClasse:
  print(
"Selecione sua classe:\n"
"1- Guerreiro\n"
"2- Mago\n"
"3- Arqueiro\n"
 )
  
  classeOp = int(input("Qual sera a classe do seu heroi:"))
    
  if classeOp == 1:
    print(f"Voce seleciounou a classe {classe['Classe1']}")
    confirmacao = input("\nDeseja confirmar? S/N") #Permitir letras maiusculas e minusculas 
    if confirmacao == "S" or confirmacao == "s" or confirmacao == "sim" or confirmacao == "Sim":
      heroi['Classe'] = classe['Classe1']
      condicaoClasse = False
    else:
      continue
    
  if classeOp == 2:
    print(f"Voce seleciounou a classe {classe['Classe2']}")
    confirmacao = input("\nDeseja confirmar? S/N") #Permitir letras maiusculas e minusculas sem precisar tratar no "OR"
    if confirmacao == "S" or confirmacao == "s" or confirmacao == "sim" or confirmacao == "Sim":
      heroi['Classe'] = classe['Classe2']
      condicaoClasse = False
    else:
      continue

  if classeOp == 3:
    print(f"Voce seleciounou a classe {classe['Classe3']}")
    confirmacao = input("\nDeseja confirmar? S/N") #Permitir letras maiusculas e minusculas 
    if confirmacao == "S" or confirmacao == "s" or confirmacao == "sim" or confirmacao == "Sim":
      heroi['Classe'] = classe['Classe3']
      condicaoClasse = False
    else:
      continue

    dasipufhdsuifdsfidsjiofoiasd