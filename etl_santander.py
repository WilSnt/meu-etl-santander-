import pandas as pd

print("Lendo a planilha...")

try:
    df = pd.read_csv("usuarios_santander.csv")
    print("Planilha carregada com sucesso!")
except:
    print("Erro ao carregar a planilha. Verifique se o arquivo existe.")
    exit()

print("Iniciando transformações...")

df = df.drop_duplicates()
df = df.dropna(how="all")

df["nome"] = df["nome"].fillna("Não informado")
df["email"] = df["email"].fillna("sem_email@santander.com")

df["dominio_email"] = df["email"].apply(lambda x: x.split("@")[-1])

print("Prévia dos dados transformados:")
print(df.head())

print("Salvando arquivo tratado...")

df.to_csv("usuarios_tratados.csv", index=False)

print("ETL finalizado com sucesso!")
