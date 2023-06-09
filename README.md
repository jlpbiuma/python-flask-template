# Python Flask Server

0. Run the server with the following command:

```
python app.py
```

1. Set this template for a new GitHub project
2. Create a virtual environment using:

```
python -m venv myenv
```

3. Activate the Python environment:

```
source myenv/bin/activate (Linux/MacOS)
myenv\Scripts\activate (Windows)
```

4. Run the following command to install all dependencies:

```
pip install -r requirements.txt
```

5. Install the dependencies of your project and update the requirements.txt with the following command:

```
pip freeze > requirements.txt
```

6. You can modify the app.py to use debug setting the property 'debug' True

```python
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
```

## Dockerfile

1. To create the docker image of this project run:

```
docker build -t <image-name> .
```

2. To build the image and start the new container run this command:

```
docker run -d --name <container-name> <image-name>
```

## Example requests:

Try the following request:

```
[GET]http://127.0.0.1:5000/api/example_resource/exampleGET
[POST]http://127.0.0.1:5000/api/example_resource/examplePOST
```

Note: If this requests works, the server is correctly working
