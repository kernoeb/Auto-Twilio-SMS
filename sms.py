#Librairies
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import wikipedia
import math

app = Flask(__name__)

# Vous pouvez modifier "/" en fonction de ce que vous souhaitez
# En supposant qu'un tunnel Serveo est utilisé, le lien à donner sera xxxxxx.serveo.net:12345
# (Le port est modifiable en dernière ligne)
# Dans le cas où vous mettez "/sms", le lien sera xxxxxx.serveo.net/sms:12345
@app.route("/", methods=['GET', 'POST'])
def sms():
    message_body = request.form['Body']
    
    resp = MessagingResponse()
    
    replyText = getReply(message_body)
    resp.message("\n\n" + replyText )
    return str(resp)

#Suppression du début du message
#Exemple: "wiki Paris" devient "Paris"
def removeHead(fromThis, removeThis):
    if fromThis.endswith(removeThis):
        fromThis = fromThis[:-len(removeThis)].strip()
    elif fromThis.startswith(removeThis):
        fromThis = fromThis[len(removeThis):].strip()
    
    return fromThis



def getReply(message):
    
    message = message.lower().strip()
    answer = ""
    
    # Wikipedia
    # Exemple: "wiki Paris" renvoie les 500 premiers caractères (au maximum) du résumé Wikipedia 
    if "wiki" in message:
        wikipedia.set_lang("fr")
        message = removeHead(message, "wiki")
        
        try:
            page = wikipedia.page(message)
            answer = str(page.summary) + "\n\n" + str(page.url)
        except:
            answer = "Cet article n'existe pas..."
            
    # Calculatrice 
    # Exemple: "calc 5*5" renvoie "25"
    elif "calc" in message:
       message = removeHead(message, "calc")
       message = eval(message)
       
       try:
           answer = str(message)
       except:
           answer = "Impossible!"
    
    #else:
    #    answer = "lol"
    
    # Évite les longs messages, et ainsi de "consommer" l'offre gratuite Twilio
    # À commenter/décommenter/modifier selon l'envie.
    if len(answer) > 500:
        answer = answer[0:500] + "..."
    
    return answer

# Port : 12345
# Possibilité d'utiliser un tunnel Serveo ou Ngrok si souhaité
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=12345)
