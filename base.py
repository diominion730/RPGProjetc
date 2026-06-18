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
    try:                                                           # eu achei mais importante colocar o try aqui, já que é int, caso o usuário coloque qualquer outra coisa, ia dar erro e o código parava
        classeOp = int(input("Qual será a classe do seu heroi:"))
    except ValueError:
        print("Por favor, digite apenas os números das classes listadas :)")
        print()
        continue
    if classeOp == 1:                                             
        print(f"Voce seleciounou a classe {classe['Classe1']}") # aqui nem precisou do try
        confirmacao = str.upper(input("Digite 'S' para sim ou 'N' para não\nDeseja confirmar?: "))  # nunca ia dar dar erro aqui porque tá aceitando absolutamente tudo, por isso o try seria inviável aqui
        if confirmacao == "S":
            heroi['Classe'] = classe['Classe1']
            condicaoClasse = False
        else:                                                               
            if confirmacao == "N": # coloquei isso aqui porque caso colocasse apenas que fosse diferente do "S" eu não iria saber se o usuário digitou "N" ou algo aleatório
                continue
            else:
                print("Por favor, digite apenas 'S' ou 'N'") # aí por isso eu coloquei esse outro else, porque caso não for de fato o "N" e for coisas aleatórias, eu posso dar uma bronca no usuário e ele saber o que é para colocar mesmo ;)
                print()
                continue
      
    if classeOp == 2:
        print(f"Voce seleciounou a classe {classe['Classe2']}") 
        confirmacao = str.upper(input("Digite 'S' para sim ou 'N' para não\nDeseja confirmar?: "))  
        if confirmacao == "S":
            heroi['Classe'] = classe['Classe2']
            condicaoClasse = False
        else:                                                               
            if confirmacao == "N": 
                continue
            else:
                print("Por favor, digite apenas 'S' ou 'N'") 
                print()
                continue

    if classeOp == 3:
        print(f"Voce seleciounou a classe {classe['Classe3']}") 
        confirmacao = str.upper(input("Digite 'S' para sim ou 'N' para não\nDeseja confirmar?: "))  
        if confirmacao == "S":
            heroi['Classe'] = classe['Classe3']
            condicaoClasse = False
        else:                                                               
            if confirmacao == "N": 
                continue
            else:
                print("Por favor, digite apenas 'S' ou 'N'") 
                print()
                continue

print(heroi) #TEST
