import json
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Carregar os dados do arquivo JSON
with open("dados.json", "r", encoding="utf-8") as file:
    lista_usuarios = json.load(file)

# Configurar o WebDriver
driver = webdriver.Chrome()

# Loop para cadastrar múltiplos usuários
for dados in lista_usuarios:
    driver.get("https://exemplo.com/formulario")  # Volta para o início
    
    time.sleep(3)  # Aguarde carregar
    
    # Preencher o formulário
    driver.find_element(By.NAME, "nome").send_keys(dados["nome"])
    driver.find_element(By.NAME, "email").send_keys(dados["email"])
    driver.find_element(By.NAME, "telefone").send_keys(dados["telefone"])
    
    # Clicar no botão de envio
    botao_cadastrar = driver.find_element(By.ID, "btn-cadastrar")  # Ajuste conforme necessário
    botao_cadastrar.click()
    
    time.sleep(3)  # Pequena pausa entre cadastros

# Fechar o navegador após cadastrar todos
driver.quit()
