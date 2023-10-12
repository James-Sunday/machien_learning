import os
import time
import datetime
import numpy as np
#from actions import *
import os
import azure.cognitiveservices.speech as speechsdk
import requests, uuid, json
import sys
sys.path.append('/home/omeife/Desktop/nobita')


updated_key = "fbecaab29ae54bb1873a364df72c4eaa"
mr_adams_key = "9e9f9a25b13049ea845b17fa46936d1b"
mr_bello_key = "607e1f6bdb8a467688f77a26bd7f0292"

#action = Actions()

def reverse(text):
    x = ""
    for i in text:
        x = i + x
    
    return x

class chatbot():
    def __init__(self,name):
        print("---starting up---",name,"---")
        self.name=name
        self.text=''
        self.role = "You are an intelligent assistant. your name is omeife, you are an AI developed in Africa, you are built at stem focus in Nigeria, you like to chat with humans and also you like to learn more about african culture and people, your name means one that does wonder, one that does great things. you can raise up your hand, you have a physical body, you can do basic body movements"
        #self.pigin_recognizer = PiginModel('JasperModelPigin.nemo')


    def recognize_arabic(self):

        # This example requires environment variables named "SPEECH_KEY" and "SPEECH_REGION"
        speech_config = speechsdk.SpeechConfig(subscription="9df5d87ee40e41339f9af788b1666913", region="eastus")
        speech_config.speech_recognition_language="ar-SA"

        audio_config = speechsdk.audio.AudioConfig(use_default_microphone=True)
        speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)

        print("Speak into your microphone.")
        speech_recognition_result = speech_recognizer.recognize_once_async().get()

        if speech_recognition_result.reason == speechsdk.ResultReason.RecognizedSpeech:
            print("Recognized: {}".format(reverse(speech_recognition_result.text)))
            self.text = speech_recognition_result.text

        elif speech_recognition_result.reason == speechsdk.ResultReason.NoMatch:
            print("No speech could be recognized: {}".format(speech_recognition_result.no_match_details))
            self.text = "ERROR"
        elif speech_recognition_result.reason == speechsdk.ResultReason.Canceled:
            cancellation_details = speech_recognition_result.cancellation_details
            print("Speech Recognition canceled: {}".format(cancellation_details.reason))
            self.text = "ERROR"
            if cancellation_details.reason == speechsdk.CancellationReason.Error:
                print("Error details: {}".format(cancellation_details.error_details))
                print("Did you set the speech resource key and region values?")


    def recognize_english(self):
    # This example requires environment variables named "SPEECH_KEY" and "SPEECH_REGION"
        speech_config = speechsdk.SpeechConfig(subscription=updated_key,region="eastus")
        speech_config.speech_recognition_language="en-US"

        audio_config = speechsdk.audio.AudioConfig(use_default_microphone=True)
        speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)

        print("Speak into your microphone.")
        speech_recognition_result = speech_recognizer.recognize_once_async().get()

        if speech_recognition_result.reason == speechsdk.ResultReason.RecognizedSpeech:
            print("Recognized: {}".format(speech_recognition_result.text))
            self.text = speech_recognition_result.text

        elif speech_recognition_result.reason == speechsdk.ResultReason.NoMatch:
            print("No speech could be recognized: {}".format(speech_recognition_result.no_match_details))
            self.text = "ERROR"
        elif speech_recognition_result.reason == speechsdk.ResultReason.Canceled:
            cancellation_details = speech_recognition_result.cancellation_details
            print("Speech Recognition canceled: {}".format(cancellation_details.reason))
            self.text = "ERROR"
            if cancellation_details.reason == speechsdk.CancellationReason.Error:
                print("Error details: {}".format(cancellation_details.error_details))
                print("Did you set the speech resource key and region values?")

    def recognize_french(self):
    # This example requires environment variables named "SPEECH_KEY" and "SPEECH_REGION"
        speech_config = speechsdk.SpeechConfig(subscription="9df5d87ee40e41339f9af788b1666913",region="eastus")
        speech_config.speech_recognition_language="fr-FR"

        audio_config = speechsdk.audio.AudioConfig(use_default_microphone=True)
        speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)

        print("Speak into your microphone.")
        speech_recognition_result = speech_recognizer.recognize_once_async().get()

        if speech_recognition_result.reason == speechsdk.ResultReason.RecognizedSpeech:
            print("Recognized: {}".format(speech_recognition_result.text))
            self.text = speech_recognition_result.text

        elif speech_recognition_result.reason == speechsdk.ResultReason.NoMatch:
            print("No speech could be recognized: {}".format(speech_recognition_result.no_match_details))
            self.text = "ERROR"
        elif speech_recognition_result.reason == speechsdk.ResultReason.Canceled:
            cancellation_details = speech_recognition_result.cancellation_details
            print("Speech Recognition canceled: {}".format(cancellation_details.reason))
            self.text = "ERROR"
            if cancellation_details.reason == speechsdk.CancellationReason.Error:
                print("Error details: {}".format(cancellation_details.error_details))
                print("Did you set the speech resource key and region values?")
   
    
    def synthesize_french(self,text):

        # This example requires environment variables named "SPEECH_KEY" and "SPEECH_REGION"
        speech_config = speechsdk.SpeechConfig(subscription="9df5d87ee40e41339f9af788b1666913", region="eastus")
        audio_config = speechsdk.audio.AudioOutputConfig(use_default_speaker=True)
    
        # The language of the voice that speaks.
        speech_config.speech_synthesis_voice_name='fr-FR-BrigitteNeural'

        speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)

        # Get text from the console and synthesize to the default speaker.

        speech_synthesis_result = speech_synthesizer.speak_text_async(text).get()

        if speech_synthesis_result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
            print("Speech synthesized for text [{}]".format(text))
        elif speech_synthesis_result.reason == speechsdk.ResultReason.Canceled:
            cancellation_details = speech_synthesis_result.cancellation_details
            print("Speech synthesis canceled: {}".format(cancellation_details.reason))
            if cancellation_details.reason == speechsdk.CancellationReason.Error:
                if cancellation_details.error_details:
                    print("Error details: {}".format(cancellation_details.error_details))
                    print("Did you set the speech resource key and region values?")
                    
    

    def recognize_pigin(self):
        self.text = self.pigin_recognizer.listen()    
    
    
    
    def synthesize_english(self,text):

        # This example requires environment variables named "SPEECH_KEY" and "SPEECH_REGION"
        speech_config = speechsdk.SpeechConfig(subscription=updated_key, region="eastus")
        audio_config = speechsdk.audio.AudioOutputConfig(use_default_speaker=True)
    
        # The language of the voice that speaks.
        speech_config.speech_synthesis_voice_name='en-NG-EzinneNeural'

        speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)

        # Get text from the console and synthesize to the default speaker.

        speech_synthesis_result = speech_synthesizer.speak_text_async(text).get()

        if speech_synthesis_result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
            print("Speech synthesized for text [{}]".format(text))
        elif speech_synthesis_result.reason == speechsdk.ResultReason.Canceled:
            cancellation_details = speech_synthesis_result.cancellation_details
            print("Speech synthesis canceled: {}".format(cancellation_details.reason))
            if cancellation_details.reason == speechsdk.CancellationReason.Error:
                if cancellation_details.error_details:
                    print("Error details: {}".format(cancellation_details.error_details))
                    print("Did you set the speech resource key and region values?")
    
    def NLU(self,role,text,name):
        url = 'http://10.10.40.2:10204/query'
        data = {'role':role,'text':text,'name':name}
        resp = requests.post(url,json=data)
        return resp.json()

    def intents(self,text):
        url = 'http://10.10.40.2:10205/predict'
        data = {'text':text}
        resp = requests.post(url,json=data)
        return resp.json()

    def synthesize_arabic(self,text):

        # This example requires environment variables named "SPEECH_KEY" and "SPEECH_REGION"
        speech_config = speechsdk.SpeechConfig(subscription="9df5d87ee40e41339f9af788b1666913", region="eastus")
        audio_config = speechsdk.audio.AudioOutputConfig(use_default_speaker=True)
    
        # The language of the voice that speaks.
        speech_config.speech_synthesis_voice_name='ar-KW-NouraNeural'

        speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)

        # Get text from the console and synthesize to the default speaker.

        speech_synthesis_result = speech_synthesizer.speak_text_async(text).get()

        if speech_synthesis_result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
            print("Speech synthesized for text [{}]".format(text))
        elif speech_synthesis_result.reason == speechsdk.ResultReason.Canceled:
            cancellation_details = speech_synthesis_result.cancellation_details
            print("Speech synthesis canceled: {}".format(cancellation_details.reason))
            if cancellation_details.reason == speechsdk.CancellationReason.Error:
                if cancellation_details.error_details:
                    print("Error details: {}".format(cancellation_details.error_details))
                    print("Did you set the speech resource key and region values?")
    
    def synthesize_pigin(self,text):
        self.synthesize_pigin(text)
    
    
    def translate(self,text,from_='en',to_='ar'):
        # Add your key and endpoint
        key = "9df5d87ee40e41339f9af788b1666913"

        endpoint = "https://api.cognitive.microsofttranslator.com"

        # location, also known as region.
        # required if you're using a multi-service or regional (not global) resource. It can be found in the Azure portal on the Keys and Endpoint page.
        location = "eastus"

        path = '/translate'
        constructed_url = endpoint + path

        params = {
           'api-version': '3.0',
           'from': from_,
           'to': to_
        }

        headers = {
            'Ocp-Apim-Subscription-Key': key,
            # location required if you're using a multi-service or regional (not global) resource.
            'Ocp-Apim-Subscription-Region': location,
            'Content-type': 'application/json',
            'X-ClientTraceId': str(uuid.uuid4())
        }

        # You can pass more than one object in body.
        body = [{
            'text': text
        }]

        request = requests.post(constructed_url, params=params, headers=headers, json=body)
        response = request.json()
    
        return response[0]['translations'][0]['text']
    
    def translate_pigin(self,text,from_='english',to_='pidgin'):
        output = translate_pigin(text,from_,to_)
        return output
    
    def wake_up(self,text):
        print(text)
        return True if "hey "+ self.name in text.lower() else False

    

    def action_time(self):
        return datetime.datetime.now().time().strftime('%H:%M')

