# Auto-Twilio-SMS
Programme Python pour recevoir automatiquement (et gratuitement*) des SMS via **Twilio**.
Ce programme est capable de réaliser des recherches via **Wikipedia** ou de répondre à de simples calculs.

Le programme de **Lizpetrov** est plus complet, mais je l'ai modifié en fonction de mes besoins!
Thanks so much Lizpetrov <3 
Forked from https://github.com/lizpetrov

## Installation:
1. Créer un compte Twilio
2. Obtenir (gratuitement) un numéro de téléphone
3. Rendez-vous sur la page https://www.twilio.com/console/phone-numbers 
4. Dans la partie "Messaging", "A message comes in", saisissez l'**IP** et le **port** de la machine. *Vous pouvez utiliser un tunnel Serveo.net (https://serveo.net/) ou Ngrok (https://ngrok.com/)*
5. Sur votre machine, installez Python3 (au minimum) https://www.python.org/
6. "pip install -r requirements.txt" *(pour installer les dépendances)*
7. "python3 sms.py"

## Utilisation
Depuis votre téléphone, envoyez simplement au numéro "acheté" les commandes suivantes:
- "wiki Paris" vous renverra:
"Sent from your Twilio trial account - Christophe Martichon, dit Christophe Maé, est un auteur-compositeur-interprète français né le 16 octobre 1975 à Carpentras (Vaucluse). https://fr.wikipedia.org/wiki/Christophe_Maé"

- "calc 14/2" vous renverra:
"Sent from your Twilio trial account - 7.0"


### Plus d'informations:

https://www.twilio.com/blog/2016/09/how-to-receive-and-respond-to-a-text-message-with-python-flask-and-twilio.html

https://www.twilio.com/docs/quickstart/python/devenvironment

https://www.twilio.com/docs/quickstart/python/sms/sending-via-rest

https://www.twilio.com/docs/quickstart/python/sms/hello-monkey


* Twilio dispose d'un système de "Trial". Libre à votre conscience de continuer l'offre (payante) ou de se recréer un compte. Twilio fonctionne très bien, utilisez de façon légale leur service! Merci! N'hésitez pas à améliorer mon programme! :)
