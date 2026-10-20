# Manipulação de Strings

# - Strings são textos ou uma cadeia de caracteres que ficam dentro de aspas. 
# - As aspas delimitam o contéudo da string do código do programa

# + Formatação de Strings

# - Usamos formatações para conseguirmos utilizar diferentes tipos de dados dentro de uma string

# ++ Método Format()

a = "AAA" #--> str
b = 7     #--> int
c = 1.2   #--> float

""" -- Formatação normal, depende da ordem de como os parâmetros/variáveis são adcionados no metodo format(), 
não sendo possível usar a mesma variável mais de uma vez dentro da string"""

                              # ':.2f' limita a quantidade de casas decimais (nesse caso, 2 casas)
string = "a = {}  b = {}  c = {:.2f}" 
formatado = string.format(a, b, c)

""" -- Formatação utilizando indices(posições) dos parâmetros, não depende da ordem do format() e permite utilizar
a mesma variável mais de uma vez dentro da string(não muito recomendado)"""
string = "a = {0}  b = {1}  c = {2:.2f}" 
formatado = string.format(a, b, c)
               # indices: 0, 1, 2

""" -- Formatação usando parâmentos nomeados. Não dependem da ordem do format() podem ser utilizados mais de uma vez
na mesma string(mais recomendados do que utilizar com indices). Porém ao nomear um parâmetro, você obrigatoriamente
deve nomear todos os outros dentro do método format()"""
string = "a = {var1}  b = {var2}  c = {var3:.2f}" 

formatado = string.format(var1=a, var2=b, var3=c)

print(formatado)
#saida >> a = AAA  b = 7  c = 1.20



## ++ Interpolação

# Diferente do format(), essa formatação é preciso se atentar ao tipo de dado, pois a simbologia muda.

"""
s - string
d e i - int
f - float
x e X - Hexadecimal
...
"""

nome = "Luiz"
fatura = 1000.9873
dias = 189

""" -- Essa formatação é mais antiga, porém é utilizada para formatações de erros de bibliotecas de logger,
para fazer a chamada dos valores é obrigatório usar a '%' e se atentar para o tipo de dado trabalhado."""
string2 = 'Olá %s, o valor da fatura foi de R$%.2f e voce tem %d dias para pagar.' % (nome, fatura, dias)
                                           # O '.2' entre o '%' e o 'f' é o limitador de casas decimais 
print(string2)

#saída >> Olá Luiz, o valor da fatura foi de R$1000.99 e voce tem 189 dias para pagar.



# ++ f-Strings

# - Formatação de strings mais recente atualmente, possui várias funcionalidades úteis para o tratamento de texto


"""
s - string
d - int
f - float
 .<qtde de dígitos>f
x ou X - Hexadecimal

(caractere)(><^)(quantidade)
> - Esquerda (adiciona os caracteres escolhidos ao lado esquerdo da variável)
< - Direita  (adiciona os caracteres escolhidos ao lado direito da variável)
^ - Centro   (adiciona os caracteres escolhidos de ambos os lados da variável)
"""

nome = 'Afonso'

print(f'Olá, prazer em te conhecer {nome}')