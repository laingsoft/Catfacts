import smtplib, random
def catfacts():
    work=open('catfacts.txt','r')
    lines = work.readlines()
    message = lines[random.randint(0,((len(lines)-1)))]
    vtext = #number goes here
    provider = "telus"
    str.lower(provider)
    if provider == "telus":
        vtext = vtext+'@msg.telus.com'
    elif provider == "rogers":
        vtext = vtext+'@pcs.rogers.com'
    elif provider == "bell":
        vtext = vtext+'@txt.bell.ca'
    elif provider == "fido":
        vtext = vtext+'@sms.fido.ca'
    elif provider == "koodo":
        vtext = vtext+'@msg.telus.com'
    elif provider == "wind":
        vtext = vtext+'@txt.windmobile.ca'

    mailsend(vtext,message)

    

def mailsend(vtext,message):

    username = #email goes here
    password = #password goes here

    #vtext = Email to send it to.
    #message = The message to send.

    msg = """From: {0}
    To: You


    
    {1}
    """ .format (username,message)

    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login(username,password)
    server.sendmail(username, vtext, msg)
    server.quit()
    print 'Done!'
while True:   
    catfacts()
