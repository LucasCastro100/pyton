import os
import pandas as pd
from unidecode import unidecode
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

# Obter o diretório atual do script
current_dir = os.path.dirname(os.path.abspath(__file__))

# Construir o caminho absoluto do arquivo Excel
file_path = os.path.join(current_dir, "nome_tabela.extensão")

# Carregar os dados do arquivo Excel
try:
    df = pd.read_excel(file_path)
    df['RA'] = df['RA'].astype(str).str.replace('\.0$', '', regex=True)     
    df['NOME'] = df['NOME'].apply(lambda x: unidecode(x).upper())
except FileNotFoundError:
    print("Arquivo não encontrado!")
    df = pd.DataFrame()

driver = webdriver.Chrome()

for index, row in df.iloc[0:].iterrows():
    driver.get("url")
    
    time.sleep(7)    
    
    # Aqui no link os input não tinham name nem id por isso peguei o placeholder
    driver.find_element(By.XPATH, '//input[@placeholder="Nome"]').send_keys(row["NOME"])
    driver.find_element(By.XPATH, '//input[@placeholder="Nickname"]').send_keys(row["RA"])
    driver.find_element(By.XPATH, '//input[@placeholder="Email de contato"]').send_keys(row["EMAIL"])
    driver.find_element(By.XPATH, '//input[@placeholder="Senha"]').send_keys(row["SENHA"])
    time.sleep(2)  
    
    elemento_body = driver.find_element(By.TAG_NAME, "body")
    ActionChains(driver).move_to_element(elemento_body).click().perform()
    time.sleep(2)

    driver.find_element(By.XPATH, '//input[@type="checkbox"]').click()

    # Clicar no botão dentro da classe flex-row-reverse que contém um p com o texto "Cadastrar-se"
    botao_cadastrar = driver.find_element(By.XPATH, '//div[contains(@class, "flex-row-reverse")]//p[text()="Cadastrar-se"]/ancestor::button')
    botao_cadastrar.click()
    
    time.sleep(5)  
driver.quit()