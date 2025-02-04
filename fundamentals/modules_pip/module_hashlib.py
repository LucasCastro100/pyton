import hashlib

# LIB PARA CRIPTOGRAFIA

# VERIFICAR OS ALGORITIMOS DISPONIVEIS  
print(hashlib.algorithms_available)

# ALGORITIMOS DISPONIVEIS DE ACORDO COM O SISTEMA OPERACIONAL
print(hashlib.algorithms_guaranteed)


# UTILIZANDO CHAR 256
algorithm = hashlib.sha256()
print(algorithm.digest())

message = "A melhor coisa que eu ja fiz, foi aceitar Jesus!".encode()
algorithm.update(message)
print(algorithm.hexdigest())

# UTILIZANDO O MD5
md5 = hashlib.md5()
md5.update(message)
print(md5.hexdigest())