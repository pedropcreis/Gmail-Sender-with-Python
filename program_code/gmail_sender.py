import smtplib

print("-" * 10, " Email Sender ", "-" * 10)
print('''Antes de prosseguir, certifique-se que nas configurações de sua conta Gmail, a opção 'Acesso a app menos seguro' esteja ativada e que você\nesteja conectado à internet.
Após preencher os dados, verifique se você digitou seu endereço de email e senha corretamente.
''')

sender = input("Informe seu gmail: ").strip()
password = input("Informe sua senha: ")
question = "SIM"
while question in ["S", "SIM"]:
    receiver = input("Informe o gmail do destinatário: ").strip()
    msgSub = input("Assunto (título): ")
    message = input("Escreva a mensagem que deseja enviar: ")

    try:
        domain = smtplib.SMTP('smtp.gmail.com', 587)    #inicia uma conexão SMTP
        domain.starttls()  #criptografa a conexão em TLS
        domain.login(sender, password)  #faz login no servidor SMTP
        domain.sendmail(sender, receiver, f"Subject: {msgSub}\n{message}")  #envia o email
        domain.quit()  #encerra a conexão
        print("Seu email foi enviado com sucesso!")
        question = input("Deseja enviar mais um email? ").upper().strip()

        while question not in ["S", "SIM", "N", "NÃO", "NAO"]:   #tratando respostas inválidas
            print("Resposta inválida! Responda com 'sim' ou 'não'.")
            question = input("Deseja enviar mais um email? ").upper().strip()
    except:
        print("Ocorreu um erro. Verifique se você preencheu os dados corretamente e ativou o acesso a app menos seguro, depois reinicie o programa.")
        break
print("-" * 10, " Programa encerrado ", "-" * 10)