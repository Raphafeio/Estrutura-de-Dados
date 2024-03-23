# Crie um vetor para armazenar as notas de 5 aluno de uma disciplina, use os metodo append.
vet_a = []
vet_a.append(9)
print(vet_a)
# Crie um vetor para armazenar os nome dos 5 alunos de uma turma, use o metodo sort.
Alunos = ["Maria", "Pedro", "Ana", "Carlos", "Vitória"]

Alunos.sort()
for Aluno in Alunos:
    print(Alunos)
# Crie um vetor para armazenar os preços de 5 produtos de uma loja, use o metodo index para encontrar um preço de um produto especifico.
Precos = ["36.55","10.40","12.20","14.50","20.00"]

Precos_produtos = "36.55"

indice = Precos.index(Precos_produtos)
print(f"O preço do produto é {Precos_produtos} e está armazenado em {indice} do vetor")
# Crie um vetor para armazenar as alturas de 5 alunos de uma turma, use o metodo reverse para ordenar em ordem descrecente.
Altura = ["1.78","1.65","1.85","1.97","1.55"]

Altura.sort(reverse=True)
print(Altura)
# Crie uma matrix para representar um tabuleiro de xadrez, use indices para acessar e alterar na matrix.
mat_a = [['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R'], 
    ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],  
    ['_', '_', '_', '_', '_', '_', '_', '_'],  
    ['_', '_', '_', '_', '_', '_', '_', '_'],  
    ['_', '_', '_', '_', '_', '_', '_', '_'],  
    ['_', '_', '_', '_', '_', '_', '_', '_'], 
    ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'], 
    ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r']]

def mostrar_tabuleiro(mat_a):
    for linha in mat_a:
        print("".join(linha))

mostrar_tabuleiro(mat_a)
# Crie uma matrix para armazenar os assentos de um cinema, use indices para marcar um assento como ocupado ou desocupado.
num_Linha = 5
num_coluna = 14

assentos_cinema = [[0 for _ in range(num_coluna)] for _ in range(num_Linha)]

def exibir_assentos():
    for i in range(num_Linha):
        for j in range(num_coluna):
            if assentos_cinema[i][j] == 0:
                print("0", end=" ")
            else:
                print("X", end=" ")
        print()

print("Assentos do Cinema:")
exibir_assentos()
# Emplemente uma pilha para armazenar o historico de navegação em um navegador web
class NavegadorWeb:
    def __init__(self):
        self.historico = []

    def visitar_pagina(self, url):
        print("Visitando página:", url)
        self.historico.append(url)

    def voltar_Pagina(self):
        if len(self.historico) > 1:
            pagina_atual = self.historico.pop()
            pagina_anterior = self.historico[-1]
            print("Voltando para:",pagina_anterior)
            return pagina_anterior
        else:
            print("Nãoc há páginas anteriores para voltar.")
            return None
        
navegador = NavegadorWeb()
navegador.visitar_pagina("www.google.com")
navegador.visitar_pagina("www.wikipedia.org")

print("\nVoltando uma página:")
navegador.voltar_Pagina()

print("\nVoltando outra página:")
navegador.voltar_Pagina()
# Emplemente uma pilha para realizar operações de desfazer e refazer um editor de texto
class EditorDeTexto:
    def __init__(self):
        self.texto = ""
        self.operacoes_desfazer = []
        self.operacoes_refazer = []

    def inserir_texto(self, texto):
        print("Inserindo texto:", texto)
        self.texto += texto
        self.operacoes_desfazer.append(("inserir", texto))

    def deletar_texto(self, indice, quantidade):
        texto_deletado = self.texto[indice:indice+quantidade]
        print("Deletando texto:", texto_deletado)
        self.texto = self.texto[:indice] + self.texto[indice+quantidade:]
        self.operacoes_desfazer.append(("deletar", texto_deletado, indice))

    def desfazer(self):
        if self.operacoes_desfazer:
            operacao = self.operacoes_desfazer.pop()
            if operacao[0] == "inserir":
                texto_inserido = operacao[1]
                self.texto = self.texto[:-len(texto_inserido)]
                self.operacoes_refazer.append(("inserir", texto_inserido))
                print("Desfazendo inserção:", texto_inserido)
            elif operacao[0] == "deletar":
                texto_deletado = operacao[1]
                indice = operacao[2]
                self.texto = self.texto[:indice] + texto_deletado + self.texto[indice:]
                self.operacoes_refazer.append(("deletar", indice, len(texto_deletado)))
                print("Desfazendo deleção:", texto_deletado)

    def refazer(self):
        if self.operacoes_refazer:
            operacao = self.operacoes_refazer.pop()
            if operacao[0] == "inserir":
                texto_inserido = operacao[1]
                self.texto += texto_inserido
                self.operacoes_desfazer.append(("inserir", texto_inserido))
                print("Refazendo inserção:", texto_inserido)
            elif operacao[0] == "deletar":
                indice = operacao[1]
                quantidade = operacao[2]
                texto_deletado = self.texto[indice:indice+quantidade]
                self.texto = self.texto[:indice] + self.texto[indice+quantidade:]
                self.operacoes_desfazer.append(("deletar", texto_deletado, indice))
                print("Refazendo deleção:", texto_deletado)

    def exibir_texto(self):
        print("Texto atual:", self.texto)

