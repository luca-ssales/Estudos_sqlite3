#crie um sistema de loja onde tem a opção de registrar funcionario e vendas, 
# e imprima ambos se o admin quiser

import sqlite3

print('----- 👕 Loja de Roupas 👖 -----')
login = input('     👤Login: ')
senha = input('     🔐Senha: ')

if login == 'admin' and senha == '1234':
    print('BEM VINDO ADMIN')
    print('1️⃣- Cdastrar funcionario')
    print('2️⃣- Registrar venda')
    menu = input('Oque deseja fazer: ')
    print()

    if menu == '1':
        print('--- Cadastro de Funcionario ---')
        nome = input('Nome: ')
        cargo = input('Cargo: ')
        email = input('Email: ')
        telefone = input('Telefone: ')

        conexao = sqlite3.connect('desafio/banco.db')
        cursor = conexao.cursor()

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS funcionario(
                nome TEXT,
                cargo TEXT,
                email TEXT,
                telefone INTEGER
        )''')
        conexao.commit()

        cursor.execute(
            "iNSERT INTO funcionario(nome, cargo, email, telefone) VALUES (?,?,?,?)",
            (nome, cargo, email, telefone)
        )
        conexao.commit()

        print('Funcionario Cadastrado✅')

        mostrar = input('Deseja ver o funcionario cadastrado?')

        if mostrar == 'sim':
            cursor.execute("SELECT * FROM funcionario")

        dados = cursor.fetchall()
        
        for funcionario in dados:
            print("-" * 20)
            print(f"Nome: {funcionario[0]}")
            print(f"Cargo: {funcionario[1]}")
            print(f"Email: {funcionario[2]}")
            print(f"Telefone: {funcionario[2]}")
            print("-" * 20)
        
        else:
            print('Obrigado, até breve!')


    if menu == '2':
        print('--- Registro de Venda ---')
        cliente = input('Cliente: ')
        produto = input('Produto: ')
        vendedor = input('Vendedor: ')
        preco = input('Preço: ')

        conexao = sqlite3.connect('desafio/banco.db')
        cursor = conexao.cursor()

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS vendas(
                cliente TEXT,
                produto TEXT,
                vendedor TEXT,
                preco INTEGER
        )''')
        conexao.commit()

        cursor.execute(
            "iNSERT INTO vendas(cliente, produto, vendedor, preco) VALUES (?,?,?,?)",
            (cliente, produto, vendedor, preco)
        )
        conexao.commit()

        print('Venda Registrada✅')

        mostrar = input('Deseja ver a venda registrada? ')

        if mostrar == 'sim':
            cursor.execute("SELECT * FROM vendas")

        dados = cursor.fetchall()
        
        for venda in dados:
            print("-" * 20)
            print(f"Nome: {venda[0]}")
            print(f"Cargo: {venda[1]}")
            print(f"Email: {venda[2]}")
            print(f"Telefone: {venda[2]}")
            print("-" * 20)
        
        else:
            print('Obrigado, até breve!')