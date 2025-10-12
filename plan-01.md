 Todo App
 - what is the app? definition and description --> app is a directory contains everything. and it has an empty file ``app/__init__.py``, so it is a "Python package". `app.`
 - who are the users? elaboration --> the users are users, wich are defined in the the app under the file module ``users.py``
 - what are the activities performed in the app? bc, ac, rc
    - business activities [bc] --> These are operational tasks like data entry, transaction processing, and workflow management that support day-to-day business functions. They ensure the smooth execution of organizational processes within the app.
    - audit activities [ac] --> These involve verifying data accuracy, tracking user actions, and ensuring compliance with policies or standards. They help maintain transparency, accountability, and data integrity in the system.
    - reporting activities --> These focus on generating summaries, dashboards, and analytical reports from collected data. They help users make informed decisions by visualizing trends and performance metrics.
 - scope of the app? --> The app’s scope defines what functions, users, and processes it covers — such as business operations, auditing, and reporting. It sets the boundaries and objectives of what the application is designed to achieve.


Actors: --> Actors are our Roles in this section
 - USER 
 - MANAGER
 - ADMIN
  
ENTITIES: --> TASKs and PROJECTs are our INTITIES, Objects that must be created on the user’s side.
 - TASK
 - PROJECT

MODEL:
 - USERS [WITH ROLES]
  -  id:  adfsasdf
  -  .....
  - ROLES
    - USER
    - MANAGER
    - ADMIN
 - TASK
 - PROJECT

RELATIONS:
- PROJECTS [MANY-ONE] MANAGER --> one MANAGER can manage many Projects
- TASK [MANY-ONE] MANAGER --> MANAGER can own many TASKS
- TASK [MANY-ONE] PROJECTS --> One PROJECT can have many TASKs
- TASK [MANY-ONE] USER --> One USER can do many TASKs

API GROUPS:
- USER [roles => user, manager, admin] [PROTECT]
   - CREATE [POST] --> USERs can only created by a ADMIN
      - ADMIN 
   - UPDATE [PUT/PATCH] --> USERs with ADMIN Roles can update all USERs Creadntials, but USER can only update their own credentials
      - ADMIN
      - OWN USER
   - DELETE [DELETE] --> USERs with ADMIN Roles can delete all credentials, but Users with Roles of USER can only delete their own credentials
      - ADMIN
      - OWN USER
   - READ  [GET] --> USERs with ADMIN Roles can read all credentials, but Users with Roles of USER can only read their own credentials
      - ADMIN
      - OWN USER

- PROJECT
   - CREATE [POST] --> ADMIN can create any PROJECT, MANAGER can create only thier own PROJECTS
      - ADMIN [ FOR ALL]
      - MANAGER  [ OWN PROJECTS]
   - UPDATE [PUT/PATCH] --> All PROJECTS can updated by ADMIN and MANAGERs can update only thier own PROJECT.
      - ADMIN [ FOR ALL]
      - MANAGER  [ OWN PROJECTS]
   - DELETE [DELETE] ---> All PROJECTS can deleted by ADMIN and MANAGERs can delete only thier own PROJECT. 
      - ADMIN [ FOR ALL]
      - MANAGER  [ OWN PROJECTS]
   - READ [GET] --> All PROJECTS can be read by ADMIN, MANAGERs and USER.
      - ADMIN [ALL]
      - MANAGER  [ALL]
      - USER [ALL]

- SCHEMAS [RESPONSE AND REQUEST]