editor = EditorDeTexto()
editor.inserir_texto("Olá, mundo!")
editor.exibir_texto()

editor.deletar_texto(4, 6)
editor.exibir_texto()

print("\nDesfazer uma operação:")
editor.desfazer()
editor.exibir_texto()

print("\nRefazer uma operação:")
editor.refazer()
editor.exibir_texto()
# Implemente uma fila para simular um fila de impressão.
class FilaDeImpressao:
    def __init__(self):
        self.fila = []

    def adiconar_documento(self, documento):
        print("Adicionado documento á fila de impressão:", documento)
        self.fila.append(documento)
    def imprimir_documento(self):
        if self.fila:
            documento = self.fila.pop(0)
            print("Imprimindo documento:", documento)
        else:
            print("A fila de impressão está vazia.")
# Implemente uma fila para simular uma fila de atendimento ao cliente.
class FilaDeAtendimento:
    def __init__(self):
        self.fila = []

    def adicionar_cliente(self, cliente):
        print("Adicionando cliente à fila de atendimento:", cliente)
        self.fila.append(cliente)

    def atender_cliente(self):
        if self.fila:
            cliente = self.fila.pop(0)
            print("Atendendo cliente:", cliente)
        else:
            print("Não há clientes na fila de atendimento.")

fila_de_atendimento = FilaDeAtendimento()
fila_de_atendimento.adicionar_cliente("Cliente 1")
fila_de_atendimento.adicionar_cliente("Cliente 2")
fila_de_atendimento.adicionar_cliente("Cliente 3")

print("\nAtendendo clientes:")
fila_de_atendimento.atender_cliente()
fila_de_atendimento.atender_cliente()
fila_de_atendimento.atender_cliente()

print("\nTentando atender mais um cliente:")
fila_de_atendimento.atender_cliente()
# Emplemente uma fila para simular um envio de mensagem em um aplicativo de mensagem.
class AplicativoMensagens:
    def __init__(self):
        self.fila_envio = []

    def enviar_mensagem(self, mensagem):
        print("Enviando mensagem:", mensagem)
        self.fila_envio.append(mensagem)

    def receber_mensagem(self):
        if self.fila_envio:
            mensagem = self.fila_envio.pop(0)
            print("Recebendo mensagem:", mensagem)
        else:
            print("Não há mensagens para receber.")

app_mensagens = AplicativoMensagens()
app_mensagens.enviar_mensagem("Olá, tudo bem?")
app_mensagens.enviar_mensagem("Como vai você?")

print("\nRecebendo mensagens:")
app_mensagens.receber_mensagem()
app_mensagens.receber_mensagem()
app_mensagens.receber_mensagem()

print("\nTentando receber mais uma mensagem:")
app_mensagens.receber_mensagem()
# Emplemente uma fila para simular a excecução de processos em um sistema operacional.
class SistemaOperacional:
    def __init__(self):
        self.fila_processos = []

    def adicionar_processo(self, processo):
        print("Adicionando processo à fila de execução:", processo)
        self.fila_processos.append(processo)

    def executar_processo(self):
        if self.fila_processos:
            processo = self.fila_processos.pop(0)
            print("Executando processo:", processo)
        else:
            print("Não há processos para executar.")

sistema_operacional = SistemaOperacional()
sistema_operacional.adicionar_processo("Processo 1")
sistema_operacional.adicionar_processo("Processo 2")
sistema_operacional.adicionar_processo("Processo 3")

print("\nExecutando processos:")
sistema_operacional.executar_processo()
sistema_operacional.executar_processo()
sistema_operacional.executar_processo()

print("\nTentando executar mais um processo:")
sistema_operacional.executar_processo()
