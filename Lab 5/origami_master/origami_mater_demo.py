#This example is directly copied from the Tensorflow examples provided from the Teachable Machine.

import tensorflow.keras
from PIL import Image, ImageOps
import numpy as np
import cv2
import sys

import subprocess
import wave
from vosk import Model, KaldiRecognizer

import threading

######
### Global vars & Instructions
### Work of choice: paper butterfly
STEP_NUM = 11 # total num of instructions
STEP_IDX = 0 # current step
# STEP_END = False # if user indicated current step is done
STEP_FLAGS = [False] * STEP_NUM # general progress: True = over; False = not over yet;
STEP_USR_DONE_FLAGS = [False] * STEP_NUM
LABELS = ["step1", "step2", "step3", "step4", "step5", "step6", "step7", "step8", "step9", "step10", "step11"]
INSTRUCTIONS = ["Step 1 : Place the paper diagonally with one corner pointing at you. We will be refering to the four corners as the left, right, lower and upper corner.",
                "Step 2 : Take the lower corner, fold it up, make it meet the upper corner.",
                "Step 3 : Take the right corner, fold it up, make it meet the upper corner.",
                "Step 4 : Flip the piece horitontally. Repeat. Take the corner now at your right, fold it up, make it meet the upper corner.",
                # "Step 5 : Take the corner now at your right, fold it up, make it meet the upper corner."
                "Steo 5 : Hold the paper up vertically, so that the side with a open pocket is facing up."
                "Step 6 : Place a finger into the opening pocket, and press on the side. Flatten the paper. Now you should have a triangle.",
                "Step 7 : Place the triangle with its top corner pointing away from you. Take its bottom edge, fold it up horizontally to a bit lower than the top corner, leave a little tip of the top corner showing from the top.",
                "Step 8 : Touch the two bottom corners that you just folded up, and feel that there are two layers on each side. Fold the top layers down as far as they can easily go, on both sides. Now, you have a butterfly shape.",
                "Step 9: Let's give the butterfly some volume. Fold the piece vertically from left to right, make the two sides meet each other.",
                "Step 10: Hold the piece in one hand, pinching on the back of the folding line from the previous step. Spread the wings with your other hand and press them down. Now, you have a butterfly."]


######
### Audio Interations
# Model directory in current directory
AUD_MODEL_DIR = "aud_model"
if not os.path.exists(AUD_MODEL_DIR):
    print ("Please download the model from https://github.com/alphacep/vosk-api/blob/master/doc/models.md and unpack as 'model' in the current folder.")
    exit (1)

USER_INPUT_FILE = 'user_audio_input.wav'
aud_model = Model(AUD_MODEL_DIR)

# Speak
def speak(instruction):
    command = """
        say() { 
            local IFS=+;/usr/bin/mplayer -ao alsa -really-quiet -noconsolecontrols "http://translate.google.com/translate_tts?ie=UTF-8&client=tw-ob&q=$*&tl=en"; 
        } ; 
    """ + f"say '{instruction}'"
    subprocess.call(command, shell=True)

# Current recording duration: 3s
def record_user_input():
    subprocess.call("arecord -D hw:2,0 -f cd -c1 -r 48000 -d 3 -t wav " + USER_INPUT_FILE, shell=True)

def recognize(pattern):
    wf = wave.open(USER_INPUT_FILE, "rb")
    if wf.getnchannels() != 1 or wf.getsampwidth() != 2 or wf.getcomptype() != "NONE":
        print ("Audio file must be WAV format mono PCM.")
        exit (1)

    rec = KaldiRecognizer(aud_model, wf.getframerate(), pattern)

    while True:
        data = wf.readframes(4000)
        if len(data) == 0:
            break
        if rec.AcceptWaveform(data):
            res = json.loads(rec.Result())
            print("Result:", res['text'])
            return res['text']
        # else:
        #     print(rec.PartialResult())
    print("Failed to recognize")
    return ""

def dont_understand():
    speak("What, what are you saying? I don’t understand.")


def give_instructions():
    speak(INSTRUCTIONS[STEP_IDX])


######

class AudioInteractionThread(threading.Thread):
    def __init__(self, name, lock):
        threading.Thread.__init__(self, name=name)
        self.name = name
        self.lock = lock
        self.pattern = "I'm good done ok"
    def run(self):
        global STEP_IDX, STEP_USR_DONE_FLAGS
        while True: ### Always recording?
            record_user_input()
            result = recognize(self.pattern)
            if "done" in result or "good" in result or "ok" in result:
                STEP_USR_DONE_FLAGS[STEP_IDX] = True
            else:
                speak("Okay. Let me know when you are ready.")


### Introduction
intro = "Hi, this is origami master. I will walk you through the steps of making a paper butterfly, step by step. When you are done with step, let me know and I will check if you got it right."
speak(intro)

lock = threading.Lock()
user_aud_thread = AudioInteractionThread('user_aud', lock)
user_aud_thread.start()


# Disable scientific notation for clarity
np.set_printoptions(suppress=True)

img = None
webCam = False
if(len(sys.argv)>1 and not sys.argv[-1]== "noWindow"):
   try:
      print("I'll try to read your image");
      img = cv2.imread(sys.argv[1])
      if img is None:
         print("Failed to load image file:", sys.argv[1])
   except:
      print("Failed to load the image are you sure that:", sys.argv[1],"is a path to an image?")
else:
   try:
      print("Trying to open the Webcam.")
      cap = cv2.VideoCapture(0)
      if cap is None or not cap.isOpened():
         raise("No camera")
      webCam = True
   except:
      print("Unable to access webcam.")


######
### Origami Step Recognition

# Load the model
TM_MODEL_PATH = 'tm_model/om_keras_model.h5'
tm_model = tensorflow.keras.models.load_model(TM_MODEL_PATH)
# Load Labels:
labels = []
f = open("tm_model/labels.txt", "r")
for line in f.readlines():
    if(len(line)<1):
        continue
    labels.append(line.split(' ')[1].strip())

######
### Main loop

while(True):
    # Give instructions for current step if haven't been done yet
    if not STEP_FLAGS[STEP_IDX]:
        give_instructions()
        STEP_FLAGS[STEP_IDX] = True


    # If user indicated step is done
    if STEP_FLAGS[STEP_IDX] and STEP_USR_DONE_FLAGS[STEP_IDX]:

        # Take in visual data
        if webCam:
            ret, img = cap.read()

        rows, cols, channels = img.shape
        data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

        size = (224, 224)
        img =  cv2.resize(img, size, interpolation = cv2.INTER_AREA)
        # turn the image into a numpy array
        image_array = np.asarray(img)

        # Normalize the image
        normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1
        # Load the image into the array
        data[0] = normalized_image_array

        # run the inference -> get step prediction
        prediction = tm_model.predict(data)
        print("I think its a:",labels[np.argmax(prediction)])

        if labels[np.argmax(prediction)] == LABELS[STEP_IDX]:
            speak(INSTRUCTIONS[STEP_IDX][:7] + " is correct. Great job!")
            # Move on to the next step
            STEP_IDX += 1



    if webCam:
        if sys.argv[-1] == "noWindow":
           cv2.imwrite('detected_out.jpg',img)
           continue
        cv2.imshow('detected (press q to quit)',img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            cap.release()
            break
    else:
        break

cv2.imwrite('detected_out.jpg',img)
cv2.destroyAllWindows()
