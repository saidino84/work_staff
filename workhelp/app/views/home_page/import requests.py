import requests

reqUrl = "https://saidinosecondapp.herokuapp.com/getmercearia/5"

headersList = {
 
}

payload = ""

response = requests.request("GET", reqUrl, data=payload,  headers=headersList)

print(response.text)