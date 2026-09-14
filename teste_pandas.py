"""
Teste de leitura e manipulação de dados com pandas
a partir de 3 fontes diferentes: TXT, CSV e um banco de dados
(aqui simulado com SQLite, mas o read_sql funciona igual para MySQL,
bastando trocar a connection string do SQLAlchemy).
"""

import pandas as pd
from sqlalchemy import create_engine

print("=" * 60)
print("1) LENDO O ARQUIVO TXT (separado por ';')")
print("=" * 60)
df_txt = pd.read_csv("sample.txt", sep=";")
print(df_txt)
print("\nTipos de dados:")
print(df_txt.dtypes)

print("\n" + "=" * 60)
print("2) LENDO O ARQUIVO CSV")
print("=" * 60)
df_csv = pd.read_csv("sample.csv")
print(df_csv)
print("\nEstatísticas rápidas (preco e estoque):")
print(df_csv[["preco", "estoque"]].describe())

print("\n" + "=" * 60)
print("3) LENDO O BANCO DE DADOS (SQLite simulando MySQL)")
print("=" * 60)
# Em um MySQL real, a linha abaixo seria algo como:
# engine = create_engine('mysql+pymysql://usuario:senha@localhost:3306/banco')
engine = create_engine("sqlite:///sample_db.sqlite")
df_db = pd.read_sql("SELECT * FROM funcionarios", engine)
print(df_db)
print("\nSalário médio por departamento:")
print(df_db.groupby("departamento")["salario"].mean().round(2))

print("\n" + "=" * 60)
print("4) EXEMPLO DE MANIPULAÇÃO COMBINANDO AS 3 FONTES")
print("=" * 60)
print(f"Total de registros TXT: {len(df_txt)}")
print(f"Total de registros CSV: {len(df_csv)}")
print(f"Total de registros DB : {len(df_db)}")

# Exemplo: idade média (TXT) e salário médio (DB) lado a lado
print(f"\nIdade média das pessoas (TXT): {df_txt['idade'].mean():.1f} anos")
print(f"Salário médio dos funcionários (DB): R$ {df_db['salario'].mean():.2f}")
print(f"Preço médio dos produtos (CSV): R$ {df_csv['preco'].mean():.2f}")
