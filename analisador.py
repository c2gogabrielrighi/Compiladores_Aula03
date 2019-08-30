# Crie um autômato para reconhecer linguagens cujos tokens podem ser:
# - Identificadores iniciados por uma letra, podendo possuir na sequência zero e/ou mais números e/ou letras;
# - Constantes numéricas formadas por um ou mais números inteiros na casa da dezena, ou seja, até o valor 99;
# - Constantes numéricas formadas por números reais, também na casa da dezena, ou seja, valor máximo de 99.99;
# - Identificadores no formato de comentários de linha, padrão da Linguagem C (//);
# - As palavras reservadas da linguagem C: int, double, float, real, break, case, char, const, continue.

# RegEx para identificadores: [a-zA-Z]\w{0,}
# RegEx para constantes numéricas int: \d{1,2}
# RegEx para constantes numéricas real: \d{1,2}\.\d{1,2}
# RegEx para identificador de comentário de linha: \/{2}.{0,}


# Definição de regras
regexIdentificadores = r'[a-zA-Z]\w{0,}'
regexNumInteiro = r'\d{1,2}'
regexNumReal = r'\d{1,2}\.\d{1,2}'
regexComentario = r'\/{2}.{0,}'
palavrasReservadas = [
    'int',
    'double',
    'float',
    'real',
    'break',
    'case',
    'char',
    'const',
    'continue'
]

for palavra in palavrasReservadas:
    print(palavra)

# Método: lê a string, remove todos os tokens e identificadores que encontrar. Se sobrar algum, retorna erro.