def linhas():
    print('-=' * 40)

class Tarefa:
    def __init__(self, titulo, descricao):
        self.titulo = titulo
        self.descricao = descricao
        self.status_tarefa = False
        


class GerenciadorTarefa:
    def __init__(self):
        self.tarefas = []


    def adicionar_tarefa(self):
        linhas()
        print('Adicionar tarefa: ')
        linhas()

        while True:
            nome_tarefa = Tarefa(self.titulo)
            descricao_tarefa = Tarefa(self.descricao)
            self.tarefas.append(nome_tarefa)
            self.tarefas.append(descricao_tarefa)

            opcao = input('Deseja adicionar outra tarefa? [Sim/Não]: ').strip().lower()

            if opcao != 'sim':
                break

tarefa = Tarefa()
gerenciador = GerenciadorTarefa()

gerenciador.adicionar_tarefa(tarefa)