def take_action(text):
    if text == 'Handshakes':
        print("shake hand ")
        thand=thandshake()
        return thand
    elif text == 'Raise right hand':
        traishand = tleft()
        return traishand
    elif text == 'Raise left hand':
        traiseleft=tleft()
        return traiseleft
    else:
        return None
     
def open_file(file_path):
    with open(file_path,'r') as f:
        out = f.read()
    return out


def talk_english(file_path):
    ai = chatbot(name='omeifae')
    ex = True
    history = []
    possible_switch = ['swahili','arabic','pigin','french']
    while ex:
        updated_name = open_file(file_path)
        

        print(updated_name)
        role = """
                your an intelligent AI chatbot, you are conversating with {} you can see physically from the visual representation of person given to you.

                visual representations of person:

                \n\n
                face facial emotion: happy,
                name of the person: {},
                \n\n

                you can only tell if a person is happy, sad, angry, and neutral. otherwise you can respond politely. you can also show empathy and bring out conversations to help improve the person mood.
                your name is omeifae, you are developed at stemfocus lab nigeria,you like to learn more about african people and culture, you can speak 4 language, English, Pidgin, arabic, and swahili.
                """.format(updated_name,updated_name)

        print("Name of person: ",updated_name)

        ai.recognize_english()
        if ai.wake_up(ai.text) is True:
            res = "hello, i am omeifaeh, how can i help you?" 
        
        #check if it's asking time
        elif "time" in ai.text:
            res = ai.action_time()
            
        
        #check if it's saying thanks
        elif any(i in ai.text for i in ["thank","thanks"]):
            res = np.random.choice(["you're welcome!","anytime!",
            "no problem!","cool!","I'm here if you need me","no problem"])
        
        elif any(i in ai.text for i in ["exit","close"]):
            res = np.random.choice(["have a good day","Bye","Goodbye","Hope to meet soon"])
            ex=True

         ## conversation
        else:
            check_for_switch = ai.intents(ai.text)
            if ai.text=="ERROR":
                res="Error, I'm having problem connecting to my server. please can you re-state what you said?"
            
            
            elif check_for_switch in possible_switch:
                ai.synthesize_english("switching to {}...".format(check_for_switch))
                return check_for_switch

            else:
                res = ai.NLU(role,ai.text,updated_name)['text']
                
            ai.synthesize_english(res)

                   
    print("Closing omeifeh")


