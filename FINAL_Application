#import libraries
import botometer
import tweepy
from textblob import TextBlob
import pandas as pd
import numpy as np
import re
import matplotlib.pyplot as plt
import tkinter as tk
from PIL import Image,ImageTk

plt.style.use('fivethirtyeight')

#twitter_handle_input = input("Enter a twitter handle to be checked: ")

window = tk.Tk()
window.title("SW Mini Project")
window.geometry("700x500")

def button_handler():
    twitter_handle_input = entry.get()
    text = tk.Text(master=window,height=5,width=30)
    text.grid(column=1,row=5)
    #text.insert(tk.END,final)

    #API Keys
    Consumer_Key =  'Fg3XpAGkG4DT4e3PxGKqQt73Y'
    Consumer_Secret = 'M1wf2rj4prbam8t9cVykR8ykKmruWdzLRzixfMlDd4XfR9TElI'
    Access_Token = '1569770373687967744-atAYRutU9QAk6k9G8UJHO6ZKTAg8pK'
    Access_Token_Secret = '8v6JzlBfdNDZzXXn5lKW4Fq1M36GYoRGYm1uihOqKHkw0'

    #Authenticate to Twitter
    auth = tweepy.OAuthHandler(Consumer_Key, Consumer_Secret)
    auth.set_access_token(Access_Token, Access_Token_Secret)
    api = tweepy.API(auth, wait_on_rate_limit = True)

    #Botometer authentication
    rapidapi_key = "edbd4ef82cmsh451f77e71d3ce33p16e014jsn78dd29491688"
    bom = botometer.Botometer(wait_on_ratelimit=True,
                              rapidapi_key=rapidapi_key,
                              consumer_key = Consumer_Key,
                              consumer_secret= Consumer_Secret,
                              Access_Token = Access_Token,
                              Access_Token_Secret = Access_Token_Secret)

    #user inputs twitter handle
    #twitter_handle_input = input("Enter a twitter handle to be checked: ")

    # Check a single account by screen name and print score
    result = bom.check_account(twitter_handle_input)
    cap = result['cap']
    overall = cap['english']

    print("Botometer score: " + str(overall))
    if overall >= 3:
       final=twitter_handle_input + " is most likely a bot" + "\n"
       print(twitter_handle_input + " is most likely a bot" + "\n")
    elif overall <=2:
        final=twitter_handle_input + " is most likely not a bot" + "\n"
        print(twitter_handle_input + " is most likely not a bot" + "\n")
    else:
        final=twitter_handle_input + " is hard to classify as a bot or not" + "\n"
        print(twitter_handle_input + " is hard to classify as a bot or not" + "\n")


    #Extract 100 tweets from twitter user
    posts = api.user_timeline(screen_name = twitter_handle_input, count = 100, lang ="en", tweet_mode="extended")
    #Print last 5 tweets from the account
    print("Here are the 5 most recent tweets by " + twitter_handle_input + ": \n")
    i = 1
    for tweet in posts [0:5]:
        print(str(i) + ') ' + tweet.full_text + '\n')
        i = i + 1

    #Create a dataframe with a column called Tweets
    df = pd.DataFrame( [tweet.full_text for tweet in posts] , columns=['Tweets'])
    #Show the first tweets
    #print(df.head())

    #Clean the text
    def cleanTxt(text):
        text = re.sub(r'@[A-Za-z0-9_]+', '', text) #Removes @mentions
        text = re.sub(r'#', '', text) #Removes # symbol
        text = re.sub(r'RT[\s]+', '', text) #Removes RT
        text = re.sub(r'https?:\/\/\S+', '', text) #Removes Hyperlink

        return text

    #Cleaning text
    df['Tweets'] = df['Tweets'].apply(cleanTxt)
    #print(df)

    #Function to get subjectivity
    def getSubjectivity(text):
        return TextBlob(text).sentiment.subjectivity
    #Function to get polarity
    def getPolarity(text):
        return TextBlob(text).sentiment.polarity
    #Create two new columns
    df['Subjectivity'] = df['Tweets'].apply(getSubjectivity)
    df['Polarity'] = df['Tweets'].apply(getPolarity)
    #Dataframe with new columns
    print("Sentiment Analysis of the last 100 tweets: \n")
    #print(df)

    #Positive, Neutral, and Negative Sentiment
    def getSentiment(score):
        if score < 0:
            return 'Negative'
        elif score ==0:
            return 'Neutral'
        else:
            return 'Positive'

    df ['Sentiment'] = df['Polarity'].apply(getSentiment)
    print(df)

    text.insert(tk.END,final)

    #Sentiment Analysis Visualization
    df['Sentiment'].value_counts()
    plt.title('Sentiment Analysis')
    plt.xlabel('Sentiment')
    plt.ylabel('Counts')
    df['Sentiment'].value_counts().plot(kind ='bar')
    plt.tight_layout()
    plt.show()


label1 = tk.Label(text ="Botometer and Sentiment Analysis", font=("Times new roman",20))
label1.grid(column=0,row=0, padx=20, pady=20)

label2 = tk.Label(text ="Enter the twitter handle: ", font=("Times new roman",15))
label2.grid(column=0,row=1, padx=10, pady=10)

button=tk.Button(window,text="Check (Bots/Sentiment)",command=button_handler,bg="red")
button.grid(column=0,row=2, padx=10, pady=10)

entry = tk.Entry()
entry.grid(column=1,row=1, padx=20, pady=20)

image=Image.open('twitter_image.jpg')
image.thumbnail((300,300),Image.ANTIALIAS)
photo=ImageTk.PhotoImage(image)
label_image=tk.Label(image=photo)
label_image.grid(column=0,row=5)

window.mainloop()
