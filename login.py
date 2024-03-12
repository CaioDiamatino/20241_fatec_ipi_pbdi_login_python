import psycopg
print(psycopg)
class Usuario:
  def __init__(self, login, senha):
    self.login = login
    self.senha = senha

#verifica se o usuário recebido existe na base
def existe(usuario):
  #abrir uma conexão com o PostgreSQL
  #obter uma abstração do tipo "cursor"
  #executar um comando sql
  #verificar o resultado
  #devolver True ou False
  with psycopg.connect(
    host="localhost",
    port=5432,
    dbname="2024_fatec_ipi_pbdi_login_python",
    user="postgres",
    password="123456"
  ) as conexao:
    with conexao.cursor() as cursor:
      cursor.execute(
        'SELECT * FROM tb_usuario WHERE login=%s AND senha=%s',
        (usuario.login, usuario.senha)
      )
      result = cursor.fetchone()
      #return #se result for igual a None, devolvo False, senão devolvo True
      #return True if result != None else False
      return result != None
    
def cadastro(usuario):
   with psycopg.connect(
    host="localhost",
    port=5432,
    dbname="2024_fatec_ipi_pbdi_login_python",
    user="postgres",
    password="123456"
  ) as conexao:
    with conexao.cursor() as cursor:
      cursor.execute(
        'INSERT INTO tb_usuario(login, senha) VALUES (%s, %s);',
        (usuario.login, usuario.senha)
      )
      print('Inserção concluida')


def menu():
    texto = '0-Dair\n1-login\n2-logoff\n3-Inserir_login\n'
    #Usuario ainda n existe
    op = int(input(texto))
    while op != 0:

        if op == 1:
            login = input('Digite o login')
            senha = input('Digite a senha')
            usuario = Usuario(login, senha)
            #Expressão condicional (if/else de uma linha só)
            print('Usuario OK' if existe(usuario) else "Usuario NOK")

        elif op == 2:
            usuario = None
            print('Logoff realizado com sucesso')
        elif op == 3:
          login = input('Insira o usuario que deseja cadastrar')
          senha = input('Digite a senha que deseja cadastrar')
          usuario = Usuario(login, senha)
          cadastro(usuario)

        else:
            print('Jovem somente valoentre 0, 1 e 2, pls')
        op = int(input(texto))

menu()
# def teste():
#   print(existe(Usuario('admin', 'admin')))

# teste()