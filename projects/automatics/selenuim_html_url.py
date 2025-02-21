import json
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

# Carregar os dados do arquivo JSON caso ele exista
try:
    with open("alunos.json", "r", encoding="utf-8") as file:
        lista_usuarios = json.load(file)
except FileNotFoundError:
    print("Arquivo não encontrado!")
    lista_usuarios = []

# Configurar o WebDriver
driver = webdriver.Chrome()

# Loop para cadastrar múltiplos usuários
for dados in lista_usuarios:
    driver.get("https://www.google.com/")  # Volta para o início
    
    time.sleep(7)      
    # Preencher o formulário de duas formas com class, id, ou tag
    # driver.find_element(By.NAME, "nome").send_keys(dados["nome"])
    # driver.find_element(By.NAME, "nickname").send_keys(dados["nickname"])
    # driver.find_element(By.NAME, "email").send_keys(dados["email"])
    # driver.find_element(By.NAME, "telefone").send_keys(dados["telefone"])
    
    #aqui no link os input nao tinham name nem id por isos peguei o placeholder
    driver.find_element(By.XPATH, '//input[@placeholder="Nome"]').send_keys(dados["nome"])
    driver.find_element(By.XPATH, '//input[@placeholder="Nickname"]').send_keys(dados["nickname"])
    driver.find_element(By.XPATH, '//input[@placeholder="Email de contato"]').send_keys(dados["email"])
    driver.find_element(By.XPATH, '//input[@placeholder="Senha"]').send_keys(dados["pass"])
    time.sleep(2)  
    
    # Encontrar o elemento body e  Clicar no body para "fechar" os checkboxes
    elemento_body = driver.find_element(By.TAG_NAME, "body")
    ActionChains(driver).move_to_element(elemento_body).click().perform()
    time.sleep(2)

    driver.find_element(By.XPATH, '//input[@type="checkbox"]').click()

    # Clicar no botão de envio -> comentado apra nao enviar apra o banco de dados
    # botao_cadastrar = driver.find_element(By.ID, "btn-cadastrar")  # Ajuste conforme necessário
    # botao_cadastrar.click()
    
    time.sleep(5)  # Pequena pausa entre cadastros

# Fechar o navegador após cadastrar todos
driver.quit()
