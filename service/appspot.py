import requests
import json


def get_response(file):
    api = 'https://filo-295211.el.r.appspot.com/upload_file'
    payload = {'bucket': 'filo-misc-images'}
    file = {'file':file}
    response = requests.request("POST", api, data=payload, files=file)

    if response.status_code==200:
        data = response.content
        json_data = data.decode('utf8')
        data_dict = json.loads(json_data)
        url = data_dict.get("url")
        url = url.replace("http://","https://")
        return url

    return