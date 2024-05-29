#  We're NOT special </br>
**Table of content**

1. Concept
2. Used software
3. The code
4. Set up installation
5. Be aware
6. Overall experience
</br></br>


##  Concept
With the 'We're NOT Special' installation, you leave your unique silhouette on the screen. This way, everyone who passes by can leave their mark, creating a collective work of art that embodies inclusivity. Because inclusivity is important in society, this interactive multimedia installation shows that everyone is unique in their own way, yet we are all just people, and one is not better than the other. </br> </br></br>

##  Used software
**We used the following languages:** </br> 
* Python
* JavaScript
* HTML
* CSS </br>

**We also used the following libraries and modules:** </br> 
* OpenCV
* MediaPipe
* NumPy
* Time
* Pygame </br> </br> </br>


## The code
*(Disclaimer: I had never used Python before, so I had to rely on YouTube tutorials and ChatGPT.)*

I started my project with the following tutorial: [Body Segmentation Tutorial](https://www.youtube.com/watch?v=IZEkwUJ6QGQ&list=LL&index=1&t=122s). This tutorial is about body segmentation. After following the tutorial, you will have a code that segments your body silhouette. The video does not show you how to download Python or the necessary libraries, so I will.

### Step 1:
Download Python from [this site](https://www.python.org/downloads/). I recommend version 3.8, 64-bit. </br> </br>

### Step 2:
Create a virtual environment. It is good practice to use a virtual environment for Python projects. By doing so, you create an isolated environment and ensure your project remains unaffected by changes made to other projects. To create a virtual environment, open the terminal and type:</br>

````sh
python -m venv myenv
```` 
###### (btw, myenv is the name for the environment; you can choose any name you like.)  </br> 


You will get a notification; you can click "yes." </br> </br>
<img src="/public/env_notification.png" alt="notification you get" width="350" height="auto"> </br>

Now, our environment is created, but it has yet to be activated. To activate it, type the following in the terminal: </br>

````sh
python -m venv myenv
```` 

You should see the name of your environment at the beginning of the path in your terminal, indicating that you are inside the environment. Don't forget to activate the environment every time you open your project! </br> </br>
<img src="/public/myenv.png" alt="how you can tell that u'r inside the envirment" width="auto" height="20">

Now that we have Python and a virtual environment, you can start installing packages.</br> </br>

### Step 3:
Install OpenCV. Open the terminal in your project and type: </br> 
````sh
pip install opencv-python
```` 
###### By the way, this should also install NumPy, so you normally shouldn't need to install it separately. </br> </br>

### Step 4: 
Install MediaPipe. Go to the terminal and type:</br> 
````sh
pip install mediapipe
```` 

You should be able to run the code, and this should be the result: </br>

<img src="/public/pycode.jpg" alt="pycode body segmentation result" width="auto" height="300">

So now we have our base, but this is only the beginning. Let’s move on to the next steps!

We need a random color generator; in this case, I want pastel-ish colors. Each silhouette should get its own unique color. We also want to add a sound every time the camera detects a person, and we want to take pictures and save them in the public folder. I would love to explain how to do this step by step, but as I already stated, I’m a beginner myself, so I’m not able to do so. You can find the full code in the "BodyDet.py" file.</br></br>

### Step 5: 
Now we have to install the last library, PyGame. Go to the terminal and type:</br>

````sh
pip3 install pygame
```` 
</br>

Everything should work now. Incase you DO face some problems, *Google, YouTube, and ChatGPT are your best friends :3*

But wait! That’s not all- We have to display the taken images of our silhouettes!

I created a HTML file with a canvas and some text, the images are being displayed inside the canvas. I use [Vite](https://www.educative.io/answers/what-is-vitejs), so you don’t have to use live server. To set it up, go to the terminal and type: </br>

````sh
npm install
```` 
</br>

After it installs, type: </br>
````sh
npm run dev
```` 
</br>

This gives you a localhost server that automatically refreshes.

I also created a CSS file to style the canvas and the text.

And last but not least, I created a JavaScript file to import and position the images. I positioned them horizontally next to each other, but you can change the positioning to suit your preference. I also made the page reload every few seconds.


## Set up installation

Setting up my installation didn't go as smoothly as I thought it would. So, I'm going to tell you how I did it and how you should do it to achieve the best result.


<img src="/public/og_setting.jpg" alt="image of my set up" width="auto" height="240">


<p float="left">
  <img src="/public/installation-img-1.jpg" width="272" /> 
  <img src="/public/installation-img-2.jpg" width="272" />
  <img src="/public/installation-img-3.jpg" width="272" /> 
</p>

**What I used:**

1. Laptop
2. External camera
3. Projector
4. White fabric
5. Whiteboard with stand

#### raspberry pi
I was originally planning to use a Raspberry Pi, and I tried to do so. But there was one problem: it was SO slow! It couldn’t run my Python code and the HTML server at the same time. It crashed every single time I tried. I'm not sure what the problem was—whether the Raspberry Pi was just very slow and there was nothing I could do, or if there was a way to make it faster that my teacher and I didn't know about. We tried various "solutions" but nothing worked. If you have experience with Raspberry Pi and know how to prevent it from lagging, I would 100% recommend using it. But if you don't have one or if it also has performance issues, you can just use your laptop to run the code. </br>

#### location
I had the option to set up my installation in either a classroom or a hallway. I chose the hallway so people could easily pass by the installation. Little did I know that this would be the wrong choice. I wanted to place it across the width of the hallway, but the walls were too close together for the projector. So, I had to set it up along the length of the hallway. As a result, the entire hallway was visible in the background. I tried to improve the setup by hanging a large white cloth over a standing whiteboard, leaving only a small space for the person trying the installation. This was supposed to stop the code from identifying background objects as people. It helped, but didn't fully solve the problem because objects were STILL being detected through the small open space, causing the system to detect random objects as people and continuously play the special sound. </br>

#### projector
The next problem was the projector. It wouldn't have been a problem if I could have installed it on the ceiling. Taping it wasn't an option either because it was too heavy. So, I had to place it on a chair, connected to my laptop. The person trying the installation had to stand to the side of the hallway since the projector was in the middle. This made the experience less pleasant. </br>

#### frame
The last problem was that we wanted to create a wooden frame and place it around the projection, mimicking a real painting in a museum. However, it was impossible because the frame was too large for the wood cutter. T.T</br>

Okay, I made it sound very bad, but it actually wasn’t! It just didn't turn out the way we wanted. Surprisingly, an orthopedagogical professional actually liked the installation and asked me to collaborate and use it at an event next year! xD > </br>

### So, what will I do differently next time? </br>

**What I will use:**
* Raspberry Pi
* external camera
* projector
* frame.

I will give Raspberry Pi another chance, tho i'm sure ill need a better one, maybe use raspberry pi 5 instead of 4? I will also somehow hang the projector. I will also ensure that the location has a fully white or plain-colored background. Additionally, I will put a wooden frame around the projection like a real piece of art. I will order the size i need or cut the wood myself instead of laser cutting it. The person should also be able to stand anywhere within the zone that the camera takes. <sup>yeah.. the solution is not that cheap</sup> </br>

<img src="/public/new_setting.jpg" alt="image of how the set up should be" width="auto" height="240">

### Set up installation- code wise


**step 1** Run the HTML with: <br> 
````sh
npm run dev
```` 
</br>

**step 2** Then run your Python code (it is normal for it to take a little while). </br>
**step 3** Make the browser full screen, and ta-da, it's ready.  </br>


## Be aware

You won’t see any images displayed if you delete even one; there should always be 20 images. Do you want a different number, like 15 or 25? Then you will have to adjust the Python and JavaScript code. Here’s how you do it: </br>

Change the 20 to whatever number you want in your Python code:</br>

![piece of code](/public/pycode_screen.png) </br>


In your JavaScript code, add or remove images in the const imagePositions array: </br>

![piece of code](/public/jscode_screen.png) </br>

## So, how was my experience overall?

It was quite an interesting project. There were moments when I felt like pulling out all my hair, and there were moments that made me happy for finally fixing whatever problem I had. Honestly, I didn’t learn as much as I had hoped, but I did gain some experience with Python, learned what a virtual environment is, and found myself using terminal more than ever before.</br>

We wanted the silhouettes to have random prints originally, but we couldn't make it work. So, we went with colors instead. That's the only downside; otherwise, I'm happy with how everything else turned out in the code.</br>

The installation itself didn’t go exactly as we wanted, but it’s alright. We still managed to impress a special guest.</br>

## Thank you </br>
Thanks for sticking with me this far! Feel free to use this project if it's helpful to you.