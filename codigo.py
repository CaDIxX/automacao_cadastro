import pyautogui as gui
import time
import pandas
# pyautogui.click -> clica
# pyautogui.write -> escreve
# pyautogui.press -> aperta uma tecla
# pyautogui.hotkey -> aperta um atalho
# pyautogui.scroll -> scrollar a tela


gui.PAUSE = 0.5
link = 'https://dlp.hashtagtreinamentos.com/python/intensivao/login'

# Passo 1: Entrar no sistema
gui.press('win')
time.sleep(2)
gui.write('Vivaldi')
gui.press('enter')
time.sleep(3)

# Acessar o link (navegação por abas depende do browser, ajuste se necessário)
for _ in range(4):
    gui.press('tab')

gui.write(link)
gui.press('enter')
time.sleep(3)

# Passo 2: Fazer login
gui.click(x=2833, y=433) # Coordenada do campo de email
gui.write('um_email_qualquer@dominio.com')
gui.press('tab')
gui.write('sua_senha_segura')
gui.press('tab')
gui.press('enter')
time.sleep(3)

# Passo 3: Abrir a Base de Dados
tabela = pandas.read_csv('produtos.csv',
                        sep=',', 
                        encoding='cp860', 
                        engine='python')

# Passo 4 e 5: Cadastrar produtos
for linha in tabela.index:

    gui.click(x=2876, y=302)
    
    # Preencher campos da tabela
    gui.write(str(tabela.loc[linha, 'codigo']))
    gui.press('tab')
    
    gui.write(str(tabela.loc[linha, 'marca']))
    gui.press('tab')
    
    gui.write(str(tabela.loc[linha, 'tipo']))
    gui.press('tab')
    
    gui.write(str(tabela.loc[linha, 'categoria']))
    gui.press('tab')
    
    gui.write(str(tabela.loc[linha, 'preco_unitario']))
    gui.press('tab')
    
    gui.write(str(tabela.loc[linha, 'custo']))
    gui.press('tab')
    
    # Obs (se não estiver vazio)
    obs = str(tabela.loc[linha, 'obs'])
    if obs != 'nan':
        gui.write(obs)
    
    # Enviar e resetar posição
    gui.press('tab')
    gui.press('enter')
    gui.scroll(5000)
    time.sleep(1)