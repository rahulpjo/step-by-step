# Step By Step

## Project Description

Step By Step is a blog/social networking app with the mission of celebrating not the final product itself, but the steps to the final product. The app is meant for skill builders in any discipline to showcase the way they practice their skill and lets other users comment with praise or constructive criticism/tips.

## Project Stack

The project leverages React and Redux on the front-end with FastAPI on the server side, which is connected to a SQLite database via SQLAlchemy.

[React Documentation](https://reactjs.org/docs/getting-started.html)

[Redux Documentation](https://redux.js.org/introduction/getting-started)

[FastAPI Documentation](https://fastapi.tiangolo.com/)

[SQLite Documentation](https://www.sqlite.org/docs.html)

[SQLAlchemy Documentation](https://docs.sqlalchemy.org/en/14/)

## Directions

To get started with project, clone and enter the repository's backend folder to begin configuration:

```
git clone git@github.com:rahulpjo/step-by-step.git
cd step-by-step/backend
```

**Optional:** It's recommended to work on the project in a virtual environment so that packages don't need to be installed globally. Using venv and any directory name you choose, create and activate a virtual environment:

```
python3 -m venv ENV_DIR_NAME
source ./ENV_DIR_NAME/bin/activate
```

Install the dependencies using pip:

```
pip install -r requirements.txt
```

Create a blog.db file in the root folder

```
touch blog.db
```

To get your server running, run the following command:

```
uvicorn blog.main:app --reload
```

**Note:** `uvicorn` is an ASGI (Asynchronous Server Gateway Interface) server implementation. `blog.main` points Uvicorn to the module where the FastAPI instantiation is located. `app` is the name of the variable the FastAPI instantiation was assigned to. `--reload` is a flag that tells the server to reload upon saving (similar to nodemon for Node developers).
