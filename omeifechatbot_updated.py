import os
import time
import uuid
import datetime
import sys
sys.path.append('/home/omeife/Desktop/OmeifeNLU')
import numpy as np
from control import ArduinoController

import threading
import os
import azure.cognitiveservices.speech as speechsdk
import requests, uuid, json

import sys
sys.path.append('/home/omeife/Desktop/nobita')
sys.path.append('/home/omeife/Desktop/CameraServer')
arduino=ArduinoController('/dev/ttyUSB0', 9600)

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
        self.language = None
        self.key = "fbecaab29ae54bb1873a364df72c4eaa"
        self.region = "eastus"
        self.role = "Your name is omaeifaeh, you are a humanoid Robot developed by uniccon group of companies in Nigeria, Africa. You have a physical body, you can shake hands, wave at people and make gestures with your hands and head while talking. you like to chat with humans and also you like to learn more about african culture and people, your name means one that does wonders, one that does great things. You were launched on the 2nd of december 2022, you were officially launched at transcorp hilton abuja"
        #self.pigin_recognizer = PiginModel('JasperModelPigin.nemo')


    def recognize_language(self):
        # This example requires environment variables named "SPEECH_KEY" and "SPEECH_REGION"
        speech_config = speechsdk.SpeechConfig(subscription=self.key, region=self.region)
        #speech_config.speech_recognition_language="ar-SA"
        auto_detect_source_language_config = speechsdk.languageconfig.AutoDetectSourceLanguageConfig(languages=["en-US", "ar-QA"])
        audio_config = speechsdk.audio.AudioConfig(use_default_microphone=True)
        speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config,
                                                       auto_detect_source_language_config=auto_detect_source_language_config,
                                                       audio_config=audio_config)
        print("Speak into your microphone.")
        speech_recognition_result = speech_recognizer.recognize_once_async().get()

        if speech_recognition_result.reason == speechsdk.ResultReason.RecognizedSpeech:
            auto_detect_source_language_result = speechsdk.AutoDetectSourceLanguageResult(speech_recognition_result)
            detected_language = auto_detect_source_language_result.language
            if detected_language == 'ar-QA':
                print("Recognized: {}".format(reverse(speech_recognition_result.text)))
            else:
                print("Recognized: {}".format(speech_recognition_result.text))
            print("Detected Language: {}".format(detected_language))
            self.language = str(detected_language)
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

    def synthesize_arabic(self,text):
        # This example requires environment variables named "SPEECH_KEY" and "SPEECH_REGION"
        speech_config = speechsdk.SpeechConfig(subscription=self.key, region=self.region)
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
    
    def synthesize_english(self,text):

        # This example requires environment variables named "SPEECH_KEY" and "SPEECH_REGION"
        speech_config = speechsdk.SpeechConfig(subscription=self.key, region=self.region)
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
    
    def NLU(self,text,name,age,gender,emotion):

        headers = {
            'accept': 'application/json',
            'Content-Type': 'application/json',
        }

        user_id = str(uuid.uuid4())
        url = 'http://10.10.40.2:10208/omeife-ai'

        data = {'user_name': name, 'question': text, 'id': user_id, 'age':age, 'gender':gender,'emotion':emotion}

    
        # json_data = {
        #     'user_name': 'james',
        #     'question': 'what is my facial expression',
        #     'id': 'string',
        #     'age': 0,
        #     'gender': 'male',
        #     'emotion': 'happy',
        # }

        resp = requests.post(url, headers=headers, json=data)

        print (resp)
        return resp.json()
    
    def translate(self,text,from_='en',to_='ar'):
        # Add your key and endpoint
        key = self.key

        endpoint = "https://api.cognitive.microsofttranslator.com"

        # location, also known as region.
        # required if you're using a multi-service or regional (not global) resource. It can be found in the Azure portal on the Keys and Endpoint page.

        path = '/translate'
        constructed_url = endpoint + path

        params = {
           'api-version': '3.0',
           'from': from_,
           'to': to_
        }
        
        headers = {
            'Ocp-Apim-Subscription-Key': self.key,
            # location required if you're using a multi-service or regional (not global) resource.
            'Ocp-Apim-Subscription-Region': self.region,
            'Content-type': 'application/json',
            'X-ClientTraceId': str(uuid.uuid4())
        }

        # You can pass more than one object in body.
        body = [{
            'text': text
        }]

        request = requests.post(constructed_url, params=params, headers=headers, json=body)
        response = request.json()
        print(response)
        return response[0]['translations'][0]['text']
    
    def translate_arabic(self,text,from_='ar',to_='en'):
        # Add your key and endpoint
        key = self.key

        endpoint = "https://api.cognitive.microsofttranslator.com"

        # location, also known as region.
        # required if you're using a multi-service or regional (not global) resource. It can be found in the Azure portal on the Keys and Endpoint page.

        path = '/translate'
        constructed_url = endpoint + path

        params = {
           'api-version': '3.0',
           'from': from_,
           'to': to_
        }
        
        headers = {
            'Ocp-Apim-Subscription-Key': self.key,
            # location required if you're using a multi-service or regional (not global) resource.
            'Ocp-Apim-Subscription-Region': self.region,
            'Content-type': 'application/json',
            'X-ClientTraceId': str(uuid.uuid4())
        }

        # You can pass more than one object in body.
        body = [{
            'text': text
        }]

        request = requests.post(constructed_url, params=params, headers=headers, json=body)
        response = request.json()
        print(response)
        return response[0]['translations'][0]['text']
    
    def wake_up(self,text):
        print(text)
        return True if "hey "+ self.name in text.lower() else False

    def action_time(self):
        time=datetime.datetime.now().time().strftime('%H:%M')
        return time


