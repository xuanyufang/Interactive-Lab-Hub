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

For Contour detection, one of the design we 

#### Face Detection

https://user-images.githubusercontent.com/42874337/139736619-e3aa47b8-72d0-4348-b6fb-31b5b2f0332d.mp4

#### Optical Flow Detection

https://user-images.githubusercontent.com/42874337/139736625-f7acb244-3d1c-4682-ad84-89b718622e84.mp4

#### Object Detection

https://user-images.githubusercontent.com/42874337/139736633-1bad1e56-8ecf-461b-b775-3129f07acfb9.mp4



#### MediaPipe

**\*\*\*Consider how you might use this position based approach to create an interaction, and write how you might use it on either face, hand or body pose tracking.\*\*\***

(You might also consider how this notion of percentage control with hand tracking might be used in some of the physical UI you may have experimented with in the last lab, for instance in controlling a servo or rotary encoder.)





https://user-images.githubusercontent.com/42874337/139738761-2dae57e8-7501-4085-8b4b-93bf0cab7777.mp4




#### Teachable Machines

**\*\*\*Whether you make your own model or not, include screenshots of your use of Teachable Machines, and write how you might use this to create your own classifier. Include what different affordances this method brings, compared to the OpenCV or MediaPipe options.\*\*\***

https://user-images.githubusercontent.com/42874337/139780543-70c49a21-06ed-4c88-9450-a31383d4825b.mp4


We trained a model with Teachable Machines detecting different actions we can apply to a piece of paper. 


### Part B
### Construct a simple interaction.

Pick one of the models you have tried, pick a class of objects, and experiment with prototyping an interaction.
This can be as simple as the boat detector earlier.
Try out different interaction outputs and inputs.

**\*\*\*Describe and detail the interaction, as well as your experimentation here.\*\*\***

For this project we are planning to prototype an origami instruction device that can give out auditory instructions to users and recognize the origami process through a camera system as we have tested with teachable machine. 

This is a device that solely utilize auditory interactions on a spatial task, which can be expand to many fields. This device can be used to explore the idea of teaching people with visual disabilities to learn origami that instructed by machine. 

We have also tested with the hand gesture recognization that we altered the code to recognize a "thumbs up" gesture that representing completion as follows:

https://user-images.githubusercontent.com/42874337/139782983-a15d7282-03a8-49a0-a5e1-d46c100f58eb.mp4


### Part C
### Test the interaction prototype

Now flight test your interactive prototype and **note down your observations**:
For example:
1. When does it what it is supposed to do?
1. When does it fail?
1. When it fails, why does it fail?
1. Based on the behavior you have seen, what other scenarios could cause problems?

**\*\*\*Think about someone using the system. Describe how you think this will work.\*\*\***
1. Are they aware of the uncertainties in the system?
1. How bad would they be impacted by a miss classification?
1. How could change your interactive system to address this?
1. Are there optimizations you can try to do on your sense-making algorithm.

### Part D
### Characterize your own Observant system

Now that you have experimented with one or more of these sense-making systems **characterize their behavior**.
During the lecture, we mentioned questions to help characterize a material:
* What can you use X for?
* What is a good environment for X?
* What is a bad environment for X?
* When will X break?
* When it breaks how will X break?
* What are other properties/behaviors of X?
* How does X feel?

**\*\*\*Include a short video demonstrating the answers to these questions.\*\*\***

### Part 2.

Following exploration and reflection from Part 1, finish building your interactive system, and demonstrate it in use with a video.

**\*\*\*Include a short video demonstrating the finished result.\*\*\***


![image](https://user-images.githubusercontent.com/42874337/140666412-97c1d666-4e35-4b64-b6ff-dad966aca5b9.png)
![image](https://user-images.githubusercontent.com/42874337/140666436-b81ecc32-aef7-41d4-b366-accb504f7a58.png)

https://user-images.githubusercontent.com/42874337/140666580-1146364c-2343-46e5-8977-bff88106447c.mp4


![image](https://user-images.githubusercontent.com/42874337/140668380-bfd8174d-fc9a-4731-baa8-433ec396e9a6.png)

![image](https://user-images.githubusercontent.com/42874337/140668512-30e1df49-ef41-4665-971d-5866dd6c01b6.png)

