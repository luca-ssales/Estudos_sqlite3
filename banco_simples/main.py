import sqlite3 # importei o sql

conexao = sqlite3.connect('banco_simples/banco.db') #cria o banco
cursor = conexao.cursor() #cursor p funcionar os comandos do sql


#cria a tabela
cursor.execute("""
CREATE TABLE IF NOT EXISTS alunos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT,
    idade INTEGER
)
""")

conexao.commit() #salva as alterções feitas

print('Banco criado com sucesso!✅')