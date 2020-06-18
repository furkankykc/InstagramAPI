import time
import urllib.request
from random import randint

from InstagramAPI import InstagramAPI
import sys, json, os
import requests

class InstagramClient(object):
    def __init__(self, username, password):
        # Attempt authentication
        try:
            if (self, username != None and password != None):
                self.username = username
                self.password = password
                self.api = InstagramAPI(username, password)
                self.api.login()
                print(self, "Login was successful for ", self.username)
            else:
                return
        except:
            print(self, "Error: Authentication Failed")
    def getValueFromJson(self,json,value):
        try:
            return json[value]
        finally:
            return ""
    def getSelfPost(self):
        return self.getPosts(self.api.username_id)
    def getPosts(self, userid):
        list = []
        self.api.getSelfUserFeed()
        for post in self.api.LastJson['items']:
            try:

                id = post['id']
                if post['caption'] is not None:
                    caption = post['caption']['text']
                else:
                    caption = ""
                print (post)
                if post['image_versions2'] is not None:
                    image = post['image_versions2']['candidates'][0]['url']
                else:
                    image = ""
                list.append([id, caption, image])
            except:
                continue
        return list


    def followSomeOne(self, username):
        self.api.follow(self.get_userID(username))
        if self.api.LastJson['status'] == 'ok':
            return True
        else:
            return False
    def getFollowers(self):
        self.api.getSelfUserFollowers()
        return (self.api.LastJson['users'])

    def getFollowings(self):
        self.api.getSelfUsersFollowing()
        return (self.api.LastJson['users'])


    def getProfileInfo(self, username):
        self.api.getUsernameInfo(self.get_userID(username))
        profilePicture = self.api.LastJson['user']['profile_pic_url']
        fullName = self.api.LastJson['user']['full_name']
        isPrivate = self.api.LastJson['user']['is_private']
        mediaCount = self.api.LastJson['user']['media_count']
        isPrivate = self.api.LastJson['user']['is_private']
        followerCount = self.api.LastJson['user']['follower_count']
        followingCount = self.api.LastJson['user']['following_count']
        biography = self.api.LastJson['user']['biography']
        return locals()
    def getRequests(self):
        self.api.getSelfUsernameInfo()
        print(self.api.LastJson)
    def upload(self, list):
        for l in list:
            print("Now Uploading this photo to instagram: " + l[1])

            urllib.request.urlretrieve(self,
                                       l[2],
                                       'temp.jpg')
            self.api.uploadPhoto('temp.jpg', l[0])
            n = randint(5, 10)
            print("Sleep upload for seconds: " + str(n))
            time.sleep(n)

    def deleteAllMedia(self):
        for media in self.getFeed(self, self.api.username_id):
            self.api.deleteMedia(self, media[0])
        return

    def getFeed(self, userid):
        list = []
        self.api.getUserFeed(self, userid)
        # print(self.api.LastJson)

        for post in self.api.LastJson['items']:

            print(post['caption']['text'])
            print(post['image_versions2']['candidates'][0]['url'])
            list.append([post['id'], post['caption']['text'], post['image_versions2']['candidates'][0]['url']])

        return list

    def get_userID(self, username):
        self.api.searchUsername(username)
        try:
            return self.api.LastJson["user"]["pk"]
        except Exception:
            print("username doesn't exist")
            return False

    def register(self, username, password):

        return


#
if __name__ == "__main__":
    api = InstagramClient("furkankykc", "############")
    #print(api.getFollowers())
    #print (api.getProfileInfo("cubbelimehmedefendi"))

    for i in (api.getPosts(api.api.username_id)):
        print(i)

#     user_id = '1461295173'
#     user_id = self.api.username_id
#     # Alternatively, use the code below
#     # (self,check evaluation.evaluate_user_followers for further details).
#     # posts = getPosts(self,self.api,1461295173)
#     # info = getUsernameInfo(self,self.api,1461295173)
#     # list = getFeed(self,get_userID(self,'inonuitiraflar'))
#     # print (self,len(self,list))
#     # upload(self,list)
#     deleteAllMedia(self,)
#     print (self,get_userID(self,'furkankykc'))
