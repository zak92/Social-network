# Social-network

Final Coursework Project for Advanced Web Development (University of London)

## How to run the application

1. Open the git bash terminal in the VS Code editor.

2. Navigate to the directory containing the source code.

3. Activate the virtual environment:

`source sn_venv/Scripts/activate`

4. Install Python packages with pip and requirements.txt

`pip install -r requirements.txt`

4. Navigate to the project directory

`cd social_network`

5. Start the server

`python manage.py runserver 127.0.0.1:8080`

6. Navigate to the landing page of the application by navigating to the following address:

http://127.0.0.1:8080/home

7. To access the web sockets web page, click on the ‘Live Chat Rooms’ menu item in the navigation bar on the home page or visit the following address:

http://127.0.0.1:8080/websockets/

To access the above page, ensure that you are logged in.

8. To access the four API endpoints I have created, navigate to the following pages:

http://127.0.0.1:8080/api/users/

http://127.0.0.1:8080/api/user/admin/

http://127.0.0.1:8080/api/groups/

http://127.0.0.1:8080/api/group/Test/

## Login credentials of the admin user

- Username: admin
- Password: abc123

## How to run the unit tests

1. Open the git bash terminal in the VS Code editor.

2. Navigate to the directory containing the source code.

3. Activate the virtual environment:

`source sn_venv/Scripts/activate`

4. Navigate to the project directory

`cd social_network`

5. Run the tests

a) Run only the API tests contained in the rest_api directory

`python manage.py test rest_api/tests/`

b) Run only the tests contained in the snapp directory

`python manage.py test snapp/tests/`

c) Run ALL tests

`python manage.py test`
