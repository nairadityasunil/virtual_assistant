audio = record.listen(source)
        
        # # Using google speech recognition to recognise the speech
        # data = " "
        # try:
        #     data = record.recognize_google(audio)
        
        # except sr.UnknownValueError:
        #     talk("Unable To Understand")
        #     print("Unable To Understand")
        #     return " "
        
        # except sr.RequestError as e:
        #     talk("Error From Google Speech Recognition")
        #     print("Error From Google Speech Recognition")
        #     return " "
        
        # print("Lucifer : "+data)