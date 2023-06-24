import imapclient
import pyzmail
import tqdm




imapclient._MAXLINE = 10000000
spam_list = ['Spammer1', 'Spammer2', 'Spammer3']
try:
    server = imapclient.IMAPClient('imap.gmail.com',ssl=True)
except imapclient.socket.gaierror:
    print('No internet connection')
    
server.login('your_gmail_account@gmail.com', 'password') #Please enter your gmail password and you 2 step generated password in google
server.select_folder('INBOX',readonly=False)

uniqy_id = server.search('ALL') #set the limit accourdingly
print('Loading....')
raw_message = server.fetch(uniqy_id,'BODY[]')
print('Start')
for i in tqdm.tqdm(uniqy_id):
    message = pyzmail.PyzMessage.factory(raw_message[i][b'BODY[]'])
    if message.get_addresses('from')[0][0] in spam_list:
        server.move(i,'[Gmail]/Spam')

