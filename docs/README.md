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

![image of my set up](/public/og_setting.jpg)

**What I used:**

1. Laptop
2. External camera
3. Projector
4. White material
5. Whiteboard with stand

I was originally planning to use a Raspberry Pi, and I tried to do so. But there was one problem: it was so slow! It couldn’t run my Python code and the HTML server at the same time. It crashed every single time I tried. I'm not sure what the problem was—whether the Raspberry Pi was slow on its own and there was nothing I could do, or there was a way to make it faster that my teacher and I didn't know about. We did try various solutions, but nothing worked. If you have experience with Raspberry Pi and know how to prevent it from lagging, I would 1000% recommend using it. But if you don't have one or yours also has performance issues, you can just use your laptop to run the code. </br>

I had the option to set up my installation in either a classroom or a hallway. I chose the hallway so people could easily pass by the installation. Little did I know this was the wrong choice. I wanted to place it across the width of the hallway, but the walls were too close together for the projector. So, I had to set it up along the length of the hallway. As a result, the whole hallway was visible in the background, which caused the system to detect random objects as people, and the special sound played continuously. </br>

The next problem was the projector. It wouldn't have been an issue if I could have installed it on the ceiling. Taping it wasn't an option either because it was too heavy. So, I had to place it on a chair, connected to my laptop. The person trying the installation had to stand to the side of the hallway since the projector was in the middle, which made the experience less pleasant. </br>

I tried to improve the setup by hanging a large white cloth over a standing whiteboard, leaving only a small space for the person trying the installation. This was supposed to stop the code from identifying background objects as people. It helped, but didn't fully solve the problem because objects were still being detected through the small open space.</br>

The last issue was that we wanted to make a frame from thin wood and place it around the projection, like a real painting in a museum. However, this wasn't possible because the frame was too large for the wood cutter. T.T</br>

Okay, I made it sound very bad, but it actually wasn’t! Just not the way we wanted. An orthopedagogy professional actually liked the installation and asked me to collaborate and use it at an event next year. </br>

**So, what will I do differently next time?** </br>

What I will use: Raspberry Pi/laptop, external camera, projector/big monitor, and a frame.

I will give the Raspberry Pi another chance. It would be great if it works without crashing, but if it still crashes, I'll use a laptop hidden from public view. I will hang the projector if possible; if not, I'll use a big monitor to display the output. I will also ensure the location has a fully white or plain-colored background. Additionally, I will frame the output like a real piece of art. The person should be able to stand anywhere within the zone that the camera covers. </br>

![image of how the set up should be](/public/new_setting.jpg)

**How do you actually set it up**

1. Run the HTML with: <br> 
<code style="color : aquamarine">npm run dev</code> </br>
2. Then run your Python code (it is normal for it to take a little while).
3. Make the browser full screen, and ta-da, it's ready.  </br>

How you make the surroundings look good is up to you. I recommend doing it the way I plan to next time.</br> 

## Be aware

You won’t see any images displayed if you delete even one; there should always be 20 images. Do you want a different number, like 15 or 25? Then you will have to adjust the Python and JavaScript code. Here’s how to do it: </br>

In your Python code, change:</br>

![piece of code](/public/pycode_screen.png) </br>

Change the 20 to whatever number you want. </br>

In your JavaScript code, add or remove images in the const imagePositions array: </br>

![piece of code](/public/jscode_screen.png) </br>

## So, how was my experience overall?

It was an interesting project. There were moments that made me want to pluck all my hair out, and there were moments that made me happy for finally fixing whatever problem I had. To be honest, I didn’t learn a lot, but I did gain some experience with Python. I learned what a virtual environment is, and I used the terminal more than ever before.</br>

We originally wanted the silhouettes to have random prints, but we weren’t able to achieve that, so we used colors instead. That’s the only con; I’m happy with everything else code-wise.</br>

The installation itself didn’t go exactly as we wanted, but it’s alright. We still managed to impress a special guest, who liked it and wants to use our installation at an event.</br>

## Thank you </br>
Thank you for reading this far. I hope you enjoyed it, and you are more than welcome to use this project.