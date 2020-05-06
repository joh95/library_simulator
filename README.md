# Script: Create Table Postgresql into Docker

### Command line into docker postgres container

- docker exec -it library psql -U library : Entry container postgres
- \l : list Databases
- \c library : Use the database library
- CREATE TABLE book (
    id serial PRIMARY KEY,
    name varchar (50) NOT NULL,
    literary_genre varchar (50),
    author varchar (50),
    year varchar (4),
    price varchar (10));

- exit 


