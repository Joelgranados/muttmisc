import requests
import uuid

class TodoistAPI:
    endpoint=""
    token=""

    def post(self, d):
        header = { "Content-Type" : "application/json",
                  "X-Request-Id" : str(uuid.uuid1()),
                  "Authorization" :"Bearer %s" % self.token }
        r = requests.post(self.endpoint, data = d, headers = header)
        return r

class TodoistTask(TodoistAPI):
    def __init__(self, token):
        self.token = token
        self.endpoint = "https://api.todoist.com/rest/v1/tasks"



