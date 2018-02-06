#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  3 14:42:37 2018

@author: yishanzhang

documentation: Create 4 tables patrons, employees,books,transactions, where 

patrons and employees tables are parental tables to transaction table which has 

foreign key lastname and firstname from patrons and employeeid from employees.

Books table has PRIMARY KEY ISBN and FOREIGN KEY LastName and FirstName refered from 
Employees table. 

Usually, AWS RDS service is good choice so I use psycopg2 to connect the database 
in AWS RDS to execute. 

This file can be executed by "python newtables.py -h YOUR_HOST_NAME, -p YOUR_PORT_NUMBER,
-d YOUR_DB_NAME, -u YOUR_USERNAME" 
"""

import psycopg2, getpass, argparse

def get_connection(host,port,user,dbname):
    connection = psycopg2.connect(
    host=host,
    port=port,
    user=user,
    password=getpass.getpass('password: '),
    dbname=dbname)
    return connection

def create_table(host,port,user,dbname):
    
    d=dict(query_patrons=''' CREATE TABLE Patrons (LastName varchar(255),
    FirstName varchar(255),Address varchar(255), PRIMARY KEY (LastName, FirstName)); ''',
    
    query_employees='''CREATE TABLE Employees (LastName varchar(255),
    FirstName varchar(255),Address varchar(255),EmployeeID INT NOT NULL PRIMARY KEY, 
    CurrentSalary Numeric, ManagerID INT) ;''',
    
    query_books=''' CREATE TABLE Books (ISBN INT NOT NULL PRIMARY KEY, Name varchar(255), 
    LastName varchar(255),FirstName varchar(255),FOREIGN KEY (FirstName)
    REFERENCES Employees(FirstName),FOREIGN KEY (LastName)
    REFERENCES Employees (LastName));''',
    
    query_transactions=''' CREATE TABLE Transactions(Date DATETIME NOT NULL PRIMARY KEY, EmployeeID INT ,
    LastName varchar(255) ,FirstName varchar(255),
    FOREIGN KEY (LastName,FirstName)  REFERENCES Patrons(LastName, FirstName),
    FOREIGN KEY (EmployeeID) REFERENCES Employees(EmployeeID));''')
    
    conn=get_connection(host,port,user,dbname)
    cur=conn.cursor()
    for key in d:
        cur.execute(d[key])
    a=conn.commit()
    return a,cur.fetchall()

def parse_args():
    parser = argparse.ArgumentParser(add_help=False)

    host = "Endpoint of database"
    parser.add_argument("-h", "--host", help=host, required=True)

    port = "Port number of database"
    parser.add_argument("-p", "--port", help=port, required=True)

    user = "user name of database"
    parser.add_argument("-u", "--user", help=user, required=True)
    
    dbname="database name"
    parser.add_argument("-d", "--dbname", help=dbname, required=True)

    return parser.parse_args()

if __name__=="__main__":
    args = parse_args()
    create_table(host=args.host,port=args.port,user=args.user,dbname=args.dbname)