# Observant Systems


For lab this week, we focus on creating interactive systems that can detect and respond to events or stimuli in the environment of the Pi, like the Boat Detector we mentioned in lecture. 
Your **observant device** could, for example, count items, find objects, recognize an event or continuously monitor a room.

This lab will help you think through the design of observant systems, particularly corner cases that the algorithms needs to be aware of.


### Deliverables for this lab are:
1. Show pictures, videos of the "sense-making" algorithms you tried.
1. Show a video of how you embed one of these algorithms into your observant system.
1. Test, characterize your interactive device. Show faults in the detection and how the system handled it.

---

### Part A
### Play with different sense-making algorithms.

**\*\*\*Try each of the following four examples in the `openCV-examples`, include screenshots of your use and write about one design for each example that might work based on the individual benefits to each algorithm.\*\*\***


#### Contour Detection

https://user-images.githubusercontent.com/42874337/139736612-4c7c5b9e-86c5-4446-a08b-1d7e880633e8.mp4

For Contour detection, one of the designs we thought of is a 2D real time VR anime converter. By utilizing the Contour Detection combining with graphic algorithm, we could build a VR software utilize the contour detection to detect edges within visual fields, and process it through a animation algorithm that can make the world looks like a 2D anime in VR headset, but with real world settings and syncronized processing.

#### Face Detection

https://user-images.githubusercontent.com/42874337/139736619-e3aa47b8-72d0-4348-b6fb-31b5b2f0332d.mp4

For face detection, one of the designs that we can think of is a event participant counter that utilize face detection at entrance. It collects the faces that passes through the device and send out information to the event organizer.

#### Optical Flow Detection

https://user-images.githubusercontent.com/42874337/139736625-f7acb244-3d1c-4682-ad84-89b718622e84.mp4

For the optical flow detection, one of the designs we could think of is a virtual note / pen, that allows users to use their hands to annotate a pdf on the screen of their laptop or computer by using their hand to draw circles, or write down things in the air. 

#### Object Detection

https://user-images.githubusercontent.com/42874337/139736633-1bad1e56-8ecf-461b-b775-3129f07acfb9.mp4

For object detection, one thing we could think of is a desktop ognizer. The camera captures how many objects and the size of the objects on the desktop and use an algorithm to optimize the best layout of the desktop for saving spaces. 


#### MediaPipe

**\*\*\*Consider how you might use this position based approach to create an interaction, and write how you might use it on either face, hand or body pose tracking.\*\*\***

(You might also consider how this notion of percentage control with hand tracking might be used in some of the physical UI you may have experimented with in the last lab, for instance in controlling a servo or rotary encoder.)

https://user-images.githubusercontent.com/42874337/139738761-2dae57e8-7501-4085-8b4b-93bf0cab7777.mp4

On hand tracking, one design we could think of is to use hand gestures as instructions to tune music. index finger up indicate tuning up, while index finger down indicates tuning down. If combined with body pose tracking, we can design a more complicated orchestra command game/system that allows people to virtually adjust volume and tune of different part of the orchestra just like a commander.


#### Teachable Machines

**\*\*\*Whether you make your own model or not, include screenshots of your use of Teachable Machines, and write how you might use this to create your own classifier. Include what different affordances this method brings, compared to the OpenCV or MediaPipe options.\*\*\***

https://user-images.githubusercontent.com/42874337/139780543-70c49a21-06ed-4c88-9450-a31383d4825b.mp4


We trained a model with Teachable Machines detecting different actions we can apply to a piece of paper. This is an initial attempt to our project in designing a device that teaches origami for people with visual impairment. The model can recognize three different basic folds of origami from any angle. It categorize the current image to a specific category based on likelihood calcuated using the model. It is different from the OpenCV since it's not processing the data consecutively, but independently as single image, which makes it hard to track things or record traces. It also does not based on hard coded recognization that would be more time consuming than Mediapipe. However, it does offers a more accurate categorization ability and recognization ability in a well-controlled setting. 


### Part B
### Construct a simple interaction.

Pick one of the models you have tried, pick a class of objects, and experiment with prototyping an interaction.
This can be as simple as the boat detector earlier.
Try out different interaction outputs and inputs.

**\*\*\*Describe and detail the interaction, as well as your experimentation here.\*\*\***

For this project we are planning to prototype an origami instruction device that can give out auditory instructions to users and recognize the origami process through a camera system as we have tested with teachable machine. This is a device that solely utilize auditory interactions on a spatial task, which can be expand to many fields. This device can be used to explore the idea of teaching people with visual disabilities to learn origami that instructed by machine. This project includes audio interaction, computer vision observation system, error handler system, and physical prototyping using 3D printer.

We have also tested with the hand gesture recognization that we altered the code to recognize a **"thumbs up"** gesture that representing completion as follows:

