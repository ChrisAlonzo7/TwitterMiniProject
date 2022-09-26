# TwitterMiniProject
App that detects whether a user is a bot or not as well as sentiment of their last 100 tweets. 

General notes:
1. We have two different versions for the front end. The first is a basic python console app. In order to test the app, run the botandsentiment.py file. This will require the user to enter a valid Twitter handle, which will then return the botometer score as well as the subjectivity, polarity, and overall sentiment of the last 100 tweets from the Twitter handle entered. 
The result should look like this with @elonmusk as an example:
![elonmuskexample](https://user-images.githubusercontent.com/73143256/192187208-3490eb69-1132-4f13-a2fc-25bd89196e1d.PNG)

2. We tried using the React Native framework with the Google Firebase app development software. But, we were unable to put all the different files togther to produce the user interface. We also had no experience in using React Native nor Firebase. Hence, we used a python desktop application implemented using the Tkinter python library as our second UI. This library renders the GUI. The user enters the twitter handle through the desktop app and we display whether the acoount is a bot or not. The rest of the information is displayed on the console. Run the FINAL_Application file. A sample code for the UI is also provided (FrontEnd_Desktop_App_Sample file). Please make sure you have the twitter_image.jpg file in the same directory since we used the image on our UI.
<img width="522" alt="Screenshot 2022-09-26 034614" src="https://user-images.githubusercontent.com/74872762/192221529-3efbd3ad-f2e3-4324-a7fb-2a057ea736ac.png">

3. The coding was entirely done in Python scripting language with the help of various libraries and APIs. 




