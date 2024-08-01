import requests

class GAssistantAPI:
    def __init__(self, base_url:str, token:str=None):
        self.base_url = base_url if base_url.endswith("/") else base_url + "/"
        self.session = requests.Session()
        self.token = token
        self.headers = {
            "Accept": "application/json"
        }
        self.session.headers.update(self.headers)
        self.auth = self.Auth(self)
        self.project = self.Project(self)
        self.statistics = self.Statistics(self)

    def set_token(self, token):
        self.token = token
        header = {
            "Authorization": "Bearer " + token
        }
        self.session.headers.update(header)


    class Auth:
        def __init__(self,gapi = None):
            self.api = GAssistantAPI() if gapi is None else gapi

        def login(self, username, password, fcm_token):
            url = self.api.base_url + "auth/login"
            payload = {
                "username": username,
                "password": password,
                "fcm_token": fcm_token
            }
            response = self.api.session.post(url, json=payload)

            if response.status_code == requests.codes.OK:
                token = response.json().get("access_token")
                self.api.set_token(token)
            return response.json()

        def ping_token(self):
            url = self.api.base_url + "auth/ping-token"
            response = self.api.session.get(url)
            return response.json()

        def logout(self):
            url = self.api.base_url + "auth/logout"
            response = self.api.session.post(url)
            return response.json()


    class Project:
        def __init__(self,gapi = None):
            self.api = GAssistantAPI() if gapi is None else gapi

        def index(self):
            url = self.api.base_url + "projects"
            response = self.api.session.get(url)
            return response.json()
        
        def show(self,id):
            url = self.api.base_url + "projects/" + str(id)
            response = self.api.session.get(url)
            return response.json()
        
        def data(self,id):
            url = self.api.base_url + "project-data/" + str(id)
            response = self.api.session.get(url)
            return response.json()
        
        def store(self,title,device_key):
            url = self.api.base_url + "projects"
            payload = {
                "title": title,
                "device_key": device_key
            }

            response = self.api.session.post(url, json=payload)
            return response.json()
        
        def update(self,id,title,device_key,
                   description,interval,start_date,
                   end_date,status):
            url = self.api.base_url + "projects/"+str(id)
            payload = {
                "title": title,
                "device_key": device_key,
                "description": description,
                "interval": interval,
                "start_date": start_date,
                "end_date": end_date,
                "status": status
            }

            response = self.api.session.put(url,json=payload)
            return response.json()
        
        def delete(self,id):
            url = self.api.session.base_url + "projects/" + str(id)
            response = self.api.session.delete(url)
            return response.json()
        
    class Statistics:
        def __init__(self,gapi = None):
            self.api = GAssistantAPI() if gapi is None else gapi

        def store_data(self,device_key,temperatures,
                       humidities,lights,moistures,P):
            
            url = self.api.base_url + "data"
            payload = {
                "device_key": device_key,
                "T": temperatures,
                "H": humidities,
                "L": lights,
                "M": moistures,
                "P": P
            }
            response = self.api.session.post(url, json=payload)
            return response.json()
        
        def store_image(self,camera_key,image):
            url = self.api.base_url + "image"
            payload = {
                "camera_key": camera_key
            }
            files = {
                "img": ("image.jpeg",image,"image/jpeg"),
                "camera_key": (None,camera_key)
            }
            response = self.api.session.post(url, files=files)
            return response.json()

        def ping(self):
            url = self.api.base_url + "ping"
            response = self.api.session.get(url)
            return response.json()