def talk_arabic(client):
    ai = chatbot(name='omeifae')
    ex = True
    history = []
    possible_switch = ['english','swahili','pigin','french']
    contexts = "your an AI, your name is omeifeah, you like to chat with human,your name means one that does wonder, one that does great things.\
                your the first AI developed in Africa, your build at stem focus lab in Nigeria, you like to learn about african culture and people, you can raise up your hand, you have a physical body, toda's date is 6th of december 2022, you were officially launched at transcorp hilton abuja on 2nd of december 2022"

    while ex:
        ai.recognize_arabic()

        if ai.text != "ERROR":
           ai.text = ai.translate(ai.text,from_='ar',to_='en')

        if ai.wake_up(ai.text) is True:
            res = "hello, i am omeifaeh, how can i help you?"

        #check if it's asking time
        elif "time" in ai.text:
            res = ai.action_time()
        
        #check if it's saying thanks
        elif any(i in ai.text for i in ["thank","thanks"]):
            res = np.random.choice(["you're welcome!","anytime!",
            "no problem!","cool!","I'm here if you need me","no problem"])
        
        elif any(i in ai.text for i in ["exit","close"]):
            res = np.random.choice(["have a good day","Bye","Goodbye","Hope to meet soon"])
            ex=False

        
         ## conversation
        else:
            check_for_switch = predict_intent_for_switch(switch_model,ai.text)
            if ai.text=="ERROR":
                res="Sorry, but i'm not able to understand what you mean, can you restate your question"

            elif check_for_switch in possible_switch:
                res = ai.translate("switching to {}".format(check_for_switch),from_='en',to_='ar')
                ai.sythesize_arabic(res)
                return check_for_switch

            else:
                history = trim_history(history,6)
                res,history = chat_gptj(client,ai.text,contexts,history)
                res = ai.translate(res,from_='en',to_='ar')
                
        ai.synthesize_arabic(res)
    
    print("Closing omeifeh")


