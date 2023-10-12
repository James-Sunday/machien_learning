
import requests
import uuid
import azure.cognitiveservices.speech as speechsdk
import sys
sys.path.append('/home/omeife/project/OmeifeNLU/')
updated_key = "fbecaab29ae54bb1873a364df72c4eaa"
from omeifechatbot import chatbot






def NLU(text,name, user_id, age,gender,emotion):

        headers = {
            'accept': 'application/json',
            'Content-Type': 'application/json',
        }

        url = 'http://10.10.40.2:10208/omeife-ai'

        data = {'user_name': name, 'question': text, 'id': user_id, 'age':age, 'gender':gender,'emotion':emotion}

        resp = requests.post(url, headers=headers, json=data)
        return resp.json()

if __name__ == "__main__":
        ai = chatbot(name='omeifae')

        text = ai.recognize_english()
        print (text)

        res = NLU(f"{text}", "kl", "4895694-olop", "23", "gender", "happy")
        # ai.synthesize_english(res)
        
        #print (NLU("Who are you?", "kl", "23", "gender", "happy"))
        print (res)