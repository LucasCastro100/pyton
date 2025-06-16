import os
import pandas as pd
from unidecode import unidecode
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

# Obter o diretório atual do script
current_dir = os.path.dirname(os.path.abspath(__file__))

# Construir o caminho absoluto do arquivo Excel
file_path = os.path.join(current_dir, "espaco_letrado.xlsx")

# Carregar os dados do arquivo Excel
try:
    df = pd.read_excel(file_path)
    # df['RA'] = df['RA'].astype(str).str.replace('\.0$', '', regex=True)     
    df['ALUNO'] = df['ALUNO'].apply(lambda x: unidecode(x).upper())
except FileNotFoundError:
    print("Arquivo não encontrado!")
    df = pd.DataFrame()

driver = webdriver.Chrome()

# Quando a esocla tiver email e senha padrão
email_fixed = ""
pass_fixed = "Inicial@123"

for index, row in df.iloc[0:].iterrows():
    driver.get("https://mundoz.zoom.education/cadastrar")
    
    time.sleep(7)    
    
    # Aqui no link os input não tinham name nem id por isso peguei o placeholder
    driver.find_element(By.XPATH, '//input[@placeholder="Nome"]').send_keys(row["ALUNO"])
    driver.find_element(By.XPATH, '//input[@placeholder="Nickname"]').send_keys(row["USUARIO"])
    driver.find_element(By.XPATH, '//input[@placeholder="Email de contato"]').send_keys(row["EMAIL"])
    driver.find_element(By.XPATH, '//input[@placeholder="Senha"]').send_keys(pass_fixed)
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