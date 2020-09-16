import requests

# response=requests.get("http://45.144.65.25/getAllChatByUser/",headers={'Authorization':'Token c3c5acabc8024152fa643229f5e5b52aae07c1cc'})
# print(response.json())

# response=requests.post("http://45.144.65.25/signin/",data={'username':'hello','password':'123'})
# print(response.json())



# response=requests.post("http://45.144.65.25/createChat/",headers={'Authorization':'Token c3c5acabc8024152fa643229f5e5b52aae07c1cc'},data={'name':'123'})
# print(response.json())


# response=requests.get("http://45.144.65.25/getMessagesByChatId/",headers={'Authorization':'Token c3c5acabc8024152fa643229f5e5b52aae07c1cc'},data={'chatId':'35'})
# print(response.json())



# response=requests.post("http://45.144.65.25/createMessage/",headers={'Authorization':'Token c3c5acabc8024152fa643229f5e5b52aae07c1cc'},data={'chatId':'35','text':'LUBLU PROGATI'})
# print(response.json())


# response=requests.get("http://45.144.65.25/users/",headers={'Authorization':'Token c3c5acabc8024152fa643229f5e5b52aae07c1cc'})
# print(response.json())

response=requests.post("http://45.144.65.25/addUserToChatByUsername/",headers={'Authorization':'Token c3c5acabc8024152fa643229f5e5b52aae07c1cc'},data={'chatId': '39',"username": "g2323rey123"})
print(response.json())

# changeUsername