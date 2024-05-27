#  We're NOT special </br>
**Table of content**

1. Concept
2. Used software
3. The code
4. Set up installation
5. Be aware
6. Overall experience
</br> 

##  Concept
With the 'We're NOT Special' installation, you leave your unique silhouette on the screen. This way, everyone who passes by can leave their mark, creating a collective work of art that embodies inclusivity. Because inclusivity is important in society, this interactive multimedia installation shows that everyone is unique in their own way, yet we are all just people, and one is not better than the other. </br> </br>

##  Used software
We used the following languages: Python, JavaScript, HTML and CSS. 
We also used the following libraries and modules: OpenCV, MediaPipe, NumPy, Time en Pygame </br> </br>

## The code
*Disclaimer: I had never used Python before, so I had to rely on YouTube tutorials and ChatGPT.*

I started my project with the following tutorial: Body Segmentation Tutorial. This tutorial is about body segmentation. After following the tutorial, you will have a code that segments your body silhouette.

The video does not show you how to download Python or the necessary libraries, so I will.

**Step 1:** Download Python from this site. I recommend version 3.8, 64-bit.

**Step 2:** Create a virtual environment. It is good practice to use a virtual environment for Python projects. By doing so, you create an isolated environment and ensure your project remains unaffected by changes made to other projects. To create a virtual environment, open the terminal and type:
<code style="color : aquamarine">python -m venv myenv</code> </br>

(myenv is the name for the environment; you can choose any name you like). You will get a notification; you can click "yes." Now, our environment is created, but it has yet to be activated. To activate it, type the following in the terminal: 
<code style="color : aquamarine">myenv\Scripts\activate</code> </br>

You should see the name of your environment at the beginning of the path in your terminal, indicating that you are inside the environment. Don't forget to activate the environment every time you open your project!

Now that we have Python and a virtual environment, you can start installing packages.</br>

**Step 3:** Install OpenCV. Open the terminal in your project directory and type: <code style="color : aquamarine">pip install opencv-python</code> </br>
(By the way, this should also install NumPy, so you normally shouldn't need to install it separately.)</br>

**Step 4:** Install MediaPipe. Go to the terminal and type:</br> 
<code style="color : aquamarine">pip install mediapipe</code> </br>

You should be able to run the code, and this should be the result: “INSERT PHOTO”.

So now we have our base, but this is only the beginning. Let’s move on to the next steps!

We need a random color generator; in this case, I want pastel-ish colors. Each silhouette should get its own unique color. We also want to add a sound every time the camera detects a person, and we want to take pictures and save them in the public folder. I would love to explain how to do this step by step, but as I already stated, I’m a beginner myself, so I’m not able to do so. You'll get the full code in the BodyDet.py file anyway.

You do have to install one last library for the sound. Let’s install PyGame. Go to the terminal and type:</br>
<code style="color : aquamarine">pip3 install pygame</code> </br>
Everything should work now. Do you face some problems? Google, YouTube, and ChatGPT are your best friends :3.

But wait! That’s not all! We have to display the taken images of our silhouettes!

I created a HTML file with a canvas and some text, the images are being displayed inside the canvas. I use Vite, so you don’t have to use a live server. To set it up, go to the terminal and type: </br>
<code style="color : aquamarine">npm install</code> </br>

After it installs, type: </br>
<code style="color : aquamarine">npm run dev</code> </br>

This will give you a localhost server that automatically refreshes.

We should also create a CSS file where we style the canvas and the text.

Last but not least, we should create a JavaScript file where we import the images and position them. We also need to make it automatically reload every few seconds. I positioned the images horizontally next to each other, but you can change the positioning to suit your preference.

These codes are also provided. You should not face any problems with these codes.

## Set up installation

I'm going to share how I set up my installation on the day I had to present it. I thought I was doing it correctly, but I realized too late that I wasn't. However, I learned from the mistake and now know how to do it better in the future. So, how did I do it?

# INSERT IMAGE SKETCH

**What I used:**

1. Laptop
2. External camera
3. Projector
4. White material
5. Whiteboard with stand

I was originally planning to use a Raspberry Pi, and I tried to do so. But there was one problem: it was so slow! It couldn’t run my Python code and the HTML server at the same time. It crashed every single time I tried. I'm not sure what the problem was—whether the Raspberry Pi was slow on its own and there was nothing I could do, or there was a way to make it faster that my teacher and I didn't know about. We did try various solutions, but nothing worked. If you have experience with Raspberry Pi and know how to prevent it from lagging, I would 1000% recommend using it. But if you don't have one or yours also has performance issues, you can just use your laptop to run the code. </br>

I had the option to set up my installation in either a classroom or a hallway. I chose the hallway so people could easily pass by the installation. Little did I know this was the wrong choice. I wanted to place it across the width of the hallway, but the walls were too close together for the projector. So, I had to set it up along the length of the hallway. As a result, the whole hallway was visible in the background, which caused the system to detect random objects as people, and the special sound played continuously. </br>