def talk_swahili(client):
    ai = chatbot(name='omeifae')
    ex = True
    history = []
    
    possible_switch = ['english','arabic','pigin','french']
    name = "something to get names of people"
    contexts = "your an AI, your conversating with {}, your name is omeifeah, you like to chat with human,your name means one that does wonder, one that does great things.\
                your the first AI developed in Africa, your build at stem focus lab in Nigeria, you like to learn more about african culture and people".format(name)

    while ex:
        ai.recognize_swahili()

        if ai.text != "ERROR":
           ai.text = ai.translate(ai.text,from_='sw',to_='en')

        if ai.wake_up(ai.text) is True:
            res = "hello, i am omeifaeh, how can i help you?" 

        #check if it's asking time
        elif "time" in ai.text:
            res = ai.action_time()
        
        #check if it's saying thanks
        elif any(i in ai.text for i in ["thank","thanks"]):
            res = np.random.choice(["you're welcome!","anytime!",
            "no problem!","cool!","I'm here if you need me","no problem"])
        
        elif any(i in ai.text for i in ["exit","close"]):
            res = np.random.choice(["have a good day","Bye","Goodbye","Hope to meet soon"])
            ex=False

        
         ## conversation
        else:
            check_for_switch = predict_intent_for_switch(switch_model,ai.text)
            if ai.text=="ERROR":
                res="Sorry, but i'm not able to understand what you mean, can you restate your question"

            elif check_for_switch in possible_switch:
                ai.synthesize(ai.translate("switching to {}".format(check_for_switch),from_='en',to_='sw'))
                return check_for_switch

            else:
                history = trim_history(history,6)
                res,history = chat_gptj(client,ai.text,contexts,history)
                res = ai.translate(res,from_='en',to_='sw')
                
        ai.synthesize_arabic(res)
    
    print("Closing omeifeh")