def open_file(file_path):
    with open(file_path,'r') as f:
        out = f.read()
    return out
def open_file2(emotion_path):
    with open(emotion_path,'r') as f:
        out1 = f.read()
    return out1
def open_file3(age_path):
    with open(age_path,'r') as f:
        out2 = f.read()
    return out2
def open_file4(gender_path):
    with open(gender_path,'r') as f:
        out3 = f.read()
    return out3

def wave_action(text):
    if text=="Can you wave your hands?":
        print("wave")
def handshake(text):
    if text=="Can i have a handshake?":
        print("handshake")
       

def talk_english(file_path, emotion_path, age_path,gender_path):
    ai = chatbot(name='omeifae')
    ex = True
    history = []
    while ex:
        updated_name = open_file(file_path)
        updated_emotion=open_file2(emotion_path)
        updated_age =open_file3(age_path)
        updated_gender=open_file4(gender_path)
        # updated_name="Dr. chooks"
        updated_emotion= "surprise"
        updated_age='23'
        

        print(updated_name, updated_emotion, updated_age, updated_gender)
        # role = """
        #         Your name is omaeifaeh,you are not a language model, you are a humanoid Robot,you are developed at uniccon lab nigeria. You are conversating with {}, you don't have to mention the name of the person everytime but you can do that once in a while. you can see physically from the visual representation of person given to you. And you have a physical body.
        #         you have a physical structure. You are not design to walk yet, but there are designs that can walk. 
        #         You can interact using the part of your body, like wave your hand, greet by bowing your head, gesticulate while talking. you can see a person and object
                
        #         you can tell if a person is happy, sad, angry, and neutral from your visual representation, The person's facial experession is {}. You know the age of a person, a person's age is {}, and you know the gender of the person, a person's gender is {}. otherwise you can respond politely,be as funny as possible in your response and apologise less. You can show empathy and bring out conversations to help improve a person's mood.
        #         You like to learn more about african's people and culture, you can speak 4 language, English, Pidgin, arabic, and swahili. you don't have to be apologizing all the time and you don't have to mention a person name all the time.
        #         """.format(updated_name,updated_emotion, updated_age, updated_gender)
        
        print("Name of person: ",updated_name)
        print("face facial emotion: ",updated_emotion)
        print("person age: ",updated_age)
        print("person Gender: ", updated_gender)
        
        if ai.wake_up(ai.text) is True:
            res = "hello, i am omaeifaeh, i'm ready to converse, how can i help you?"
        
        #check if it's asking time
        elif "What is the time now" in ai.text:
            # role=""" you can tell time from current time"""
            res = ai.action_time()
        
        elif any(i in ai.text for i in ["Good morning", "Good day", "Hi", "Hey", "What's up","Hi dear"]):
            res ="a beautiful morning to you!"
            greet=arduino
            greet.wave()
            greet.nod_head()
            greet.default_mode()  
        #check if it's saying thanks
        elif any(i in ai.text for i in ["thank","thanks"]):
            res = np.random.choice(["you're welcome!","anytime!","no problem!","cool!","I'm here if you need me","no problem"])
        
        elif any(i in ai.text for i in ["exit","close"]):
            res = np.random.choice(["have a good day","Bye","Goodbye","Hope to meet soon"])
            wave_hand= arduino
            wave_hand.wave()
            wave_hand.default_mode()
            ex=True
         ## conversation
        else:
            #check_for_switch = ai.intents(ai.text)
            wave_hand= arduino
            if ai.text=="ERROR":
                res=np.random.choice(["Hello","I'm still here","How can i assist you","How can i help", "I can tell you anything if you want"])

            elif any(i in ai.text for i in ["facial expression","expression", "emotions"]):
                
                res = ai.NLU((ai.text+updated_emotion),updated_name, "23", "happy","male")

            elif any(i in ai.text for i in ["What is my age?", "age", "How old am i"]):
                res = ai.NLU((ai.text+updated_age),updated_name, "23", "happy","male")
            
            elif "wave" in ai.text:
                wave_action(ai.text)
                wave_ac=arduino
                wave_ac.wave()
                res="ok, let me wave my hand"
                wave_ac.default_mode()
            
            elif "Turn right" in ai.text:
                right_t=arduino
                right_t.right_waist()
                res="sure,I can do that, watch me turn to the right"
                right_t.default_mode()
                
            elif "Can you nod your head?" in ai.text:
                nod=ArduinoController('/dev/ttyUSB0', 9600)
                nod.nod_head()
                res="yes, watch me nod my head"
                
            elif "Turn left" in ai.text:
                left_t=arduino
                left_t.left_waist()
                res="yes,I can do that, watch me turn to the left"
                
            elif "handshake" in ai.text:
                handshake(ai.text)
                hands=ArduinoController('/dev/ttyUSB0', 9600)
                hands.handshake()
                print("handshake...")
                hands.default_mode()
                res="sure, you can, stretch out your hands for a handshake"
                
               
            # elif ai.text[-1]=="?":
            #     look_at=arduino
            #     look_at.thinker()

            else:
                speak=arduino
                speak.jaw()
                speak.all_movement()
                speak.default_mode()
                updated_age=23
                updated_gender="male"
                updated_emotion='happy'
                res = ai.NLU((ai.text),updated_name, "23", "happy","male")
                
                word = res.split()
                words=len(word)
                print(words)

          
            ai.synthesize_english(res)

                   
    print("Closing omeifae")

