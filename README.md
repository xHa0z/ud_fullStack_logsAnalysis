## Log Analysis Project
This repo is to use python to analyze log that stores in a sql database

### queries.sql
It contains all necessary sql queries to execute the python correctly

### logs.py
It contains functions to answer the questions

## Run
To run this project 
* Run queries.sql first
``` bash
psql -d news -f queries.sql
```
* Execute python, result will be printed in the console
``` bash
python logs.py
```