import sqlite3

print('Cadastro alunos')
nome = input('Nome: ')
idade = input('Idade: ')
serie = input('Serie: ')

conexao = sqlite3.connect('banco_monstrar/banco.db')
cursor = conexao.cursor()

cursor.execute('''
 CREATE TABLE IF NOT EXISTS alunos(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            idade INTEGER, 
            serie TEXT       
            )''')

conexao.commit()

cursor.execute(
    "INSERT INTO alunos(nome, idade, serie) VALUES (?,?,?)" ,
    (nome, idade, serie)
    )

conexao.commit()

cursor.execute("SELECT * FROM alunos")

dados = cursor.fetchall()

for aluno in dados:
    print("-" * 20)
    print(f"Nome: {aluno[0]}")
    print(f"Idade: {aluno[1]}")
    print(f"Serie: {aluno[2]}")
    print("-" * 20)