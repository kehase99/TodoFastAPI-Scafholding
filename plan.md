 Todo App
 - what is the app? definition and description --> app is a directory contains everything. and it has an empty file ``app/__init__.py``, so it is a "Python package". `app.`
 - who are the users? elaboration --> the users are users, wich are defined in the the app under the file module ``users.py``
 - what are the activities performed in the app? bc, ac, rc
    - business activities [bc] --> These are operational tasks like data entry, transaction processing, and workflow management that support day-to-day business functions. They ensure the smooth execution of organizational processes within the app.
    - audit activities [ac] --> These involve verifying data accuracy, tracking user actions, and ensuring compliance with policies or standards. They help maintain transparency, accountability, and data integrity in the system.
    - reporting activities --> These focus on generating summaries, dashboards, and analytical reports from collected data. They help users make informed decisions by visualizing trends and performance metrics.
 - scope of the app? --> The app’s scope defines what functions, users, and processes it covers — such as business operations, auditing, and reporting. It sets the boundaries and objectives of what the application is designed to achieve.


Actors:  --> Actors are our Roles in this section
 - USER
 - MANAGER
 - ADMIN
  
ENTITIES: --> TASKs and PROJECTs are our INTITIES, Objects that must be created on the user’s side.
 - TASK
 - PROJECT

MODEL:
 - USERS [WITH ROLES]
  - ID: [id] .....
  - USERNAME: [username] ...
  - EMAIL: [email] ....
  - PASSWORD: [password] ....
  - Adress: [adress]
  - etc ....
  - ROLES: [role] ....
    - USER
    - MANAGER
    - ADMIN
  
 - TASK
   - task-id: [id]
   - task: [task type]
   - completed: [true or false]
   - time: [time]
   - priority:[priority]
   - rate: [rate]
  
 - PROJECT
   - project-ID: [ID]
   - project-Name: [Pname]
   - completed: [true or false]
   - time: [time]
   - priority:[priority]

RELATIONS:
- PROJECTS [MANY-ONE] MANAGER 
- TASK [MANY-ONE] MANAGER
- TASK [MANY-ONE] PROJECTS
- TASK [MANY-ONE] USER

API GROUPS:
- USER [roles => user, manager, admin] [PROTECT] [/users]
   - CREATE [POST] [/users]
      - ADMIN 
   - UPDATE [PUT/PATCH] [/users/<id>]
      - ADMIN
      - OWN USER
   - DELETE [DELETE] [/users/<id>]
      - ADMIN
      - OWN USER
   - READ  [GET] [/users/<id>]
      - ADMIN
      - OWN USER

- PROJECT  [/project]
   - CREATE [POST] [/project]
      - ADMIN [ FOR ALL]
      - MANAGER  [ OWN PROJECTS]
   - UPDATE [PUT/PATCH] [/project/<id>]
      - ADMIN [ FOR ALL]
      - MANAGER  [ OWN PROJECTS]
   - DELETE [DELETE] [/project/<id>]
      - ADMIN [ FOR ALL]
      - MANAGER  [ OWN PROJECTS]  
   - READ [GET] [/project/<id>]
      - ADMIN [ALL]
      - MANAGER  [ALL]
      - USER [ALL]
  
- TASK  [/task]
   - CREATE [POST] [/task]
      - ADMIN [ FOR ALL]
      - MANAGER  [ OWN PROJECTS]
   - UPDATE [PUT/PATCH] [/task/<id>]
      - ADMIN [ FOR ALL]
      - MANAGER  [ OWN PROJECTS]
   - DELETE [DELETE] [/task/<id>]
      - ADMIN [ FOR ALL]
      - MANAGER  [ OWN PROJECTS]  
   - READ [GET] [/task/<id>]
      - ADMIN [ALL]
      - MANAGER  [ALL]
      - USER [ALL]
  

