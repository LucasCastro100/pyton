import os
def add_contact():
    name = input("Informe seu nome: ")
    address = input("Informe seu endereço: ") 
    phone = input("Informe seu telefone: ")
    
    contato = f"Nome {name} \nEndereço: {address} \nTelefone: {phone}"
    
    with open("fundamentals/exercises/manipulating_files/dados/contacts.txt", "a", encoding="utf-8") as file:
        file.write(contato)
        
def view_contacts():
    if not os.path.exists("fundamentals/exercises/manipulating_files/dados/contacts.txt"):
        print("Ainda não existem contatos cadastrados.")
        return
    with open("fundamentals/exercises/manipulating_files/dados/contacts.txt", "r", encoding="utf-8") as file:
        contacts = file.read()
    print("Contatos:")
    print(contacts)
       
def delete_contacts():
    if not os.path.exists("fundamentals/exercises/manipulating_files/dados/contacts.txt"):
        print("Ainda não existem contatos cadastrados.")
        return
    with open("fundamentals/exercises/manipulating_files/dados/contacts.txt", "w", encoding="utf-8") as file:
        file.write("")
        
    print("Contatos apagados com sucesso!")
       