import time
import random
from datetime import datetime

G = "\033[92m" 
B = "\033[94m"
Y = "\033[93m"
R = "\033[91m"
W = "\033[0m"

class DecodeLabspprobot:
    def __init__(self):
        self.knowledge_base = {
            "greeting":{
                "keywords":["hi", "hello", "hey", "greetings"],
                "responses":["Hello! How can I assist you today?", "Hi there! What can I do for you?", "Greetings! How may I help you?"]
            },
            "status":{
                "keywords":["how are you", "how's it going",],
                "responses":["Iam just a program", "but Iam functioning as expected!"], 
            },
            "contact":{
                "keywords":["contact", "email", "phone"],
                "responses":["phone: +1-234-567-8901", "email:decodelabs.tech.gmail.com","phone:+91 89330 06408"]
            },
            "ai_logic":{
                "keywords":["ai logic", "how do you work", "explain your logic"],
                "responses":["I use a combination of natural language processing and machine"]
             },
              "thanks":{
                "keywords":["thanks", "thank you", "appreciate it"],
                "responses":["You're welcome!", "No problem!", "Glad I could help!"]
            }        
        }