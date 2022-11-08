import json 
with open("user.json") as user:
     data = json.load(user)
     print(data[0]["title"])
     
for x in range(5):
    print(data[x]["title"])
    print(data[x]["body"])
    print("\n")
    
