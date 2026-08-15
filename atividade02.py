
def inicio():
    numero = int(input("""============Bem vindo a minha atividade 02================
        
    escolha uma das opções abaixo:
    0 - Sair"""))
    return (menu(numero))

def menu(numero):
    if (numero == 0):
        print("Saindo...")
        return
    elif (numero == 1):
        atividade1()
    elif (numero == 2):
        atividade2()
    elif (numero == 3):
        atividade3()
    else:
        print("Opção inválida")
        return inicio()
    
def atividade1():
    lista = []
    print("Atividade 1 - lista de 10 números e a sua media, seu maior e seu menor numero")
    for i in range(10):
        num = int(input("Digite um número: "))
        lista.append(num)
    atividade1_maior_menor_e_media(lista)
    print("Fim da atividade 1")
    return inicio()

def atividade1_maior_menor_e_media(lista):
    print(f"O maior número é: {max(lista)}")
    print(f"O menor número é: {min(lista)}")
    total = 0
    for i in range (10):
        total += lista[i]
    print(f"A média é: {total/10}")
    input("Pressione enter para voltar ao menu")
    return

def atividade2():
    print("Atividade 2 - O texto que conta suas vogais, retorna ele invertido e verifica se o texto é parindromo")

    texto = str(input("Digite um texto: "))

    atividade2_vogais(texto)
    atividade2_parindromo(texto, atividade2_invertido(texto))
    print("Fim da atividade 2")
    input("Pressione enter para voltar ao menu")
    return inicio()

def atividade2_vogais(texto):
    vogais = 0
    for i in range(len(texto)):
        if (texto[i] == "a" or texto[i] == "e" or texto[i] == "i" or texto[i] == "o" or texto[i] == "u" or texto[i] == "A" or texto[i] == "E" or texto[i] == "I" or texto[i] == "O" or texto[i] == "U"):
            vogais += 1
    print(f"O texto possui {vogais} vogais")
    return

def atividade2_invertido(texto):
    texto_invertido = ''
    for i in range(len(texto)-1, -1, -1):
        texto_invertido += texto[i]
    print(f"O texto invertido é: {texto_invertido}")
    return texto_invertido

def atividade2_parindromo(texto, texto_invertido):
    if (texto != texto_invertido):
        print("O texto não é parindromo")
        return
    print("O texto é parindromo")
    return

def atividade3():
    dicionario = {
    }
    lista = []
    continuar = True
    print("Atividade 3 - dicionario de nomes e quantas veses cada um aparece")

    while continuar:
        nome = str(input("Digite um nome para ser adicionado a lista: "))
        lista.append(nome)
        print(f"A lista atual é: {lista}")
        continuar = str(input("Deseja continuar? [S/N] "))
        if (continuar == "N" or continuar == "n"):
            continuar = False

    for i in range(len(lista)):
        if (lista[i] in dicionario):
            dicionario[lista[i]] += 1
        else:
            dicionario[lista[i]] = 1

    for i in range(len(dicionario)):
        print(f"O nome {list(dicionario.keys())[i]} aparece {list(dicionario.values())[i]} vezes")
    print("Fim da atividade 3")
    input("Pressione enter para voltar ao menu")
    return inicio()





inicio()
