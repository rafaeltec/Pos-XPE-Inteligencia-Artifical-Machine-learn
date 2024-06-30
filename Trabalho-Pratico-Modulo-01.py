
#Atividade 1
#Execute e analise a saída do seguinte código no Google Colab:
# Declaração das variáveis
inicio = 0
fim = 100

# Verifica quais números são divisíveis por cinco e exibe aqueles que são
for numero in range(inicio, fim):
    if numero % 5 == 0:
        print(numero)

#Atividade 2
#Altere o código da atividade 1 para que ele exiba os números múltiplos de 2, 5 e 7 (simultaneamente) e que estejam dentro do intervalo entre 100 e 500 (incluindo o 100 e o 500).
# Declaração das variáveis
inicio = 100
fim = 501  # Inclui o 500 no intervalo

# Verifica quais números são divisíveis por 2, 5 e 7 simultaneamente
for numero in range(inicio, fim):
    if numero % 2 == 0 and numero % 5 == 0 and numero % 7 == 0:
        print(numero)


#Atividade 3
#Altere o código da atividade 1,
#criando uma variável divisor e, em seguida, verifique quais os números no intervalo entre 0 e 1000 (incluindo o 0 e excluindo o 1000) são múltiplos da variável divisor.
# Declaração das variáveis
inicio = 0
fim = 1000
divisor = 3  # Você pode alterar este valor para qualquer outro divisor desejado

# Verifica quais números são divisíveis pelo valor da variável divisor
for numero in range(inicio, fim):
    if numero % divisor == 0:
        print(numero)
        
        
#Atividade 4
#Crie um código declarando as seguintes variáveis do tipo string e realize as transformações solicitadas.
# Variáveis do tipo string
nome = 'João da Silva'
cidade = 'São Paulo'
cpf = '123.456.789-00'

# Transforme todos os caracteres das variáveis em maiúsculo
print(nome.upper())
print(cidade.upper())
print(cpf.upper())

# Transforme todos os caracteres das variáveis em minúsculo
print(nome.lower())
print(cidade.lower())
print(cpf.lower())

# Exiba a posição do caractere 'ã', se presente, em cada uma das variáveis
print(nome.find('ã'))
print(cidade.find('ã'))
print(cpf.find('ã'))

# Exiba o número de caracteres de cada variável
print(len(nome))
print(len(cidade))
print(len(cpf))

# Remova os pontos (.) e o hífen (–) da variável cpf
cpf_limpo = cpf.replace('.', '').replace('-', '')
print(cpf_limpo)


#Atividade 5
#Crie um código que realize o somatório de todos os caracteres da seguinte string:
numero = '127957'

# Inicializa a variável auxiliar soma
soma = 0

# Percorre cada caractere da string e soma os valores numéricos
for caractere in numero:
    soma += int(caractere)

print(soma)

