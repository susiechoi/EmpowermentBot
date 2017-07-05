'''
Created on May 6, 2017

@author: Susie Choi

All code closely follows the code presented in parts one and two of busterroni11's
(extremely helpful) "How to Make a Reddit Bot" tutorial series.
Part one: https://youtu.be/krTUf7BpTc0
Part two: https://youtu.be/A6rTvlgLUWk
'''

import praw
import config
import os

def botLogin():
    print "Now: Logging in"
    reddit = praw.Reddit(username = config.username,
                password = config.password,
                client_id = config.client_id,
                client_secret = config.client_secret,
                user_agent = "susBotTest's AsianFeminism comment grabber")
    return reddit

def runBot(reddit, commentsGrabbed):
    print "Now: Getting 25 post replies"
    for reply in reddit.subreddit("AsianFeminism").comments():
        if "confidence" in reply.body:
            if reply.id not in commentsGrabbed:
        # if replying to commments, add above: and not reply.author == reddit.user.me():
                print "We found the string 'confidence' in this comment: "+reply.body
                commentsGrabbed.append(reply.id)
                with open("CommentsGrabbedFromAsianFem.txt","a") as theFile: # a is append
                    theFile.write(reply.id + "\n")
    print commentsGrabbed

def getCommentsGrabbed():
    if not os.path.isfile("CommentsGrabbedFromAsianFem.txt"):
        commentsGrabbed = []
    else:
        with open("CommentsGrabbedFromAsianFem.txt","r") as theFile: #r is read
            commentsGrabbed = theFile.read()
            commentsGrabbed = commentsGrabbed.split("\n")
            commentsGrabbed = filter(None, commentsGrabbed)
    return commentsGrabbed

# main
reddit = botLogin();
commentsGrabbed = getCommentsGrabbed()
print commentsGrabbed
runBot(reddit, commentsGrabbed)
