import os
import pandas as pd
from unidecode import unidecode
from selenium import webdriver
from selenium.webdriver.common.by import By

import time

# Obter o diretório atual do script
current_dir = os.path.dirname(os.path.abspath(__file__))

# Construir o caminho absoluto do arquivo Excel
file_path = os.path.join(current_dir, "nome_tabela.extensao")

# Carregar os dados do arquivo Excel
try:
    df = pd.read_excel(file_path)
    # df['RA'] = df['RA'].astype(str).str.replace('\.0$', '', regex=True)     
    # df['NOME'] = df['NOME'].apply(lambda x: unidecode(x).upper())    
    print(df)
except FileNotFoundError:
    print("Arquivo não encontrado!")
    df = pd.DataFrame()

driver = webdriver.Chrome()

for index, row in df.iloc[0:].iterrows():
    driver.get("url")  # Volta para o início
    
    time.sleep(5)    
      
    driver.find_element(By.XPATH, '//input[@placeholder="Usuário"]').send_keys(row["RA"])    
    driver.find_element(By.XPATH, '//input[@placeholder="Senha"]').send_keys(row["SENHA"])
    time.sleep(5)  
        
    botao_cadastrar = driver.find_element(By.XPATH, '//div[contains(@class, "flex-row-reverse")]//p[text()="Entrar"]/ancestor::button')
    botao_cadastrar.click()
    
    time.sleep(20)  
    
    # # Verificar se o botão "Dispensar Tutorial" existe e clicar nele se existir
    # dispensar_tutorial_elements = driver.find_elements(By.XPATH, '//button[p[text()="Dispensar Tutorial"]]')
    # if dispensar_tutorial_elements:        
    #     dispensar_tutorial = dispensar_tutorial_elements[0]
    #     dispensar_tutorial.click()
    #     time.sleep(5)
      
    
    insert_code = driver.find_element(By.XPATH, '//button[p[text()="Inserir Código"]]')
    insert_code.click()
    time.sleep(5) 
    
    # driver.find_element(By.XPATH, '//input[@placeholder="Digite o código"]').send_keys(row["CODIGO TURMA"])
    # codigo_turma = driver.find_element(By.XPATH, '//button[p[text()="Continuar"]]')
    # codigo_turma.click()    
    # time.sleep(5)
    
    # confirma_codigo_turma = driver.find_element(By.XPATH, '//button[p[text()="Continuar"]]')
    # confirma_codigo_turma.click()
    # time.sleep(15)
    
    if pd.notna(row["CODIGO PEDIDO"]) and row["CODIGO PEDIDO"] != "":
        driver.find_element(By.XPATH, '//input[@placeholder="Digite o código"]').send_keys(row["CODIGO PEDIDO"])         
        codigo_compra = driver.find_element(By.XPATH, '//button[p[text()="Continuar"]]')
        codigo_compra.click()        
        time.sleep(20)
    else:
        driver.execute_script("window.scrollTo(0, 0);")
        driver.execute_script("document.elementFromPoint(0, 0).click();")
        time.sleep(5)
        
        
    svg_element = driver.find_element(By.XPATH, '//img[@src="/assets/images/avatar_1.png"]')
    svg_element.click()
        
    time.sleep(5)
    
    sair = driver.find_element(By.XPATH, '//button[p[text()="Sair"]]')
    sair.click()
    
    time.sleep(5)        
        

# Fechar o navegador após cadastrar todos
driver.quit()