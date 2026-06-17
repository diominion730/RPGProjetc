heroi = {}
classe = {"Classe1": "Guerreiro", "Classe2": "Mago", "Classe3": "Arqueiro"} #Adicionar um dicionario dentro de cada classe com seus respectivos atributos

#Criação de personagem
#Nome do heroi
nome_heroi = str(input("Qual o nome do seu heroi?"))
heroi['Nome'] = nome_heroi 

altura_heroi = float(input("Qual a altura do seu heroi?"))
heroi['Altura'] = altura_heroi

peso_heroi = float(input("Qual o peso do seu heroi?"))
heroi['Peso'] = peso_heroi

print("\n")

print(
"Selecione sua classe:"
"1- Guerreiro"
"2- Mago"
"3- Arqueiro"
)

classeOp = str(input("Qual sera a classe do seu heroi"))
if classeOp == 3:
  print(f"Voce seleciounou a classe{classe['Classe3']}")
  
  confirmacao = input("\nDeseja confirmar? S/N") #Permitir letras maiusculas e minusculas 
  if confirmacao == "S" or "s" or "sim" or "Sim": #Precisa de outra logica ou algum metodo/função
    heroi['Heroi'] = classe['Classe3']
  #else
    #Precisa mudar a lógica e fazer com que pergunte ate o usuario selecionar uma classe

print(heroi.items())

#Poralgum motivo nao cai no If classeOp == 3

