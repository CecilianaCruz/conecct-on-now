

import paramiko

# Configurações de conexão SSH
hostname = '10.0.19044.2486'  # Substitua pelo endereço IP do computador remoto
port = 22  # Porta SSH padrão
username = 'ceciliana.cruz'
password = 'Ccjbdsac123'

# Inicializar o cliente SSH
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

try:
    # Conectar ao computador remoto
    client.connect(hostname, port, username, password)

    # Comando para iniciar o programa Python
    comando = 'python /home/user/meu_programa.py'  # Substitua pelo caminho do seu programa Python
    stdin, stdout, stderr = client.exec_command(comando)

    # Ler a saída do comando, se necessário
    saida = stdout.read().decode('utf-8')
    erros = stderr.read().decode('utf-8')

    # Exibir resultados, se necessário
    print('Saída:', saida)
    print('Erros:', erros)

finally:
    # Fechar a conexão SSH
    client.close()
