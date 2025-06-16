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
file_path = os.path.join(current_dir, "files/data_users_ebd.xlsx")

try:
    df = pd.read_excel(file_path)   
except FileNotFoundError:
    print("Arquivo não encontrado!")
    df = pd.DataFrame()
    
# Configurar o modo invisível (headless)
chrome_options = Options()
# chrome_options.add_argument("--headless")  # Roda sem abrir a janela
chrome_options.add_argument("--window-size=1920x1080")
driver = webdriver.Chrome(options=chrome_options)

for index, row in df.iloc[0:].iterrows():
    driver.get("https://www.igrejacristamaranata.org.br/ebd/participacoes/")
    
    wait = WebDriverWait(driver, 10)

    # CPF
    cpf_field = wait.until(EC.presence_of_element_located((By.NAME, "icm_member_cpf")))
    cpf_field.send_keys(str(row["CPF"]))
    
    time.sleep(3)

   # FUNCAO (Select 1)
    if pd.notna(row["FUNCAO"]):
        selects = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "selectize-input")))
        select1 = selects[2]
        wait.until(EC.element_to_be_clickable(select1))
        select1.click()
        
        dropdowns = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".selectize-dropdown")))
        dropdown1 = dropdowns[0]  # Primeiro dropdown após clicar select1
        
        options1 = dropdown1.find_elements(By.CSS_SELECTOR, "div.option")
        for opt in options1:
            if opt.get_attribute("data-value") == str(row["FUNCAO"]):
                wait.until(EC.element_to_be_clickable(opt))
                opt.click()
                break

    # TRABALHO (Select 2)
    if pd.notna(row["TRABALHO"]):
        selects = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "selectize-input")))
        select2 = selects[3]
        wait.until(EC.element_to_be_clickable(select2))
        select2.click()
        
        dropdowns = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".selectize-dropdown")))
        dropdown2 = dropdowns[1]  # Segundo dropdown após clicar select2
        
        options2 = dropdown2.find_elements(By.CSS_SELECTOR, "div.option")
        for opt in options2:
            if opt.get_attribute("data-value") == str(row["TRABALHO"]):
                wait.until(EC.element_to_be_clickable(opt))
                opt.click()
                break
    
    time.sleep(3)
    # Radio botão fixo
    radio = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[name="icm_member_categoria"][value="2"]')))
    radio.click()

    # Checkbox
    checkbox = wait.until(EC.element_to_be_clickable((By.ID, "aceitoOsTermos")))
    if not checkbox.is_selected():
        checkbox.click()

    # Mensagem
    if pd.notna(row["PARTICIPACAO"]):
        mensagem = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@placeholder="Digite sua mensagem"]')))
        mensagem.click()
        mensagem.send_keys(str(row["PARTICIPACAO"]))

driver.quit()