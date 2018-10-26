#! /usr/bin/env python

#You should install facepy API to use this $pip install facepy
#Specify your api key and birthday date
oath_token='EAACEdEose0cBAMeiWBwRhTcZBZC2DefVShst2bFEnBj8XiRnOp8gHcUBqcPcfFUx2f3CTqiQr7Ur0B6LhMIWOZBcrD8gGXZCZAcItXUVFwiZCr3yw5H9RKhnu2o60Q99JqLPfbKix2IXIu1YuzVYJNQthQ5V3xhKX3M6aPQOI3nzxWBxDkRLn8XbCQVv6tVZCru5RZBrCYHonRKOa13M0PXmObR1LvIKbwVaIpEgZCVf9zAZDZD'
my_birth_day = '1986-11-26T00:00:00+0530' #in ISO 8601 format ex: 2012-05-21T00:00:00+0000

#You need not change any code below this line
from facepy import GraphAPI
from dateutil import parser
import json
import random

#Intialize the graph API
graph = GraphAPI(oath_token)

#some variables specific to the app
my_facebook_id = graph.get('me')['id'].encode('utf-8')
print("my_facebook_id : {}".format(my_facebook_id))
my_birth_date = parser.parse(my_birth_day)
fetchMoreFeeds = True
feedLink = "me/feed"
posts = []
bD_strings = set(["happy", "b'day", "bday", "birthday"])
thank_you_notes = [
    "A friend like you is the nicest gift from life. Thank you for your birthday greeting :)",
    "Another year is left behind and we must move forward. Your birthday greeting was cool. Thank you :)",
    "Messages such as yours make me feel happy about my birthday. Thank you :)",
    "I look at my birthday messages. Thank you all for remembering such a special day for me",
    "Thank you for your birthday wishes",
    "I greatly appreciate your birthday wishes. Your friendship has always meant so much to me"
]

def getPost(feeds):
    """
    Function to get individual post from the feeds,
    It adds the post to an array @posts if
             * it is addressed to the user
             * after the birthday until now
             * user didn't commented already
             * contains wishing words like happy, birthday
    """
    global fetchMoreFeeds
    for feed in feeds['data']:
                #skip if this is not a post/message
        if not feed.has_key("message"):
            continue
        print("feed : {}\n".format(feed))
        #skip if this is my own post
        if feed['id'].encode('utf-8') == my_facebook_id:
            continue
        created_date = parser.parse(feed['created_time'])
        #Stop the loop and return if this post is older than my birthday
        if created_date.__lt__(my_birth_date):
            fetchMoreFeeds = False
            return
        #Skip if the post is not addressed to me
        if feed['to']['data'][0]['id'].encode('utf-8') != my_facebook_id:
            continue
        message = feed['message'].encode('utf-8').lower()
        #if the post already has comments skip it
        if feed['comments']['count'] > 0:
            continue
        #If message has any of the birthday words add the post to map
        if bD_strings.intersection(set(message.split())).__len__() > 0:
            post = {}
            post['id'] = feed['id']
            post['url'] = feed['actions'][0]['link']
            post['sender_name'] = feed['from']['name'].encode('utf-8')
            post['sender_id'] = feed['from']['id'].encode('utf-8')
            posts.append(post)

    #Get the next set of posts(pagination)
    feedLink = feeds['paging']['next'].replace('https://graph.facebook.com/', '')
    return feedLink

# Get the feeds till the birthday
while fetchMoreFeeds:
    feeds = graph.get(feedLink)
    feedLink = getPost(feeds)

#Now select a random thanking note and comment on the post
for post in posts:
    post_link = str(post['id']) + '/comments'
    thank_note  = thank_you_notes[random.randint(0, len(thank_you_notes) -1) ]
    graph.post(post_link, message=thank_note)
print "Wished %s .." % (post['sender_name'])
