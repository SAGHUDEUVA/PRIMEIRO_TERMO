# valor1 = int(input("Digite o primeiro valor: "))
# valor2 = int(input("Digite o segundo valor: "))
# resultado = valor1/valor2
# print(f"Os resultados dessa divisão foi: {resultado}")

# Tratamento de Erros e Exceções
# valor1 = int(input("Digite o primeiro valor: "))
# valor2 = int(input("Digite o segundo valor: "))
# resultado = valor1 / valor2
# print(f"O resultado da divisão é: {resultado}")
# O código acima pode gerar um erro de divisão por zero se o usuário digitar 0 para o segundo valor. Para tratar esse erro, podemos usar um bloco try-except:
# Exemplo 1: Tratamento de divisão por zero
# try:
#     valor1 = int(input("Digite o primeiro valor: "))
#     valor2 = int(input("Digite o segundo valor: "))
#     resultado = valor1 / valor2
#     print(f"O resultado da divisão é: {resultado}")
# except ZeroDivisionError:
#     print("Erro: Não é possível dividir por zero.")

# Exemplo 2: Tratamento de entrada inválida
# try:
#     valor1 = int(input("Digite o primeiro valor: "))
#     valor2 = int(input("Digite o segundo valor: "))
#     resultado = valor1 / valor2
#     print(f"O resultado da divisão é: {resultado}")
# except ValueError:
#     print("Erro")


# namefront = input("Digite o prmeiro nome: ")
# sobrenome = input("Digite o sobrenome: ")
# nome_completed = f"{primeiro_nome} {sobrenome}"
# try:
#     print(f"Olá, {nome_completed} nome registrado com sucesso!!")
# except Exception as e:
#     print(f"Ocorreu um erro: {e}")


# Projeto 1:
# Projeto: Precisamos de um algoritmo para gerenciamento de cancelas para um shopping.
# Toda entrada e saída irá ser sinalizada
# Valores para entrada e permanência do veículo deverá ser pergutado 
# As entrada deverão ser registradas por placa.
#fazer passo a passo separado dos demais

# 
# Passo 1:  
# Perguntar informações sobre o veiculo ou forma acesso
# Pressionar o botao para emitir ticket
# Verificar se possui TAG para acesso liberado 
# Se possuir erros informar ao usuario

# Passo 2:
# Verificar tempo de permanencia
# Valor a ser cobrado

# Passo 3:
# Saida como sera?
# Calcular tempo de permanencia
# Se for tag gerar na fatura da tag
# Pagar ticket
# Devolver ticket na saida

# Passo 4:
# Gerar relatorio de entradas e saidas
# Tratamento de Erros
# Revisão do código

#fazer um codigo muito simples

print("-----Estacionamento do Shopping-----")

placa = input("Qual é a placa do seu automovel?: ").upper

horario1 = input("Qual foi a hora da sua chegada?")

horario2 = input("Qual foi a hora da sua saída?")