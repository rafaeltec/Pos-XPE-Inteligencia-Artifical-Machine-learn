
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
