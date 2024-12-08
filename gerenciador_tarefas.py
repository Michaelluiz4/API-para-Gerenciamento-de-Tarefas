def linhas():
    print('-=' * 40)


class Tarefa:
    def __init__(self, nome, descricao):
        self.nome = nome
        self.descricao = descricao
        self.status_tarefa = False        


    def __str__(self):
        return f'Tarefa: {self.nome}. Descrição: {self.descricao}'


class GerenciadorTarefa:
    def __init__(self):
        self.tarefas = []


    def adicionar_tarefa(self):
        descricao = None

        while True:
            linhas()
            print('Adicionar tarefa:')

            adicionar_tarefa = input('Você deseja adicionar alguma tarefa: [Sim/Não]: ').strip().lower()
            print()

            if adicionar_tarefa == 'sim':
                nome_tarefa = input('Tarefa: ').strip().lower()
                if nome_tarefa not in [tarefa.nome for tarefa in self.tarefas]:
                    adicionar_descricao = input('Deseja adicionar uma descrição? [Sim/Não]: ').strip().lower()
                    if adicionar_descricao == 'sim':
                        descricao = input('Descrição da tarefa: ')    
                    nova_tarefa = Tarefa(nome_tarefa, descricao)
                    self.tarefas.append(nova_tarefa)
                    print(f'\033[32mSucesso\033[0m. Tarefa {nome_tarefa} adicionada com sucesso. ')
                else:
                    print(f'Tarefa {nome_tarefa} já está na lista de tarefas. ')
            elif adicionar_tarefa in ['nao', 'não']:
                break
            else:
                print('\033[31mERRO\033[0m: Opção invalída. ')
                continue


    def exibir_tarefas(self):
        if not self.tarefas:
            print('Nenhuma tarefa foi adicionada.')
        else:
            for tarefa in self.tarefas:
                print(tarefa)


gerenciador = GerenciadorTarefa()

gerenciador.adicionar_tarefa()
gerenciador.exibir_tarefas()
