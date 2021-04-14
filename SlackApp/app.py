import requests
import json
import numpy as np
import time

def send_data(text):
    WEBHOOK = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
    data = {"text":text}
    headers = {'content-type': 'application/json'}
    res = requests.post(WEBHOOK, data=json.dumps(data), headers=headers)
    print(res.text)

if __name__ == '__main__':
    try:
        start = time.time()
        A = np.arange(1000000).reshape(250,4000)
        B = np.arange(1000000).reshape(250,4000)
        AB = A*B
        time.sleep(2)
        end = time.time()
        totalTime = str(end - start)
        msg = "time taken is" + totalTime
        send_data(str(msg))
    except:
        msg = "Error in the script!"
        send_data(str(msg))