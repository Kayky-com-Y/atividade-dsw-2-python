class pessoa():
    def __init__(self, nome, idade, email):
        self.__nome = nome
        self.__idade = idade
        self.__email = email

    def get_nome(self):
        return self.__nome

    def get_idade(self):
        return self.__idade

    def get_email(self):
        return self.__email

    def adicionar_idade(self, idade):
        self.__idade += idade


def listar_pessoas(pessoas):
    print (f"pessoa 1: nome: {pessoas[0].get_nome()} idade: {pessoas[0].get_idade()} email: {pessoas[0].get_email()}")
    print (f"pessoa 2: nome: {pessoas[1].get_nome()} idade: {pessoas[1].get_idade()} email: {pessoas[1].get_email()}")
    print (f"pessoa 3: nome: {pessoas[2].get_nome()} idade: {pessoas[2].get_idade()} email: {pessoas[2].get_email()}")

pessoas = []
for i in range(3):
    continuar = True
    nome = str(input("Digite o nome da pessoa: "))
    while continuar:
        idade = int(input("Digite a idade da pessoa: "))
        if idade >= 0:
            continuar = False
        else:
            print("Idade inválida")
    email = str(input("Digite o email da pessoa: "))
    pessoa_real = pessoa(nome, idade, email)
    pessoas.append(pessoa_real)

listar_pessoas(pessoas)
continuar = True
while continuar:
    print (f"Escolha uma das 3 pessoas para adicionar idades nele: \n1 - {pessoas[0].get_nome()}\n2 - {pessoas[1].get_nome()}\n3 - {pessoas[2].get_nome()}")
    escolha = int(input("Escolha uma das 3 pessoas: "))
    idade = int(input("Digite a idade a ser adicionada: "))

    pessoas[escolha-1].adicionar_idade(idade)

    listar_pessoas(pessoas)

    continuar = str(input("Deseja continuar a adicionar idade as pessoas? [S/N] "))
    if (continuar == "N" or continuar == "n"):
        continuar = False

class Aluno(pessoa):
    def __init__(self, nome, idade, email, matricula, curso):
        super().__init__(nome, idade, email)
        self.__matricula = matricula
        self.__curso = curso

    def exibir_dados(self):
        print(f"Nome: {self.get_nome()} Idade: {self.get_idade()} Email: {self.get_email()} Matricula: {self.__matricula} Curso: {self.__curso}")

class Classe():
    def __init__(self, nome, alunos: list):
        self.__nome = nome
        self.__alunos = alunos

    def adicionar_aluno(self, aluno):
        self.__alunos.append(aluno)

    def exibir_alunos(self):
        for aluno in self.__alunos:
            aluno.exibir_dados()

classe = Classe("Classe 1", [])

for i in range(3):
    pessoa_aluno = pessoas[i]
    matricula = str(input(f"Digite a matricula do aluno {pessoa_aluno.get_nome()}: "))
    curso = str(input(f"Digite o curso do aluno {pessoa_aluno.get_nome()}: "))
    aluno = Aluno(pessoa_aluno.get_nome(), pessoa_aluno.get_idade(), pessoa_aluno.get_email(), matricula, curso)
    classe.adicionar_aluno(aluno)

classe.exibir_alunos()



