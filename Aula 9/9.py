# 1. O Problema da Idade
# idade = input("Digite sua idade: ")
# if idade >= 18:
# print("Você é maior de idade.")

# corrigido:
# idade = int(input("Digite sua idade: "))
# if idade >= 18:
#     print("Você é maior de idade.")

#melhoria:
# try:
#     idade = int(input("Digite sua idade: "))
#     if idade >= 18:
#         print("Você é maior de idade.")
#     else:
#         print("Você é menor de idade.")
# except:
#     print("Erro: Por favor, digite um número inteiro válido.")


# 2. A Escrita Fiel
# nome = "Mariana"
# print("Seja bem-vinda, nome!")

#melhoria:
# nome = "Juan"
# print(f"Seja bem-vindo, {nome.title()}!")

#corrigido:
# nome = "Juan"
# print(f"Seja bem-vindo, {nome}!")



# 3. Falta de Espaço
# numero = 10
# if numero > 5:
# print("O número é maior que cinco.")
# else:
# print("O número é menor ou igual a cinco.")
#melhoria:
# numero = 10
# limite = 5

# if numero > limite:
#     print(f"O número {numero} é maior que {limite}.")
# else:
#     print(f"O número {numero} é menor ou igual a {limite}.")

#corrigido:
# numero = 10
# if numero >= 5:
#     print("O número é maior que cinco.")
# else:
#     print("O número é menor ou igual a cinco.")




# 4. Esquecimento Fatal
# usuario = "aluno123"
# if usuario == "aluno123"
# print("Login realizado com sucesso.")

#corrigido:
# usuario = "aluno123"
# if usuario == "aluno123":
#     print("Login realizado com sucesso.")

#melhoria:
# usuario = "aluno123"

# if usuario == "aluno123":
#     print("Login realizado com sucesso.")
# else:
#     print("Usuário incorreto. Acesso negado.")




# 5. Atribuição vs. Comparação
# clima = "ensolarado"
# if clima = "chuvoso":
# print("Leve um guarda-chuva!")

#melhoria:
# clima = "Chuvoso "

# if clima.lower().strip() == "chuvoso":
#     print("Leve um guarda-chuva!")
# else:
#     print("O tempo parece bom, aproveite o dia!")

#corrigido
# clima = "ensolarado"
# if clima == "chuvoso":
#     print("Leve um guarda-chuva!") 




# 6. Misturando Alhos com Bugalhos
# pontos = 50
# print("Parabéns! Você fez " + pontos + " pontos.")

#melhoria:
# pontos = 50
# print(f"Parabéns! Você fez {pontos} pontos.")

#corrigido:
# pontos = 50
# print(f"Parabéns! Você fez {pontos} pontos.")

# 7. A Ordem dos Fatores
# O sistema deve dar "Excelente" para notas 9 ou 10.
# nota = 9.5
# if nota >= 7:
# print("Aprovado")
# elif nota >= 9:
# print("Excelente!")

#melhoria:
# nota = 9.5

# if nota >= 9:
#     print("Excelente!")
# elif nota >= 7:
#     print("Aprovado")
# else:
#     print("Reprovado. Precisa estudar mais!")

# corrigido:
# nota = 9.5
# if nota >= 9:
#     print("Excelente!")
# elif nota >= 7:
#     print("Aprovado")

# 8. O Contador de 1 a 5
# Objetivo: Mostrar na tela os números 1, 2, 3, 4 e 5.
# for i in range(5):
# print(i)

#corrigido:
# for i in range(1, 6):
#     print(i)

# 9. O Loop Eterno
# tentativas = 1
# while tentativas <= 3:
# print("Tentando conectar...")
# O código deveria parar após 3 tentativas

#corrigido:
# tentativas = 1
# while tentativas <= 3:
#     print("Tentando conectar...")
#     tentativas += 1

# 10. A Senha Teimosa
# O programa deve pedir a senha até que o usuário digite "python123"
# senha = ""
# while senha == "python123":
# senha = input("Digite a senha secreta: ")
# print("Acesso concedido!")

#corrigido:
# senha = ""
# while senha != "python123":
#     senha = input("Digite a senha secreta: ")
# print("Acesso concedido!")