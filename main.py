import time,cv2
from modules import Capture,GAssistantAPI

capture = Capture(0)
api = GAssistantAPI(base_url="https://gassistant.insoulit.com/api")

# login to GASSistant
username="user@user.com"
password="topsecret"
fcm_token="dVNlWsamR76pypJY6sts1_:APA91bHjDgENiSd6gnYms2TB3zPyeqPda4Pf05RTTxqpx0kWB-zQuqqUPQosTNX0SHgmAgxPxf1n1LvHgmoNyOwXbKzztWnFy_Lygk4YKCdm0bPhws6PS0e7zsNCannKD8dqLtbu_sd-"
api.auth.login(username=username, password=password, fcm_token=fcm_token)


while True:
    try:
        img = capture.image()
        _,img_encode = cv2.imencode('.jpeg', img)
        img_bytes = img_encode.tobytes()
        response = api.statistics.store_image(camera_key="aCPeaY8K4p1EYMzqyTRoEX2gNktOyOoXg3c08Gxi",image=img_bytes)
        response2 = api.statistics.store_data("PY5WGkoHwu4azEYOKmL51S3g6WEUKKKPAw6JCs3V",27,32,33,23,2)
        print(response,response2)
        time.sleep(30)
        # break
    except Exception as e:
        print("Encountered exception",str(e))
        time.sleep(5)

capture.clear()