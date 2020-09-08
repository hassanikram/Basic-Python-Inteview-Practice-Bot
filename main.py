import pyaudio
import wave
from wit import Wit
import random
import numpy as np

client = Wit('5AW2H4RD4MUUYNFLIJCJWMZGZS5S3LUT')

data={'break_answer':{'question':'What is the use of Break Statement', 'intent':'break'},
      'continue_answer':{'question':'What is the use of Continue Statement', 'intent':'continue'},
      'arg_answer':{'question':'What is the us of *arg', 'intent':'args'},
      'deep_copy_answer':{'question':'What is the use of Deep Copy', 'intent':'deep_copy'},
      'dictionary_answer':{'question':'What is Dictionary in Python', 'intent':'dictionary'},
      'golbal_variable_answer':{'question':'What is a Global Variable', 'intent':'golbal_variable'},
      'local_variable_answer':{'question':'What is a Local Variable', 'intent':'local_variable'},
      'interpreted_language_answer':{'question':'Why is Python an Interpreted Language', 'intent':'interpret'},
      'is_keyword_answer':{'question':'Why IS Keyword is used','intent':'is_keyword'}
      ,'iterator_answer':{'question':'What is an Iterator in Python','intent':'iterator'}
      ,'lambda_function_answer':{'question':'What is a Lambda Function in Python','intent':'lambda_function'}
      ,'namespace_answer':{'question':'What is Namespace','intent':'namespace'}
      ,'self_keyword_answer':{'question':'What is the use of Self Keyword','intent':'self_keyword'}
      ,'set_data_type_answer':{'question':'What is SET in Python','intent':'set_data_type'}
      ,'shallow_copy_answer':{'question':'What is Shallow Copy in Python','intent':'shallow_copy'}
      ,'split_function_answer':{'question':'What is Split function','intent':'split_function'}
      ,'tuple_answer':{'question':'What is Tuple in Python','intent':'tuple'}}



data_new={'continue_answer':{'question':'What is the use of Continue Statement', 'intent':'continue'}}



def record_audio(filename):
    filename = 'Data/'+str(filename)+'.wav'

    # set the chunk size of 1024 samples
    chunk = 1024

    # sample format
    FORMAT = pyaudio.paInt16

    # mono, change to 2 if you want stereo
    channels = 1

    # 44100 samples per second
    sample_rate = 44100
    record_seconds = 10

    # initialize PyAudio object
    p = pyaudio.PyAudio()

    # open stream object as input & output
    stream = p.open(format=FORMAT, channels=channels, rate=sample_rate, input=True, output=True,
                    frames_per_buffer=chunk)
    frames = []
    print("Recording...")
    for i in range(int(44100 / chunk * record_seconds)):
        data = stream.read(chunk)
        # if you want to hear your voice while recording
        # stream.write(data)
        frames.append(data)
    print("Finished recording.")
    # stop and close stream
    stream.stop_stream()
    stream.close()
    # terminate pyaudio object
    p.terminate()
    # save audio file
    # open the file in 'write bytes' mode
    wf = wave.open(filename, "wb")
    # set the channels
    wf.setnchannels(channels)
    # set the sample format
    wf.setsampwidth(p.get_sample_size(FORMAT))
    # set the sample rate
    wf.setframerate(sample_rate)
    # write the frames as bytes
    wf.writeframes(b"".join(frames))
    # close the file
    wf.close()



number_of_questions=5
list_of_question_numbers=[]
i=0
while True:
    random_number=random.randint(0,len(data)-1)
    while random_number in list_of_question_numbers:
        random_number = random.randint(0, len(data)-1)
    list_of_question_numbers.append(random_number)
    i=i+1
    if i==number_of_questions:
        break


print(list_of_question_numbers)

#for i in range(number_of_questions):
for (key,value) in list(data_new.items()):
    #key,value=list(data.items())[list_of_question_numbers[i]]
    print()
    print(value['question'])
    record_audio(key)
    with open('Data/'+str(key)+'.wav', 'rb') as f:
       resp = client.speech(f, {'Content-Type': 'audio/wav'})
    #print(resp['text'])
    try:
        print(resp['text'])
        returned_intent=resp['intents'][0]['name']

        if returned_intent == value['intent']:
            print('Correct')
        else:
            print('Incorrect')
    except:
        print('Could not hear answer completely')
        continue