- SCHEMAS [RESPONSE AND REQUEST]
  
  - USER [/user]
     - POST REQUEST [/user]: [ UserPostRequest] .....
       - username
       - email 
       - password
       - adress
     - POST RESPONSE [/user]: [ UserPostResponse] .....
       -  message
       -  status
       -  etc
     - UPDATE REQUEST [/user/<id>]: [ UserUpdateRequest] .....
       - username
       - email 
       - password
       - adress
     - UPDATE RESPONSE [/user/<id>]: [ UserUpdateResponse] .....
       -  message
       -  status
     - DELETE RESPONSE [/user/<id>]: [ UserUpdateResponse] .....
       -  message
       -  status
  
  - TASK [/task]
    - POST REQUEST [/task]: [ TaskPostRequest] .....
     - task
     - completed
     - time
     - priority
     - rate
    - UPDATE REQUEST [/task/<id>]: [ TaskUpdateRequest] .....
     - task
     - completed
     - time
     - priority
     - rate
    - POST RESPONSE [/task]: [ TaskPostRequest] .....
     - task
     - completed
     - time
     - priority
     - rate
    - UPDATE RESPONSE [/task/<id>]: [ TaskUpdateRequest] .....
     - task
     - completed
     - time
     - priority
     - rate
   - DELETE RESPONSE [/task/<id>]: [ TaskUpdateResponse] .....
      -  message
      -  status


  - PROJECT [/project]
    - POST REQUEST [/project]: [ ProjectPostRequest] .....
     - project-Name
     - completed
     - time
     - priority
  
  - PROJECT [/project]
    - UPDATE REQUEST [/project/<id>]: [ ProjectUpdateRequest] .....
     - project-Name
     - completed
     - time
     - priority
  - PROJECT [/project]
    - POST RESPONSE [/project]: [ ProjectPostResponse] .....
     - project-Name
     - completed
     - time
     - priority
  
  - PROJECT [/project]
    - UPDATE RESPONSE [/project/<id>]: [ ProjectUpdateResponse] .....
     - project-Name
     - completed
     - time
     - priority
   - DELETE RESPONSE [/project/<id>]: [ ProjectDeleteResponse] .....
     - message
     - status
  
- REPOSITORIES:
   ....coming soon..........

- SERVICES:
   ....coming soon..........

- DEPENDENCIES:
   ....coming soon..........

- TESTS:
  - INTEGRATION
  - UNIT TEST [ IN THE FEATURE] 
   ....coming soon..........

-  LIBRARIES:
```
   fastapi 
   uvicorn 
   bcrypt
   python-multipart
   pydantic
   pydantic-settings 
   requests
   motor 
   beanie 
   pyjwt
   python-jose[cryptography] 
   passlib[bcrypt] 
   pytest
   pre-commit
   ruff
   mypy
```

- SCAFFOLDING
```
todoApp
├─ .vscode/ 
│  ├─ extensions.json
│  ├─ launch.json  
│  └─ settings.json
├─ app/
│  │  ├─ __init__.py
│  ├─ core/
│  │  ├─ __init__.py
│  │  ├─ api.py   # routs            
│  │  ├─ config.py # configuration 
│  │  └─ db.py 
│  ├─ models/
│  │  ├─ __init__.py
│  │  ├─ user.py
│  │  ├─ project.py
│  │  └─ etc ...
│  ├─ schemas/
│  │  ├─ __init__.py
│  │  ├─ user.py
│  │  ├─ project.py
│  │  └─ etc ...
│  ├─ repositories/
│  │  ├─ __init__.py
│  │  └─ user_repo.py
│  ├─ services/
│  │  ├─ __init__.py
│  │  └─ user_service.py
│  └─ dependencies/
│     ├─ __init__.py
│     └─ auth.py
│     └─ common.py
├─ tests/
│  └─ test_users.py
├─ main.py
├─ __init__.py
├─ .env.example
├─ .pre-commit-config.yaml
├─ .mypy.ini
├─ .python-version
├─ ruff.toml
├─ uv.lock
├─ plan.md
├─ .gitignore
├─ pyproject.toml
├─ docker-compose.yml
├─ pytest.ini
└─ README.md
```