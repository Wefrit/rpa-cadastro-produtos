import pyautogui
from time import sleep
import pandas as pd

# Passo 1: entrar no site da empresa: https://dlp.hashtagtreinamentos.com/python/intensivao/login
# 1-a) abrir o chrome
def apertar(botao):
    pyautogui.press(botao)
def escrever(msg):
    pyautogui.write(msg)

pyautogui.PAUSE = 0.5
apertar("win")
escrever("chrome")
apertar("enter")
sleep(0.5)

# 1-b) entrar no site
escrever("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
apertar("enter")
sleep(3)

# Passo 2: Fazer login
apertar("tab")
escrever("email@teste.com")
apertar("tab")
escrever("senhaaleatória")
apertar("enter")
sleep(3)
# Passo 3: Importar a base de dados
produtos = pd.read_csv("produtos.csv")

# Passo 4: Cadastrar produto
# 4 -a) Ir para o campo inicial
apertar("tab")
# 4 -b) Cadastrar todos os produtos
for linha in produtos.index:

    # 4 -c) Escrever os dados do primeiro e passar para o próximo
    codigo = produtos.loc[linha,"codigo"]
    escrever(codigo)

    apertar("tab")
    marca = produtos.loc[linha,"marca"]
    escrever(marca)

    apertar("tab")
    tipo = produtos.loc[linha,"tipo"]
    escrever(tipo)

    apertar("tab")
    categoria = str(produtos.loc[linha,"categoria"])
    escrever(categoria)

    apertar("tab")
    preco_unitario = str(produtos.loc[linha,"preco_unitario"])
    escrever(preco_unitario)

    apertar("tab")
    custo = str(produtos.loc[linha,"custo"])
    escrever(custo)

    apertar("tab")
    obs = str(produtos.loc[linha,"obs"])
    if obs != "nan":
        escrever(obs)
    else:
        escrever("")
    # 4 -c) Enviar os dados
    apertar("tab")
    apertar("enter")
    sleep(1)
    pyautogui.click(79,295)
    pyautogui.scroll(100000)
    pyautogui.click(324,368)
