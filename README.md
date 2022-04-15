# URL generator application

### This project enables users to upload any image and in return users will get url of the image

### Project Detail:
1. User uploads an image and get url of image in webpage.

2. Google auth is incorporated in frontend.

3. When user uploads image, the image is wrapped up in body of POST API and POST API return url is user is authenticated.

3. API is also authenticated. Calling API from Postman won't work.

2. Backend API is authenticated, So only users who are logged in can only get url.


## Running the application on Local Machine:
1. From magicurl directory, Create Virtual Environment
```shell
python3 -m venv [name_of_virtual_env]
```

2. Install dependencies
```shell
pip install -r requirements.txt
```

3. Activate virtual environment
```shell
source venv/bin/activate
```

4. Run the application
```shell
python3 manage.py runserver --insecure
```




## Running on local machine through docker:
1. Build container from magicurl directory

```shell
docker build . -t django-dev
```     


2. Run command from tahoe directory
 
```shell
docker run -p 8083:8000 -it --rm django-dev
```    

3. cd into container

```shell
docker exec -it [container id] bash
```