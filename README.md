# tahoe- URL generator application

### geturl is django project

### url generator is app where templates and views will be found.

### api is app where wrapper api is written to communicate with appspot api.

How to run it on docker locally:
1. Build container from tahoe directory

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