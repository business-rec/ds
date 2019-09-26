import json
import requests

# if you want to test local
# url = "http://localhost:9000"

# if you want to test deployed
url = "http://br-yelp-predict-rating.herokuapp.com"

val = {"category": 'Shopping',
       "review": "Service is okay but the wait time is too long."}

# you'll get a 200 response if the keys align
# and something bad if the keys don't align.
if __name__ == '__main__':
    r_success = requests.post(url, data=json.dumps(val))
    print(
        f"Request responded: {r_success}.\nResponse was\n{r_success.json()}")
