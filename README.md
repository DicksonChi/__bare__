# __bare__
* [Dependencies](#dependencies)
* [Installation](#installation)
* [Running Locally](#running)
* [Justification](#justification)

## Dependencies

This project makes use of these dependencies:

* Python 3.7 - Programming language for backend development
* Flask Framework

## Installation
```
$ git clone git@github.com:DicksonChi/__bare__.git
$ cd __bare__
$ make venv
$ source venv/bin/activate
```

##### TO INSTALL REQUIREMENTS
`$ make requirements`


## Running

##### TO RUN BACKEND
`$ make migrate_task` to migrate task from csv to the database
 
`$ make run` or to run in the background
`$ make run_backgound`


## Justification
SQLite was used as database because of the size of the records in the task_data.scv file

Flask was used as the web framework because of the lightness of the framework and also the project requirements. Using  django 
will be too large for this small project

#### How it works.
1. The migrate_task_data handles the creation of every record of the task in the DB.

2. The database created in (1) is what is used here as the DB for this web app that is connecting to the server

3. At every get request to the home endpoint the list of the task is return and it is logged that the
record was requested for  