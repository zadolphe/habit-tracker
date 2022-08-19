import requests
import datetime

pixelaPostEndpoint = "https://pixe.la/v1/users"
token = "zadolphetoken"
username = "zadolphe"
graphId = "graph1"
dateTime = datetime.datetime.now()
currentDay = str(dateTime.day)
currentYear = str(dateTime.year)
currentMonth = str(dateTime.month)
currentDate = currentYear+"0"+currentMonth+currentDay
#print(currentDate)



#currentDate = currentDate.split('-')


#we need to create a user first 
#required parameters from documenation 
user_params = {
    "token": token,
    "username": username,
    "agreeTermsOfService": "yes", 
    "notMinor": "yes"
}

#response = requests.post(url=pixelaPostEndpoint, json=user_params)
#print(response.text)
#we successfully created a user getting a 200 response, now it says 409 bc user already exists

#create a graph 
graphEndpoint = f"{pixelaPostEndpoint}/{username}/graphs"
#this wil now use headers http method, need the user token as the header of the post  
headers = {
    "X-USER-TOKEN": token
}
#request body 
body_params = {
    "id": graphId, 
    "name": "liftingGraph", 
    "unit": "kg",
    "type": "int",
    "color": "sora"
}
#post the graph 
#graphResponse = requests.post(url=graphEndpoint, headers=headers, json=body_params)
#print(graphResponse.text)

#post value to the graph 
postValueEndpoint = f"{pixelaPostEndpoint}/{username}/graphs/{graphId}"
#required header and body
postValueBody = {
    "date": currentDate, 
    "quantity": "145"
}
postValueResponse = requests.post(url=postValueEndpoint, headers=headers ,json=postValueBody)
print(postValueResponse.text)