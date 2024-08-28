
# E-MAIL E SENHA:
e_mail = "goncalvewalter@gmail.com"
senha = "zdlhfb65"

#    Passo a passso do projeto:

#    1. Abrir o sistema da empresa 
    #https://dlp.hashtagtreinamentos.com/python/intensivao/login

# para instalar a biblioteca "pyautogui" digite no cmd do vs code: pip install pyautogui 
import pyautogui
import time 
# pyautogui.click-> clicar como mouse 
# pyautogui.press-> pressionar tecla do teclado
# pyautogui.write-> escrever um texto
# pyautogui.read-> ler um texto 
# pyautogui.hotkey-> apertar um conjunto de teclas 

# abrir o navegador (Chrome)

pyautogui.PAUSE = 1.5

pyautogui.press("win") # pressiona a tecla windows, para acessar todos os progmas do pc!
pyautogui.write("chrome") # digita na barra de procura para encontar o programa!
pyautogui.press("enter") # presssiona a tecla enter para executar o programa!
time.sleep(5) # o programa dorme por 4 segundos para que o programa execute corretamente!
pyautogui.click(x=279, y=822) # clica na aba de visitante, para abrir um site!
# pyautogui.doubleClick(746, 243)



# ENTRAR NO SITE DO SISTEMA  
    # site: "https://dlp.hashtagtreinamentos.com/python/intensivao/login"  
site = "https://dlp.hashtagtreinamentos.com/python/intensivao/login" # vareável para guardar o site   
pyautogui.write(site.lower()) # chamo a biblioteca para o python escrever o que está quardado na vareável!
pyautogui.press("enter")  # logo em seguida, pressiono "enter" para fazer a busca no site!
time.sleep(3)

#    2. Fazer login 
    #blibioteca para fazer um click para um login: pyautogui.click()   
pyautogui.press("tab")
# selecionar o campo de e-mail e escrever o e-mail
pyautogui.write("goncalvewalter@gmail.com")
pyautogui.press("tab")
# depois do tab o paython passa pro campo de senha e escreve sua senha
pyautogui.write("jlk654")
pyautogui.press("tab")
pyautogui.press("enter") # enter para confirmar o login
#time.sleep(2.5)


#    3. Abrir/importar a base de dados do produto para cadastrar 

import pandas as pd


tabela_de_dados = pd.read_csv("produtos.csv")
# print(tabela_de_dados)



#    4. Cadastrar um produto 

for linha in tabela_de_dados.index:

    # clicar no campo do codigo do produto:
    pyautogui.click(x=381, y=257)
    # escreve o codigo do produto
    pyautogui.write(tabela_de_dados.loc[linha, "codigo"]) 
    # passa pro proximo campo
    pyautogui.press("tab")
    # escreve o marca do produto 
    pyautogui.write(tabela_de_dados.loc[linha, "marca"]) 
    # passa pro proximo campo
    pyautogui.press("tab")   
    # escreve o tipo do produto
    pyautogui.write(tabela_de_dados.loc[linha, "tipo"]) 
    # passa pro proximo campo
    pyautogui.press("tab")
    # escreve o categoria do produto
    pyautogui.write(str(tabela_de_dados.loc[linha, "categoria"])) 
    # passa pro proximo campo
    pyautogui.press("tab")
    # escreve o preco do produto
    pyautogui.write(str(tabela_de_dados.loc[linha, "preco_unitario"])) 
    # passa pro proximo campo
    pyautogui.press("tab")
    # escreve o custo do produto
    pyautogui.write(str(tabela_de_dados.loc[linha, "custo"])) 
    # passa pro proximo campo
    pyautogui.press("tab")
    # escreve o obs do produto
    obs = str(tabela_de_dados.loc[linha, "obs"]);
    if obs != "nan":
        pyautogui.write(obs)
    # passa pro proximo campo
    pyautogui.press("tab")
    # apertar o botão enviar
    pyautogui.press("enter")
    # scroll pra parte de cima do site
    pyautogui.scroll(500)

#    5. Repetir issso até acabar a lista de produtos  
