# from InstagramAPI import InstagramAPI, json, requests
# import time
# from datetime import datetime
#
# from instaRest import InstagramClient
# url = 'https://www.instagram.com/p/Bg6TBRLgKbic9ObnhsV9bS-h1SbxzmQqika30w0/?taken-by=furkankykc'
#
# # stop conditions, the script will end when first of them will be true
# until_date = '2017-03-31'
# count = 100
# def get_media_id(url):
#     req = requests.get('https://api.instagram.com/oembed/?url={}'.format(url))
#     media_id = req.json()['media_id']
#     return media_id
#
# def get_self_followers():
#     followers = api.LastJson
#     print (followers)
#
# def getLikedMedia(media_id=1745791455609267938):
#     results = []
#     api.getMediaLikers(media_id)
#     posts = api.LastJson.get('users', [])
#     for post in posts:
#         print(post.get('username'))
#         results.append(post.get('username'))
#     return results
# if __name__ == "__main__":
#     # api.login()
#     # api.getSelfUserFollowers()
#     # # user_id = '1461295173'
#     # user_id = api.username_id
#
#     myClient = InstagramClient(username,password)
#     list = myClient.get_followers()
#     for i  in list:
#         print(i+"\n")
#     #print("statussss = ",list['page_size'])
#     myClient.get_userInfo(23)

# '
#
#
