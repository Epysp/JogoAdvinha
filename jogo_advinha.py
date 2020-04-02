import os
import time
from random import randint as r
from termcolor import colored

os.system("clear")


print("###Criador : D3pl0yzz Epysp \n###Contato: (82)981690602\n")

#usuario 

nome = input(colored("Digite Seu Nome : \n",'green'))

time.sleep(2)

print()

print("Maquina : Eu Irei Pensar Em um numero de 0 a 20 , É seu dever e advinha-lo \n")

time.sleep(1)


print("Aviso : QUANDO VOCÊ ERRAR O NÚMERO IRA GERAR AUTOMÁTICAMENTE OUTRO NÚMERO PARA SUA OUTRA CHANCE ")

print(" 1- FÁCIL(MAS CHANCES)\n2 - MÉDIO (10 CHANCES)\n 3 - DIFÍCIL(5 CHANCES)\n")


dificuldade = int(input("QUAL NIVEL  : "))

if dificuldade == 1:
	
	chances = 30
	
elif dificuldade == 2:
	chances = 10

else:
	chances = 5
	
acerto = 1


while acerto == 1:


	print()
	
	while chances != 0:

		numero_pensado = r(0,20)
	
		#print(numero_pensado)
	
		print()
	
		chute = int(input("Qual Número A Maquina Pensou? : "))
	
		if chute == numero_pensado:
		
			print(f"Correto {nome}  , Parabens")
		
			print("1 - Sim \n 2 - Não")
		
			opc = int(input(" Deseja Jogar Novamente ? :"))
			
			if opc == 2:
				
				acerto = 2
				
				time.sleep(2)
				
				print("OBRIGADO POR JOGAR :)")
				
				break

	#chute = int(input("Qual Número A Maquina pensou ? : "))
		elif chute != numero_pensado:
			print()
			print(f"Errou , O Número Era {numero_pensado}")
			chances -= 1
			print()
			print(f"Você Só Tem {chances} Chances Agora :(")
	
		elif chances == 0:
	
			print()
			print(f"{nome} Game Over !")
		
		#os.system("python3 jogo_advinha.py")