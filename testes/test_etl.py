import os
import sys
import pandas as pd

# 👉 adiciona a pasta raiz do projeto no PYTHONPATH
sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..")
    )
)

from etl_pipeline import extrair_dados, transformar_dados


def test_extracao():
    df = extrair_dados()
    assert not df.empty
    assert all(col in df.columns for col in ['nome', 'idade', 'email', 'salario'])


def test_transformacao():
    df = pd.DataFrame({'idade': [10, -5, 20]})
    df_tratado = transformar_dados(df)
    assert (df_tratado['idade'] >= 0).all()
