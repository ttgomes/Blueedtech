def menuordens():
    print (''' 
              Menu:

              [0] - Sair​
              [1] - Exibir lista de alunos com suas notas (cada aluno tem uma nota)​
              [2] - Inserir aluno e nota​
              [3] - Alterar a nota de um aluno​
              [4] - Consultar nota de um aluno específico ​
              [5] - Apagar um aluno da lista​
              [6] - Exibir a média da turma''')
              
    ​
sair = (0)
exibir_lista = (1)
inserir_aluno = (2)
Alterar_nota = (3)
consultar_nota = (4)
apagar_aluno = (5)
exibir_media = (6)

while True :
    sair = input("digite o numero no menu que desja acessar ?: (fim para sair) ")
    if sair == "fim":
     break

