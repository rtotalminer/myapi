#  A Basic User Management System using FastAPI
**Work in progress!**

## Overview
This application should serve as a solid template to build any API that implenets authorisation and authenticaion, along with object–relational mapping using the package `peewee` which can easily build a controller to handle with CRUD requests.

## Running the application
<em>If you want to keep your code clean and avoid having to install packages on your host machine, I recommend a Python VM such as venv.</em>

Firstly, install the requirements:

```
pip install  requriements.txt 
```

Then launch the server - make sure your in the directory `../myapi/`:

```
uvicorn main:app --reload
```
