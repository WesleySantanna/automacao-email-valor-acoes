import pyautogui
import pyperclip
import webbrowser
import time
import yfinance
 

ticker = input ("Digite o código da ação desejada: ")

dados = yfinance.Ticker(ticker).history(start="2020-01-01", end= "2020-12-31")
fechamento = dados.Close

maxima = round(fechamento.max(), 2)
minima = round(fechamento.min(), 2)
valor_medio = round(fechamento.mean(), 2)

destinatario = "emaildeexemplo@gmail.com"
assunto = "Análise de Ações"
mensagem = f"""

Prezado Gestor,
Seguem as análizes solicitadas da ação {ticker}:
Cotação máxima: R${maxima}
Cotação mínima: R${minima}
Valor médio: {valor_medio}

Qualquer dúvida, estou á disposição!

Att. Wesley Santana """

webbrowser.open("www.gmail.com")
time.sleep(3)


pyautogui.PAUSE = 3 

pyautogui.click(x=2019, y=229)

pyperclip.copy(destinatario)
pyautogui.hotkey("ctrl", "v")
pyautogui.hotkey("tab")

pyperclip.copy(mensagem)
pyautogui.hotkey("ctrl", "v")

pyautogui.click(x=3075, y=1036)

pyautogui.click("ctrl" , "f4")

print("Email enviado com sucesso!")