https://user-images.githubusercontent.com/42874337/139782983-a15d7282-03a8-49a0-a5e1-d46c100f58eb.mp4

The hand gesture utilizes MediaPipe, and we anticipate to use it as a milestone detection, which allows users to show the device that they have completed the current phase and ready for the device to examine and give out next step of the interaction.

### Part C
### Test the interaction prototype


Our device in detail will be a physical desktop space that a camera hangs around 40cm above users' hands which will be able to recognize and see the origami progress from a vertical angle. Users will show the device after each step instructed, and make changes or move on to next step based on the device's feedback. 

Here's an initial prototype we designed using a desk lamp:

![0703ee0a556280b2e063cc3d99d06f2](https://user-images.githubusercontent.com/42874337/140884939-ac3476b8-9d35-4fa5-93ce-47da2a16428d.jpg)

This is actually better than our expectation since the light also contribute to the clearness of the image captured.

#### Underlying mechanism

The following is the video fo a new Teachable Machine that we implemented and trained that would be able to recognize each steps of the origami example we chose (butterfly). It contains a total of 10 steps, we have also included a default background that has nothing on the desktop surface. 

https://user-images.githubusercontent.com/42874337/140884914-3ac09e27-d8a9-47a4-8e4d-7bfc15279bf1.mp4

#### Flight test

**Flight test video:**

https://user-images.githubusercontent.com/42874337/141015380-17709dd3-ce48-4022-979d-4dc0b1a7b1d5.mp4


**1. When does it what it is supposed to do?**

The device will detect whether the user is completing the instruction properly before the next step, if not, the error handler system will instruct the user to redo the previous step or to continue from the current step. 

**2. When does it fail?**

In our interaction, the device fail sometimes when the location of the origami is placed incorrectly, or far away from the center. Due to the nature of teachable machine, it strongly influenced the accuracy of detection.

**3. When it fails, why does it fail?**

One reason is that we did not train the model enough at each different angle, another reason is that we use only one color paper on both side, which sometimes will be harder for the model to predict based on the same color origami if the shape stays similar. (Two of our steps shows very similar detection result, and higher chance to mix with each other).

**4. Based on the behavior you have seen, what other scenarios could cause problems?**

The light could also causes problem, when we train the model in one specific luminant setting, and test in another, it causes lower accuracy. Also the color of the desktop itself influence the accuracy as well in our design.

**\*\*\*Think about someone using the system. Describe how you think this will work.\*\*\***

**1. Are they aware of the uncertainties in the system?**

Our expected users will be less aware of the uncertainties in the system in our design. This is due to the fact that we are expecting our users to complete the task without any time of visual aids, even no need to look at the origami themselves.

**2. How bad would they be impacted by a miss classification?**

 Due to our error handler system, we expect our users won't be impacted too back due to a miss classification, not only will the device detect current origami progress multiple times to ensure accuracy, but also at the worst case, our user will be asked to redo the process by disassemble it to last step, which is not a huge loss.

**3. How could change your interactive system to address this?**

Other than our error handler system, we have also think of a way for our user to actively ask the device to reexamine the current origami progress if they think the device makes a mistake. 

**4. Are there optimizations you can try to do on your sense-making algorithm.**

Yes, one thing we are planning on doing is to include more samples with different desktop surface, luminant enviromental factors, and angles of the origami steps, so that the whole system can be more accurate in terms of focusing on the origami itself, instead of being influenced by the environment.

### Part D
### Characterize your own Observant system

Now that you have experimented with one or more of these sense-making systems **characterize their behavior**.
During the lecture, we mentioned questions to help characterize a material:

#### **Our Case**

In our case, the X refers to the **Origami Master** observant system. It gives instructions at each step, observes images of the user's origami piece after they performed each step (and gives the system a verbal cue) to check if they got the step right.

* **What can you use X for?**

* The core idea of this system is to do the job that's usually done with user's eyes and thinking process, so that visually impaired users can also try to learn origami.

* **What is a good environment for X?**

* An environment that's relatively quiet, and has a flat platform for the user to place X and do their work.

* **What is a bad environment for X?**

* An environment that's too noisy to the point it interrupts the system taking in audio input from the user.

* **When will X break?**

* A) False negative / False positive - When X fails to classify a correct piece or mistakenly sees a wrong piece as correct, due to unconsidered variance while training the model, or similarities between differetn steps;
B) Audio recognition failure - When X fails to accurately & timely recognize the user's spoken words.

* **When it breaks how will X break?**

* X will give wrong feedback (false negative / false positive); Or when it's a audio failure, it won't react to the user's aduio cues when it should.

* **What are other properties/behaviors of X?**

* The CV classification process of X is triggered by user's audio cues. When the users says "I'm done/good/okay", it feeds what it sees to the CV classification model and performs its judging duties.

