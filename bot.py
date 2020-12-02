#from telegram.messageentity import MessageEntity

#from final import ajio_care as care

import final
#import telegram
#bot = telegram.Bot(token='1471624452:AAEPVzcP48Xjq6Kvr7mfV6BTFVMGJKZYqdQ')

#print(care.find_stock('https://www.ajio.com/teamspirit-mid-rise-joggers-with-contrast-stripes/p/440781271_charcoal',2))


#updates = bot.get_updates()


#read a message
def care(message):
    """
    docstring
    """
    #message= mess.text
    #print(message)
    #print(type(message))
    query= str(message).split(',')
    print(query)
    if(len(query)==2):
        #print(eval(query[1]))
        return final.ajio_care.find_stock(eval(query[0]),eval(query[1]))
    
''' 
for u in updates:
    message= u.message.text
    #print(message)
    #print(type(message))
    query= str(message).split(' , ')
    print(query)
    if(len(query)==2):
        #print(eval(query[1]))
        u.message.reply_text(care.find_stock(eval(query[0]),eval(query[1])))

'''
