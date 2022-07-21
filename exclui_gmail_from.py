import imaplib
from function_credentials import credenciais

# configurando acesso IMAP
imap = imaplib.IMAP4_SSL("imap.gmail.com")

#incluindo seu email e senha que está na classe MinhasCredenciais
e_mail = credenciais.email
password = credenciais.senha

#login
imap.login(e_mail, password)

#selecionando caixa de entrada INBOX, pode substituir por SPAM ou qualquer outra.
imap.select("inbox")

#informando qual remetente de email quer excluir todas as mensagens
status, messages_id_list = imap.search(None, 'FROM "noreply@bluefitacademias.com.br"')

messages = messages_id_list[0].split(b' ')

print("deletanto emails !!!!!")

#função que seleciona os emails para serem deletado
count =1
for mail in messages:
    imap.store(mail, "+FLAGS", "\\Deleted")
    count +=1
print("emails selecionados com sucesso")

# deletando, fechando e saindo da conta
imap.expunge()
imap.close()
imap.logout()
print("finalizado com sucesso! emails deletados")
