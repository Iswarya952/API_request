import requests
#GET REQUEST
response=requests.get("https://jsonplaceholder.typicode.com/posts")
print(response)
print(response.status_code)
print(response.json())
#Filtering the data
params={"userId":2}
response=requests.get("https://jsonplaceholder.typicode.com/posts",params)
print(response.json())