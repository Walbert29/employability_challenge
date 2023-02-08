# Employability Challenge
Created users have the ability to search for vacancies that fit their profile based on the skills they add when they create their account. Additionally, the user's application to it can be stored in the database.

## Installation
The installation and execution of this program is quite simple, the processes to be carried out are listed below.

1. Previous requirements:
For the correct execution of the system it is necessary to install dependencies such as:
* Fastapi: Framework used to create endpoints.
* SQLAlchemy - The set of tools for manipulating the database.
* Dotenv: Used for the database connection.
* Numpy: Used to generate matches

2. Download:
To download it, just clone the repository on github

3. Installation:
To install the system and run it either locally or in a production environment, once the repository has been cloned, run the command:
```
pip -r requirements.py
```
to install all necessary dependencies, another way to run it is by generating a docker image with the provided Dockerfield, using the command:
```
docker build -t name:tag location_docker_field
```

Once the docker image is generated, it is possible to execute the line:
```
docker run -it name:tag
```
to start the service

## Use
A quick guide to use this development is described below.

Features:

**Module User**
* Search information of a user based on his ID: It is possible to see the information stored of a user in the database, sending the User ID of this.
* Search information of a user based on his Email: It is possible to see the information stored of a user in the database, sending the Email of this.
* Update User: User information is highly updateable except for sensitive fields like email and User ID.
* Create User: The creation of the user is completely open, however, it has the protection that the User ID is generated automatically.

**Module Vacancy**

* Create Vacancy: Like the creation of users, the creation of the vacancy is allowed freely, except for the self-generated ID.
* Search vacancy by ID: It is possible to see all the information of a vacancy sent by its ID.
* Delete job: Jobs can be removed as long as you have the ID from which you want to remove them.

**Module Employability**

* Search for matches: This functionality is mainly responsible for finding those vacancies that match the skills of a user.

**Module Application**
* Search for applications from a user: This functionality is responsible for returning to which vacancies a person has applied with their respective information.

* Search applications for a vacancy: This functionality is responsible for finding which users have applied for a vacancy and displaying their information.