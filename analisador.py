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

arrSaida = []
arrErros = []
arrSimbolos = []

def addSaida(descricao,numeroLinha):
    arrSaida.append('[' + str(numeroLinha) + '] ' + descricao)

def addErros(numeroLinha):
    arrErros.append(str(numeroLinha))

def addSimbolos(string):
    if string not in arrSimbolos:
        arrSimbolos.append(string)
    return (arrSimbolos.index(string))+1


def ehComentario(string,numeroLinha):
    if(len(string) >= 2):
        if string[0] == '/' and string[1] == '/':
            addSaida('COMENTÁRIO',numeroLinha)
            return True
        else:
            return False
    else:
        return False

def ehReservada(string,numeroLinha):
    palavrasReservadas = 'int double float real break case char const continue'
    for palavraReservada in palavrasReservadas.split(' '):
        if string == palavraReservada:
            addSaida(palavraReservada.upper(),numeroLinha)
            return True

def ehInteiro(string,numeroLinha):
    listaNumeros = '0 1 2 3 4 5 6 7 8 9'
    if(len(string) > 2):
        return False
    else:
        for caractere in string:
            if caractere not in listaNumeros.split(' '):
                return False

        identificador = addSimbolos(string)
        addSaida('IDENTIFICADOR ' + str(identificador),numeroLinha)
        return True

def ehReal(string,numeroLinha):
    listaNumeros = '0 1 2 3 4 5 6 7 8 9'
    numeroSplit = string.split('.')
    if(len(numeroSplit) == 2):
        if (len(numeroSplit[0]) >= 1 and len(numeroSplit[0]) <= 2) and (len(numeroSplit[1]) >= 1 and len(numeroSplit[1]) <= 2):
            numeroInteiro = numeroSplit[0]
            numeroReal = numeroSplit[1]

            for inteiro in numeroInteiro:
                if inteiro not in listaNumeros.split(' '):
                    return False

            for real in numeroReal:
                if real not in listaNumeros.split(' '):
                    return False

            identificador = addSimbolos(string)
            addSaida('IDENTIFICADOR ' + str(identificador),numeroLinha)
            return True

def ehIdentificador(string,numeroLinha):
    listaLetras = 'a b c d e f g h i j k l m n o p q r s t u v w x y z'
    listaNumeros = '0 1 2 3 4 5 6 7 8 9'
    if string[0] not in listaLetras:
        return False
    else:
        for caractere in string:
            if caractere not in listaLetras and caractere not in listaNumeros:
                return False
        identificador = addSimbolos(string)
        addSaida('IDENTIFICADOR ' + str(identificador),numeroLinha)
        return True

fileInput = open('entrada.txt')
numeroLinha = 1
for fileLine in fileInput.readlines():
    fileLineSplit = fileLine.split(' ',1)
    if ehComentario(''.join(fileLineSplit[0].split()),numeroLinha):
        exit
    elif len(fileLineSplit) > 1:
        addErros(numeroLinha)
    else:
        if ehReservada(''.join(fileLineSplit[0].split()),numeroLinha):
            exit
        elif ehInteiro(''.join(fileLineSplit[0].split()),numeroLinha):
            exit
        elif ehReal(''.join(fileLineSplit[0].split()),numeroLinha):
            exit
        elif ehIdentificador(''.join(fileLineSplit[0].split()),numeroLinha):
            exit
        else:
            addErros(numeroLinha)

    numeroLinha += 1

fileInput.close()

fileOutput = open('saida.txt','wt')
fileOutput.write('\n'.join(arrSaida))

fileOutput.write('\nTabela de símbolos:')
for ind, simbolo in enumerate(arrSimbolos):
    fileOutput.write('\n' + str(ind+1) + ' - ' + simbolo)
fileOutput.write('\nO programa possui erro nas seguintes linhas: ' + ', '.join(arrErros))
fileOutput.close()