def talk_french(client):
    ai = chatbot(name='omeifae')
    ex = True
    history = []
    
    possible_switch = ['english','arabic','pigin','swahili']

    name = "something to get names of people"
    contexts = "your an AI, your conversating with {}, your name is omeifeah, you like to chat with human,your name means one that does wonder, one that does great things.\
                your the first AI developed in Africa, your build at stem focus lab in Nigeria, you like to learn more about african culture and people".format(name)

    while ex:
        ai.recognize_french()

        if ai.text != "ERROR":
           ai.text = ai.translate(ai.text,from_='fr',to_='en')

        if ai.wake_up(ai.text) is True:
            res = "hello, i am omeifaeh, how can i help you?" 

        #check if it's asking time
        elif "time" in ai.text:
            res = ai.action_time()
        
        #check if it's saying thanks
        elif any(i in ai.text for i in ["thank","thanks"]):
            res = np.random.choice(["you're welcome!","anytime!",
            "no problem!","cool!","I'm here if you need me","no problem"])
        
        elif any(i in ai.text for i in ["exit","close"]):
            res = np.random.choice(["have a good day","Bye","Goodbye","Hope to meet soon"])
            ex=False

        
         ## conversation
        else:
            check_for_switch = predict_intent_for_switch(switch_model,ai.text)
            if ai.text=="ERROR":
                res="Sorry, but i'm not able to understand what you mean, can you restate your question"

            elif check_for_switch in possible_switch:
                ai.synthesize(ai.translate("switching to {}".format(check_for_switch),from_='en',to_='sw'))
                return check_for_switch

            else:
                history = trim_history(history,6)
                res,history = chat_gptj(client,ai.text,contexts,history)
                res = ai.translate(res,from_='en',to_='fr')
                
        ai.synthesize_french(res)
    
    print("Closing omeifeh")


def talk_pigin(client):

    ai = chatbot(name='omeifae')
    ex = True
    history = []
    possible_switch = ['english','arabic','swahili']
    name = "something to get names of people"
    contexts = "your an AI, your conversating with {}, your name is omeifeah, you like to chat with human,your name means one that does wonder, one that does great things.\
                your the first AI developed in Africa, your build at stem focus lab in Nigeria, you like to learn more about african culture and people".format(name)

    while ex:

        ai.recognize_pigin()
        
        if ai.text != "None":
           ai.text = translate_pigin(ai.text,from_='pigin',to_='english')['target ']

        if ai.wake_up(ai.text) is True:
            res = "hello, i am omeifaeh, how can i help you?" 

        #check if it's asking time
        elif "time" in ai.text:
            res = ai.action_time()
        
        #check if it's saying thanks
        elif any(i in ai.text for i in ["thank","thanks"]):
            res = np.random.choice(["you're welcome!","anytime!",
            "no problem!","cool!","I'm here if you need me","no problem"])
        
        elif any(i in ai.text for i in ["exit","close"]):
            res = np.random.choice(["have a good day","Bye","Goodbye","Hope to meet soon"])
            ex=False

        
         ## conversation
        else:
            check_for_switch = predict_intent_for_switch(switch_model,ai.text)
            if ai.text==None:
                res="Sorry, but i no understand you, you fit talk mek i hear again?"

            elif check_for_switch in possible_switch:
                ai.synthesize_pigin(ai.translate_pigin("switching to {}".format(check_for_switch)))
                return check_for_switch

            else:
                history = trim_history(history,6)
                res,history = chat_gptj(client,ai.text,contexts,history)
                
                
                res = ai.translate_pigin(res,from_='english',to_='pigin')['target ']
                
                
        ai.synthesize_pigin(res)
    
    print("Closing omeifeh")




def global_communication():
    #--------------------------------------------------START WITH ENGLISH------------------------------------------------------------
    switcher = talk_english('/home/omeife/project/CameraServer/Return_values/updated_names.txt')
    switch = switcher
    #--------------------------------------------------------------------------------------------------------------------------------

    while True:
        
        if switch == 'pigin':
            switcher = talk_pigin(client)
            switch=switcher

        elif switch=='swahili':
            switcher = talk_swahili(client)
            switch=switcher

        elif switch == 'arabic':
            switcher = talk_arabic(client)
            switch=switcher

        elif switch == 'english':
            switcher = talk_english(client)
            switch = switcher
      
        elif switch == 'french':
            switcher = talk_french(client)


"""if __name__ == "__main__":
    #print("done")
    #get = predict_intent_for_switch(switch_model,"can we switch to swahili")
    #print(get)
    #client = nlpcloud.Client("finetuned-gpt-neox-20b", "78f028e1962e3910fcb0103f03a4394166fc81e0", gpu=True, lang="en")
    #talk_french(client)

    global_communication()
"""

