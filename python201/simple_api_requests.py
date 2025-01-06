import requests
import time

while True:
    req = requests.get("https://github.com/PBelle451")
    print(req.status_code)
    if req.status_code != 200:
        # Add a function here
        pass
    time.sleep(3)