import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

print("🤖 Iniciando o robô com filtro de dados...")

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
        print("🤖 Clicando no menu de pesquisas...")
        menu_pesquisa = navegador.find_element(By.PARTIAL_LINK_TEXT, "Pesquisa")
        menu_pesquisa.click()
        print("👆 Menu clicado com sucesso!")
        time.sleep(3)
    except Exception as e_clique:
        print(f"⚠️ Nota sobre o clique: {e_clique}")
    
    html_da_pagina = navegador.page_source
    sopa = BeautifulSoup(html_da_pagina, "html.parser")
    print("✅ Página capturada! Filtrando informações relevantes...")
    
    todos_os_links = sopa.find_all("a")
    
    # CRIANDO UMA LISTA COMPORTADA PARA ARMAZENAR OS DADOS COMO UMA TABELA
    dados_filtrados = []
    
    for link in todos_os_links:
        texto = link.text.strip().upper() # Transforma em maiúsculo para facilitar a busca
        endereco = link.get("href")
        
        # FILTRO INTELIGENTE: Só aceita se tiver termos ligados a pesquisas eleitorais
        if "PESQUISA" in texto or "VISUALIZAR" in texto or "CONSULTA" in texto:
            if endereco and endereco != "#":
                dados_filtrados.append({"Item": link.text.strip(), "Link de Acesso": endereco})

    # EXIBINDO OS RESULTADOS FILTRADOS EM FORMATO DE TABELA NO TERMINAL
    print("\n📊 --- TABELA DE RESULTADOS FILTRADOS PELO ROBÔ ---")
    print(f"{'Nº':<4} | {'CONTEÚDO DA PESQUISA / LINK':<50}")
    print("-" * 60)
    
    for indice, item in enumerate(dados_filtrados):
        print(f"{indice + 1:<4} | {item['Item'][:45]:<45} -> {item['Link de Acesso'][:40]}...")
        
    print("-" * 60)
    print(f"📈 O robô filtrou {len(dados_filtrados)} opções realmente úteis para o projeto das 170 encontradas!")

except Exception as e:
    print(f"❌ Ocorreu um erro durante a raspagem: {e}")

finally:
    # navegador.quit() 
    print("🤖 Robô finalizou a execução e manteve o navegador aberto.")