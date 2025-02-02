# E:\PYTHONCLASSTF>.\tensorflowvenv\Scripts\activate
# cd PrakashSenapati\2024_12_12_RNN_Theory_NextWordPred_SpeechRecognition
# (tensorflowvenv) E:\PYTHONCLASSTF\PrakashSenapati\2024_12_12_RNN_Theory_NextWordPred_SpeechRecognition>python Pyttsx3_Self.py
# If you will run this code from Jupyter notebokk then below error will come: so run this file from terminal to avoid error
# RuntimeError: run loop already started
# This will open interface in new window but will show nothing. Text will be read in female voice and in the end it will be saved on current folder

import pyttsx3
import nest_asyncio

# Patch the event loop to allow re-entry
nest_asyncio.apply()

engine = pyttsx3.init()

# Set properties
engine.setProperty("rate", 125)
engine.setProperty("volume", 1.0)

voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)  # Female voice

# Speak text
# end first line with \ to avoid the empty line!
engine.say('''\
Bidirectional Encoder Representations from Transformers (BERT) is a deep learning model 
that helps computers understand the meaning of text by analyzing the relationships between words in a sentence. 
BERT is a natural language processing (NLP) model that learns to understand the 
context of unlabeled text by looking at words from both the left and right. 
It's trained on large amounts of language data, including English Wikipedia and the Brown Corpus.
''')
engine.runAndWait()

# Save audio to file
engine.save_to_file('''\
pyttsx3 is a text-to-speech conversion library in Python. 
Unlike alternative libraries, it works offline and is compatible with both Python 2 and 3
''',"test.mp3")
engine.runAndWait()
print("Audio saved successfully.")