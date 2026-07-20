import sqlite3 # importei o sql

print("Sistema de Cadastro Novos Alunos")
#criei as variaveis com inputs
nome = input('Nome: ') 
idade = input('Idade: ')
serie = input('Serie: ')

conexao = sqlite3.connect('banco_variaveis/banco.db') #crie o banco
cursor = conexao.cursor() #cursor para que os comandos do sql funcione

#criei a tabela "alunos"
cursor.execute('''
    CREATE TABLE IF NOT EXISTS alunos(
    nome TEXT, 
    idade INTEGER,
    serie TEXT
        )''')

conexao.commit() #commit p salvar as alterações feitas acima

#adicionei os valores das variaveis dentro da tebela que criei a cima
cursor.execute(
    "INSERT INTO alunos (nome, idade, serie) VALUES (?,?,?)",
    (nome, idade, serie)
    )

conexao.commit() #commit p salvar as alterações feitas acima

print('Aluno Cadastrado!') #print p ter crtz q o banco foi criado