import pandas as pd




def extrair_dados() -> pd.DataFrame:
    data = {
        'nome': ['Alice Hamilton', 'Bob Dolly', 'Charlie Kenedy', 'Rita Smith', 'Kaitlin Klose'],
        'idade': [25, 30, 28, -5, 32],
        'email': ['alice@mail.com', 'bob@mail.com', 'charlie@mail.com', 'rita@mail.com', 'kaitlin@gmail.com'],
        'salario': [50000, 60000, 55000, 45000, 70000, 80000]
    }

    return pd.DataFrame(data)

def transformar_dados(df: pd.DataFrame) -> pd.DataFrame:
    df['idade'] = df['idade'].apply(lambda x: max(x, 0))
    df = df.drop_duplicates()
    return df


def carregar_dados(df: pd.DataFrame):
    print("Carregando dados no banco...")
    print(df)

def run_pipeline():
    df = extrair_dados()
    df = transformar_dados(df)
    carregar_dados(df)

if __name__ == "__main__":
    run_pipeline()