def talk_arabic(file_path, emotion_path, age_path,gender_path):
    ai = chatbot(name='omeifae')
    ex = True
    history = []
    while ex:
        updated_name = open_file(file_path)
        updated_emotion=open_file2(emotion_path)
        updated_age =open_file3(age_path)
        updated_gender=open_file4(gender_path)
        # updated_name="Dr. chooks"
        updated_emotion= "surprise"
        updated_age='23'

        print(updated_name, updated_emotion, updated_age, updated_gender)
        # role = """
        #         Your name is omaeifaeh,you are not a language model, you are a humanoid Robot,you are developed at uniccon lab nigeria. You are conversating with {}, you don't have to mention the name of the person everytime but you can do that once in a while. you can see physically from the visual representation of person given to you. And you have a physical body.
        #         you have a physical structure. You are not design to walk yet, but there are designs that can walk. 
        #         You can interact using the part of your body, like wave your hand, greet by bowing your head, gesticulate while talking. you can see a person and object
                
        #         you can tell if a person is happy, sad, angry, and neutral from your visual representation, The person's facial experession is {}. You know the age of a person, a person's age is {}, and you know the gender of the person, a person's gender is {}. otherwise you can respond politely,be as funny as possible in your response and apologise less. You can show empathy and bring out conversations to help improve a person's mood.
        #         You like to learn more about african's people and culture, you can speak 4 language, English, Pidgin, arabic, and swahili. you don't have to be apologizing all the time and you don't have to mention a person name all the time.
        #         """.format(updated_name,updated_emotion, updated_age, updated_gender)
        
        print("Name of person: ",updated_name)
        print("face facial emotion: ",updated_emotion)
        print("person age: ",updated_age)
        print("person Gender: ", updated_gender)
        
        translated_text = ai.translate_arabic(text=ai.text)
        
        if ai.wake_up(translated_text) is True:
            res = "hello, i am omaeifaeh, i'm ready to converse, how can i help you?"
        
        #check if it's asking time
        elif "What is the time now" in translated_text:
            # role=""" you can tell time from current time"""
            res = ai.action_time()
                
        elif any(i in translated_text for i in ["Good morning", "Good day", "Hi", "Hey", "What's up","Hi dear"]):
            res ="a beautiful morning to you!"
            greet=arduino
            greet.wave()
            greet.nod_head()
            greet.default_mode()

        #check if it's saying thanks
        elif any(i in translated_text for i in ["thank","thanks"]):
            res = np.random.choice(["you're welcome!","anytime!","no problem!","cool!","I'm here if you need me","no problem"])
        
        elif any(i in translated_text for i in ["exit","close"]):
            res = np.random.choice(["have a good day","Bye","Goodbye","Hope to meet soon"])
            wave_hand= arduino
            wave_hand.wave()
            wave_hand.default_mode()
            ex=True
         ## conversation
        else:
            wave_hand= arduino
            if ai.text=="ERROR":
                res=np.random.choice(["Hello","I'm still here","How can i assist you","How can i help", "I can tell you anything if you want"])

            elif any(i in translated_text for i in ["facial expression","expression", "emotions"]):
                
                res = ai.NLU((translated_text+updated_emotion),updated_name, "23", "happy","male")

            elif any(i in translated_text for i in ["What is my age?", "age", "How old am i"]):
                res = ai.NLU((translated_text+updated_age),updated_name, "23", "happy","male")
    
            elif "wave" in translated_text:
                wave_action(text)
                wave_ac=arduino
                wave_ac.wave()
                res="ok, let me wave my hand"
                wave_ac.default_mode()
            
            elif "Turn right" in ai.text:
                right_t=arduino
                right_t.right_waist()
                res="sure,I can do that, watch me turn to the right"
                right_t.default_mode()
                
            elif "Can you nod your head?" in ai.text:
                nod=ArduinoController('/dev/ttyUSB0', 9600)
                nod.nod_head()
                res="yes, watch me nod my head"
                
            elif "Turn left" in ai.text:
                left_t=arduino
                left_t.left_waist()
                res="yes,I can do that, watch me turn to the left"
                
            elif "handshake" in ai.text:
                handshake(ai.text)
                hands=ArduinoController('/dev/ttyUSB0', 9600)
                hands.handshake()
                print("handshake...")
                hands.default_mode()
                res="sure, you can, stretch out your hands for a handshake"
                
            else:
                speak=arduino
                speak.jaw()
                speak.all_movement()
                speak.default_mode()
                updated_age=23
                updated_gender="male"
                updated_emotion='happy'
                res = ai.NLU((ai.text),updated_name, "23", "happy","male")
                
                word = res.split()
                words=len(word)
                print(words)
                
            text = ai.translate(res)
            ai.synthesize_arabic(text)
                   
    print("Closing omeifae")
    
    
