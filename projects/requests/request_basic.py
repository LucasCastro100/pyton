import requests
import json
import os

url_users = 'https://jsonplaceholder.typicode.com/users'
url_posts = 'https://jsonplaceholder.typicode.com/posts'
url_comments = 'https://jsonplaceholder.typicode.com/comments'

base_dir = os.path.dirname(os.path.abspath(__file__))
files_dir = os.path.join(base_dir, 'files')

def get_users():
    response = requests.get(url_users)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code}")
        return None
    
def get_user_by_id(user_id):
    response = requests.get(url_users, params={'id': user_id})
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Erro: {response.status_code}")
        return None
    
def get_posts():
    response = requests.get(url_posts)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code}")
        return None
    
def get_posts_by_user_id(user_id):
    response = requests.get(url_posts, params={'userId': user_id})
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Erro: {response.status_code}")
        return []
    
def get_comments():
    response = requests.get(url_comments)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code}")
        return None    

def get_comments_by_post_id(post_id):
    response = requests.get(url_comments, params={'postId': post_id})
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Erro: {response.status_code}")
        return []
    
def export_to_txt(data, filename):
    os.makedirs(files_dir, exist_ok=True)
    filepath = os.path.join(files_dir, filename)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(json.dumps(data, indent=4, ensure_ascii=False))

    print(f"✅ Exportado para {filepath}\n")
    
def menu():
    while True:
        print("\n====== MENU JSONPLACEHOLDER ======")
        print("1. Listar todos os usuários")
        print("2. Buscar usuário por ID")
        print("3. Listar todos os posts")
        print("4. Buscar posts por ID do usuário")
        print("5. Listar todos os comentários")
        print("6. Buscar comentários por ID do post")
        print("0. Sair")
        choice = input("Escolha uma opção: ")

        if choice == '1':
            users = get_users()
            if users:
                print(json.dumps(users, indent=4))
                export = input("Deseja exportar para .txt? (s/n): ")
                if export.lower() == 's':
                    export_to_txt(users, 'usuarios.txt')

        elif choice == '2':
            user_id = input("Digite o ID do usuário: ")
            user = get_user_by_id(user_id)
            if user:
                print(json.dumps(user, indent=4))
                export = input("Deseja exportar para .txt? (s/n): ")
                if export.lower() == 's':
                    export_to_txt(user, f'usuario_{user_id}.txt')

        elif choice == '3':
            posts = get_posts()
            if posts:
                print(json.dumps(posts, indent=4))
                export = input("Deseja exportar para .txt? (s/n): ")
                if export.lower() == 's':
                    export_to_txt(posts, 'posts.txt')

        elif choice == '4':
            user_id = input("Digite o ID do usuário: ")
            posts = get_posts_by_user_id(user_id)
            if posts:
                print(json.dumps(posts, indent=4))
                export = input("Deseja exportar para .txt? (s/n): ")
                if export.lower() == 's':
                    export_to_txt(posts, f'posts_usuario_{user_id}.txt')

        elif choice == '5':
            comments = get_comments()
            if comments:
                print(json.dumps(comments, indent=4))
                export = input("Deseja exportar para .txt? (s/n): ")
                if export.lower() == 's':
                    export_to_txt(comments, 'comentarios.txt')

        elif choice == '6':
            post_id = input("Digite o ID do post: ")
            comments = get_comments_by_post_id(post_id)
            if comments:
                print(json.dumps(comments, indent=4))
                export = input("Deseja exportar para .txt? (s/n): ")
                if export.lower() == 's':
                    export_to_txt(comments, f'comentarios_post_{post_id}.txt')

        elif choice == '0':
            print("Encerrando o programa...")
            break
        else:
            print("❌ Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()
# Example usage
# users = get_users()
# if users:
#     print("Lista de Usuários:")
#     print(json.dumps(users, indent=4))

# user = get_user_by_id(1)
# if user:
#     print("Usuário com ID 1:")
#     print(json.dumps(user, indent=4))
    
# posts = get_posts()
# if posts:
#     print("Todos os Posts:")
#     print(json.dumps(posts, indent=4))

# posts_user_id = get_posts_by_user_id(1)
# if posts_user_id:
#     print("Posts do Usuário ID 1:")
#     print(json.dumps(posts_user_id, indent=4))

# comments = get_comments()
# if comments:
#     print("Todos os Comentários:")
#     print(json.dumps(comments, indent=4))
    
# comments_post = get_comments_by_post_id(1)
# if comments_post:
#     print("Comentários do Post ID 1:")
#     print(json.dumps(comments_post, indent=4))
