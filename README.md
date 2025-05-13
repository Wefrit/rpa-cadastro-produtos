# Automação de Cadastro de Produtos com PyAutoGUI 🖱️📋

Este projeto é uma automação feita com Python que preenche automaticamente um formulário de cadastro de produtos no navegador, usando a biblioteca `pyautogui`.

## 💡 Funcionalidades

- Abre o navegador e acessa um site de exemplo
- Faz login automaticamente
- Lê os dados de produtos de um arquivo CSV
- Preenche e envia o formulário com os dados de cada produto

## 📁 Requisitos

- Python 3.x
- Bibliotecas:
  - `pyautogui`
  - `pandas`

## ▶️ Como usar

1. Instale as dependências:
  ```bash
pip install pyautogui pandas
```

2. Execute o script:
   Para rodar o script, execute o seguinte comando no terminal ou prompt de comando:
```bash
 python projeto_1.py
 ```

⚠️ Certifique-se de que o navegador está visível e que a resolução da tela está compatível com os cliques automatizados.

## 📄 Dados de exemplo

Os dados devem estar em um arquivo `produtos.csv`, com colunas como:
- `codigo`
- `marca`
- `tipo`
- `categoria`
- `preco_unitario`
- `custo`
- `obs`

---

Feito com Python por Nathan Lopes

