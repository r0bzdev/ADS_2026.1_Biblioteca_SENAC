"""Etapa 13: o SQL que vocês já conhecem, rodando pelo Python (Aula 10).

Rode com:  python exemplos/sqlite_puro.py
"""
import sqlite3

conexao = sqlite3.connect("exemplo.db")   # o banco é um arquivo; se não existe, é criado
cursor = conexao.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS produto (
        id      INTEGER PRIMARY KEY AUTOINCREMENT,
        nome    TEXT NOT NULL UNIQUE,
        preco   REAL NOT NULL,
        tamanho TEXT NOT NULL
    )
""")

# o ? protege contra SQL injection: o valor nunca é colado no texto do SQL
cursor.execute("INSERT OR IGNORE INTO produto (nome, preco, tamanho) VALUES (?, ?, ?)",
               ("Camiseta básica", 39.90, "M"))
conexao.commit()                          # sem commit, nada fica gravado

for linha in cursor.execute("SELECT id, nome, preco FROM produto WHERE preco < ?", (100,)):
    print(linha)                          # (1, 'Camiseta básica', 39.9)

conexao.close()
