import requests

from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser
from rest_framework.views import APIView

from service import appspot


class UploadImage(APIView):
    parser_classes = [MultiPartParser]

    def post(self,request,*filename,**format):

        if request.method == 'POST' and is_request_authenticated(request):
            
            uploaded_file = request.data.get('file')

            if is_valid_image_file(uploaded_file):
                data = upload_image(uploaded_file)

                if data:
                    return Response({"url": data}, status = 200)
                    
                return Response({"message": "The file is not valid. Please check", "code": "BAD REQUEST"},status=400)     
            return Response({"message": "The file is not valid. Please check", "code": "BAD REQUEST"},status=400)
        return Response({"message": "Not valid authentication credentials", "code": "Unauthorized request"},status=401)         

    @classmethod
    def get_extra_actions(cls):
        return []

def is_valid_image_file(file)-> bool:
    file_name = file.name
    ext = file_name.split(".")[-1]
    allowed_ext=["jpg","jpeg","png","tif","tiff","gif","heic","svg"]

    if ext in allowed_ext:
        return True

    return False

def upload_image(file):
    response = appspot.get_response(file)

    return response


def is_request_authenticated(request) -> bool:
    token = get_access_token(request)

    if not token:
        return False
    
    email = get_user_email(token)
    return "@findfilo.com" in email
    

def get_user_email(token):
    response = requests.request("GET",f"https://www.googleapis.com/oauth2/v2/userinfo?access_token={token}")
    user_data = response.json()
    email = user_data.get('email', [])

    return email

        
def get_access_token(request):
    return request.headers.get("Authorization")        