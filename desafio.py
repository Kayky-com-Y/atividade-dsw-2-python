class escola():
    def __init__(self, nome, cursos: list):
        self.__nome = nome
        self.__cursos = cursos

    def adicionar_curso(self, curso):
        self.__cursos.append(curso)

    def quantidade_de_cursos(self):
        return len(self.__cursos)

    def get_curso(self, index):
        return self.__cursos[index]

    def get_nome(self):
        return self.__nome

class cursos():
    def __init__(self, nome, alunos: list):
        self.__nome = nome
        self.__alunos = alunos

    def get_nome(self):
        return self.__nome

    def adicionar_aluno(self, aluno):
        self.__alunos.append(aluno)

    def listar_alunos(self):
        for i in range(len(self.__alunos)):
            self.__alunos[i].exibir_dados()

class alunos():
    def __init__(self, nome, idade, email, matricula):
        self.__nome = nome
        self.__idade = idade
        self.__email = email
        self.__matricula = matricula

    def get_nome(self):
        return self.__nome

    def get_idade(self):
        return self.__idade

    def get_email(self):
        return self.__email

    def get_matricula(self):
        return self.__matricula

    def exibir_dados(self):
        print(f"Nome: {self.get_nome()} Idade: {self.get_idade()} Email: {self.get_email()} Matricula: {self.__matricula}")

continuar = True
escola_publica = escola("Escola governador kayky batista", [])
while continuar:
    print(f"===========Gerenciador de cursos da escola {escola_publica.get_nome()}========================")
    escolha = int(input("Escolha uma das opções abaixo:\n1 - Criar um novo curso\n2 - Criar um novo aluno\n3 - Listar alunos de um curso\n4 - Sair\nDigite o numero da sua escolha: "))
    if escolha == 1:
        nome_curso = str(input("Digite o nome do curso: "))
        curso = cursos(nome_curso, [])
        escola_publica.adicionar_curso(curso)
    elif escolha == 2:
        nome_aluno = str(input("Digite o nome do aluno: "))
        idade_aluno = int(input("Digite a idade do aluno: "))
        email_aluno = str(input("Digite o email do aluno: "))
        matricula_aluno = str(input("Digite a matricula do aluno: "))
        aluno = alunos(nome_aluno, idade_aluno, email_aluno, matricula_aluno)
        print(f"Escolha um curso da {escola_publica.get_nome()}:")
        for i in range(escola_publica.quantidade_de_cursos()):
            print(f"{i+1} - {escola_publica.get_curso(i).get_nome()}")
        escolha_curso = int(input("Digite o numero do curso: "))
        escola_publica.get_curso(escolha_curso - 1).adicionar_aluno(aluno)
    elif escolha == 3:
        for i in range(escola_publica.quantidade_de_cursos()):
            print(f"{i+1} - curso - {escola_publica.get_curso(i).get_nome()}")
            print("alunos:")
            escola_publica.get_curso(i).listar_alunos()
        input("Pressione enter para voltar ao menu:")
    elif escolha == 4:
        continuar = False
    else:
        print("Opção inválida")