import random 

def adivinhe_o_numero():
	numero_secreto = random.randint(1, 100) 
	tentativas = 0 

	
	print("Bem-vindo ao jogo 'Adivinhe o Número'!")
	print("Escolha um nível de dificuldade:")
	print("1 - Fácil (10 tentativas)")	
	print("2 - Médio (7 tentativas)")
	print("3 - Difícil (5 tentativas)")


	dificuldade = int (input("Escolha o nível: "))


	if dificuldade == 1:
		max_tentativas = 10
	elif dificuldade == 2:
		max_tentativas = 7
	else:
		max_tentativas = 5


	print("Estou pensando em um número entre 1 e 100.")

	
	while tentativas < max_tentativas:
		palpite = int(input("Faça um palpite: "))
		tentativas += 1
	
		if palpite < numero_secreto:
			print("Muito baixo! Tente novamente.")
		elif palpite > numero_secreto:
			print("Muito alto! Tente novamente.")
		else:
			print(f"Parabéns! Você adivinhou o número em {tentativas} tentativas.")
			break

	if tentativas == max_tentativas:
		print(f"Você atingiu o número máximo de tentativas. O número secreto era {numero_secreto}.")		

if __name__ == "__main__":
	adivinhe_o_numero()

















	
