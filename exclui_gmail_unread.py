import imaplib
from function_credentials import credenciais

imap = imaplib.IMAP4_SSL("imap.gmail.com")
email = credenciais.email
password = credenciais.senha

imap.login(email, password)

imap.select("inbox")

status, messages_id_list = imap.search(None, '(UNSEEN)')

messages = messages_id_list[0].split(b' ')

print("deletando emails !!!!!")

count =1
for mail in messages:
    imap.store(mail, "+FLAGS", "\\Deleted")
    count +=1
print("emails selecionados com sucesso")

imap.expunge()
imap.close()
imap.logout()
print("finalizado com sucesso! emails deletados")
