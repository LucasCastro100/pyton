from agenda import add_contact, view_contacts, delete_contacts

def main():
    while True:
        print('Agenda')
        print("1 - Adicionar contato")
        print("2 - Visualizar contatos")
        print("3 - Apagar contatos")
        print("0 - Sair")
        
        option = input("Escolha uma opção: ")
        
        if option == "1":
            add_contact()
        elif option == "2":
            view_contacts()
        elif option == "3":
            delete_contacts()
        elif option == "0":
            break
        else:
            print("Opção inválida!")
            
main()