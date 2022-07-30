from kivy.lang import Builder
from kivymd.app import MDApp
KV = '''
MDScreen:
    MDIconButton:
        icon: 'microphone'
        pos_hint: {'center_x': .5, 'center_y': .5}
        user_font_size: '40sp'
        theme_text_color: 'Custom'
        text_color: app.theme_cls.primary_color
        on_release: app.summer()
    MDLabel:
        text:'Tap The Mic To Speak....'
        pos_hint: {'center_x': .5, 'center_y': .4}
        halign:'center'
'''


class mic(MDApp):
    def build(self):
        self.theme_cls.theme_style = 'Dark'
        self.icon = 'M1 Air Intro Thumbnail.png'
        return Builder.load_string(KV)

    def summer(self):
        import gmail
        import pyttsx3
        import speech_recognition as sr
        import wikipedia
        import os
        import datetime
        import sys
        from googlesearch import search
        import webbrowser

        print('Please say "Hello" to Wake up')
        print()

        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        engine.setProperty('voice',voices[36].id)


        def speak1(audio):
            engine.say(audio)
            engine.runAndWait()

        def takecommand1():
                r = sr.Recognizer()
                with sr. Microphone() as source:
                    print('listening.....')
                    r.pause_threshold = 1
                    r.energy_threshold = 4000
                    audio_data = r.listen(source)
                try:
                    print('recognizing....')
                    query = r.recognize_google(audio_data,language='en-IN')
                    print(f'you said:{query}\n')
                except Exception as e:
                    print(e)
                    print('say that again please')
                    return 'none'
                return query
            
        if __name__=='__main__':
                while True:
                    query = takecommand1().lower()
                    print(query)
                    print()
                    if 'hello' in query:
                        def horizon():
                            engine = pyttsx3.init()
                            voices = engine.getProperty('voices')
                            engine.setProperty('voice',voices[34].id)
                            print()
                            print('Try Speaking...\n\nWhat is the time\nPlease search...\nplay(''music,videos'')...\nwhat is (ex- 2+2)...\ntell me about(informative knowledge)\nwhat do you know about\nwrite a message (Gmail)\nmy playlist\nopen saavn\nopen youtube music\nopen camera\nopen i mart\nopen amazon\nopen facebook\nopen youtube\nopen gmail\nopen google')
                            print()
                            print('To exit please speak "close"')
                            print()

                            
                            def speak(audio):
                                engine.say(audio)
                                engine.runAndWait()

                            def WishMe():
                                h = int(datetime.datetime.now().hour)
                                if h>0 and h<12:
                                    speak('good morning Rishit')
                                elif h>12 and h<16:
                                    speak('good afternoon Rishit')
                                else:
                                    speak('good evening Rishit')
                                    


                            def takecommand():
                                r = sr.Recognizer()
                                with sr. Microphone() as source:
                                    print('listening.....')
                                    r.pause_threshold = 1
                                    r.energy_threshold = 4000
                                    audio_data = r.listen(source)
                                try:
                                    print('recognizing....')
                                    query = r.recognize_google(audio_data,language='en-IN')
                                    print(f'you said:{query}\n')
                                except Exception as e:
                                    print(e)
                                    print('say that again please')
                                    return 'none'
                                return query

                            if __name__=='__main__':
                                WishMe()
                                while True:
                                    query = takecommand().lower()
                                    print(query)
                                    
                                    if 'time' in query:
                                        st = datetime.datetime.now()
                                        print(st)
                                        speak(st.strftime("%H:%M:%S"))

                                    elif 'date' in query:
                                        st = datetime.datetime.now()
                                        print(st.strftime('%D'))
                                        speak(st.strftime('%D'))
                                        

                                    elif 'day' in query:
                                        st = datetime.datetime.now()
                                        print(st.strftime('%A'))
                                        speak(st.strftime('it is a %A'))


                                    # Gmail Writing
                                    
                                    # SEARCHES 

                                    elif 'search' in query:
                                        l=[]
                                        for j in search(query, tld='co.in', num=10, stop=10, pause=2):
                                            l.append(j)
                                        
                                        speak('yes sir')
                                        webbrowser.open(l[0])
                                    
                                    elif 'open' in query:
                                        l=[]
                                        for j in search(query, tld='co.in', num=10, stop=10, pause=2):
                                            l.append(j)
                                        
                                        speak('yes sir opening')
                                        webbrowser.open(l[0])
                                    
                                    elif 'what' in query:
                                        l=[]
                                        for j in search(query, tld='co.in', num=10, stop=10, pause=2):
                                            l.append(j)
                                        
                                        speak('yes sir')
                                        webbrowser.open(l[0])
                                        

                                    # MUSIC
                                                                
                                    elif 'youtube music' in query:
                                        l=[]
                                        for j in search(query, tld='co.in', num=10, stop=10, pause=2):
                                            l.append(j)
                                        
                                        speak('yes sir opening youtube music')
                                        webbrowser.open(l[0])

                                    elif 'play' in query:
                                        l=[]
                                        for j in search(query, tld='co.in', num=10, stop=10, pause=2):
                                            l.append(j)
                                        
                                        speak('yes sir playing')
                                        webbrowser.open(l[0])

                                    #APPS
                                    elif 'amazon' in query:
                                        l=[]
                                        for j in search(query, tld='co.in', num=10, stop=10, pause=2):
                                            l.append(j)
                                        
                                        speak('yes sir opening amazon')
                                        webbrowser.open(l[0])

                                    elif 'youtube' in query:
                                        l=[]
                                        for j in search(query, tld='co.in', num=10, stop=10, pause=2):
                                            l.append(j)
                                        
                                        speak('yes sir opening youtube')
                                        webbrowser.open(l[0])
                                        

                                    # GOOGLE APPS

                                    elif 'gmail.com' in query:
                                        l=[]
                                        for j in search(query, tld='co.in', num=10, stop=10, pause=2):
                                            l.append(j)
                                        
                                        speak('yes sir opening mail')
                                        webbrowser.open(l[0])

                                    elif 'google' in query:
                                        l=[]
                                        for j in search(query, tld='co.in', num=10, stop=10, pause=2):
                                            l.append(j)
                                        
                                        speak('yes sir opening google')
                                        webbrowser.open(l[0])

                                    # communication

                                    elif 'great' in query:
                                        speak('thankyou sir')

                                    elif 'amazing' in query:
                                        speak('thankyou sir')
                                        
                                    elif 'how are you' in query:
                                        speak('i am having a great day,sir')
                                        
                                    elif 'i hope you are fine' in query:
                                        speak('yes sir, could not be better')
                                        speak('i hope you are fine, sir')
                                        
                                    elif 'i am great' in query:
                                        speak('that is great,sir')

                                    elif 'close' in query:
                                        speak('ok sir,have a great day ahead')
                                        quit()
                                        
                                
                        
                        horizon()



mic().run()