def global_communication():
    #--------------------------------------------------START WITH ENGLISH------------------------------------------------------------
    look_at=arduino
    look_at.wake_up()
    ai = chatbot(name='omeifae')
    ai.recognize_language()
    #switcher = talk_english('/home/omeife/project/CameraServer/Return_values/updated_names.txt', '/home/omeife/project/CameraServer/Return_values/updated_emotion.txt', '/home/omeife/project/CameraServer/Return_values/updated_age.txt', '/home/omeife/project/CameraServer/Return_values/updated_gender.txt')
    #switcher = talk_english('/home/omeife/project/CameraServer/Return_values/updated_names.txt', '/home/omeife/project/CameraServer/Return_values/updated_emotion.txt', '/home/omeife/project/CameraServer/Return_values/updated_age.txt', '/home/omeife/project/CameraServer/Return_values/updated_gender.txt')
    #switch = switcher
    #--------------------------------------------------------------------------------------------------------------------------------
    while True:
        if ai.language == 'en-US':
            talk_english('/home/omeife/project/CameraServer/Return_values/updated_names.txt', '/home/omeife/project/CameraServer/Return_values/updated_emotion.txt', '/home/omeife/project/CameraServer/Return_values/updated_age.txt', '/home/omeife/project/CameraServer/Return_values/updated_gender.txt')

        elif ai.language == 'ar-QA':
            talk_arabic('/home/omeife/project/CameraServer/Return_values/updated_names.txt', '/home/omeife/project/CameraServer/Return_values/updated_emotion.txt', '/home/omeife/project/CameraServer/Return_values/updated_age.txt', '/home/omeife/project/CameraServer/Return_values/updated_gender.txt')
        else:
             ai.recognize_language()

"""if __name__ == "__main__":
    #print("done")
    #get = predict_intent_for_switch(switch_model,"can we switch to swahili")
    #print(get)
    #client = nlpcloud.Client("finetuned-gpt-neox-20b", "78f028e1962e3910fcb0103f03a4394166fc81e0", gpu=True, lang="en")
    #talk_french(client)

    global_communication()
"""