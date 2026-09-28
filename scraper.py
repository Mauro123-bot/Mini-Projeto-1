import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

print("🤖 Iniciando o robô de raspagem...")

opcoes = webdriver.ChromeOptions()
servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico, options=opcoes)

try:
    url_pesquisa = "https://tse.jus.br" 
    print(f"🌍 Acessando a página: {url_pesquisa}")
    navegador.get(url_pesquisa)
    
    print("⏳ Aguardando o carregamento completo do portal do TSE...")
    time.sleep(5)
    
    try:
        print("🤖 Tentando localizar e clicar no menu de pesquisas registradas...")
        menu_pesquisa = navegador.find_element(By.PARTIAL_LINK_TEXT, "Pesquisa")
        menu_pesquisa.click()
        print("👆 Menu clicado com sucesso!")
        time.sleep(3)
    except Exception as e_clique:
        print(f"⚠️ Nota: Não foi necessário clicar ou o menu mudou de nome: {e_clique}")
    
    html_da_pagina = navegador.page_source
    sopa = BeautifulSoup(html_da_pagina, "html.parser")
    print("✅ Página capturada com sucesso! O robô está pronto para ler os dados.")
    print(f"📌 Título do site acessado: {navegador.title}")

except Exception as e:
    print(f"❌ Ocorreu um erro durante a raspagem: {e}")

finally:
    # navegador.quit() 
    print("🤖 Robô finalizou a execução e manteve o navegador aberto para análise.")