* **How does X feel?**

* It feels like a camera hanging over your desk/table/working station like a lamp, watching your hand movements. It also feels like a devices listening to what you say and waiting to react.


**\*\*\*Include a short video demonstrating the answers to these questions.\*\*\***

**Developer test of the device from step 1 to step 6:**

https://user-images.githubusercontent.com/42874337/141044704-0b051b61-2a2c-4616-9e94-31991041ce7d.mp4



### Part 2.

#### Feedback

From the feedback we received from our classmates and peers, we have concluded a few common opinion:

1. If the users are expected to be blindfolded (or with visual impairment), how to let them know what's the visual field of the camera so that they will keep their working space intact? (We have included a new physical prototype in 3D printing that would be able to be placed under a tray that indicate the designed working space.)

2. What if my hand is also in the visual field, will that influence the accuracy? (We have also included hand in our training sample, as well as instruct our users to put their hand afar when the device examine the progress of the origami, which would be able to address this issue.)

**3D printing model of our new prototype:**

![image](https://user-images.githubusercontent.com/42874337/140666412-97c1d666-4e35-4b64-b6ff-dad966aca5b9.png)
![image](https://user-images.githubusercontent.com/42874337/140666436-b81ecc32-aef7-41d4-b366-accb504f7a58.png)

https://user-images.githubusercontent.com/42874337/140666580-1146364c-2343-46e5-8977-bff88106447c.mp4

**Since the device is too big to print, we divided it into two parts that can be assemblied afterwards:**

![image](https://user-images.githubusercontent.com/42874337/140668380-bfd8174d-fc9a-4731-baa8-433ec396e9a6.png)

![image](https://user-images.githubusercontent.com/42874337/140668512-30e1df49-ef41-4665-971d-5866dd6c01b6.png)

**Since the 3D printer is lack of material this whole week in MakerLAB, we cannot actually print it out before submission. Thus we utilized our initial prototype to finish this lab at this moment. However, we'd like to include the new model once it's been printed.**


![979b6a7e812043975b2755d5ef0e442](https://user-images.githubusercontent.com/42874337/141044100-3f6566c6-39aa-4036-8a48-ca0dd8a422ef.jpg)

### User tests 

In order to create a realistic testing environment and collect meaningful feedback, we recruited a participant who is neither in the IDD class or exposed to the whole process.

We asked the participant to **cover her eyes**, to fully imitate what a visually impaired user would feel.

> An interesting point the participant raised while we are explaining the process to her is that, actual visually impaired users might have a sharper sense of the environment that us. It could be hard for able-sighted people to adjust to this setting and find this system useful.

We drawed a few problems from our observation of the testing process.

#### User Test Video


https://user-images.githubusercontent.com/37056925/141142591-86b48854-d4db-42be-9c34-13352516a407.mp4


https://user-images.githubusercontent.com/37056925/141145055-783dab5c-6f6e-4c33-8757-26e1f0e3c034.mp4



#### Problems We Found

Though the participant generally understood the instructions and was able to follow along, but we did found a few problems in our observation.

1. When it comes to using Computer Vision, there are always **more details** that are required in a origami step that we can think of beforehand. 

* In order for a image of a step's ending product to be recognized as correct, the orientation in which the piece is placed needs to be considered and taken into account while training the model. **Some of our steps is lacking multi-orientation variance, and this is something to consider in future steps towards a final project (should it adopt a similar observant system)**.

2. **The robustness of the "alternative" interaction medium is essential for an accessibility centric system.**

* In our case, we wanted to substitue user’s visual input/outputs in the origami learning process with CV + audio communication; the audio communication is how the observant system communicate with the user, so it would need to be very robust for the system to work smoothly. 

* Unfortunately, the audio input methods for our Raspberry Pi is not working ideally. The microphone often fails to take in audio from the user, thus it commonly took multiple attempts for the user to indicate to the system that they are done with the current step.

* Towards the end of this process, we started questioning the rationality of choosing audio as the method for users to cue the system for step correctness check. There are two ways of information transmission in this design, system to user and user to system. **Audio is necessary for the system delivering message to the user, but is it really a good idea for the other way around? What if we just gave users a button to press?** Afterall, robustness is key as stated before, and audio is not the best choice in this sense.


<br>

The practices in this lab provided us with helpful insights on our thinking process for the final project.

We've always been interested in accessibility and sense-enhancing topics & designes in general, and want to build something for our finals somewhere down this track.

P.S. Maybe someday we can help anyone learn how to make a paper butterfly for their loved ones.

![pbutterfly](https://user-images.githubusercontent.com/37056925/141156073-b17b2a5c-7278-49b2-a78f-21ddf1da4787.jpeg)
