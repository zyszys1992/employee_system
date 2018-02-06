#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  3 23:00:35 2018

@author: yishanzhang

For this python script, we record Employees.EmployeesID, Employees.CurrentSalary, 
Transaction.Date,where Employees are the authors of books 
who can borrow as many books as they want by using INNER JOIN.

This file can be executed by "python newtables.py -h YOUR_HOST_NAME, -p YOUR_PORT_NUMBER,
-d YOUR_DB_NAME, -u YOUR_USERNAME" 
"""
import psycopg2, getpass, argparse

def Employee_return(host,port,user,dbname,Date):
    query='''SELECT Employees.EmployeesID, Employees.CurrentSalary, Transaction.Date FROM 
    ((Transaction INNER JOIN Employees ON Transactions.EmployeeID=EmployeesID) 
    INNER JOIN Books ON Employees.LastName=Books.LastName 
    AND Employees.FirstName=Employees.FirstName));
    '''
    connection = psycopg2.connect(
    host=host,
    port=port,
    user=user,
    password=getpass.getpass('password: '),
    dbname=dbname)
    cur=connection.cursor()
    b=cur.execute(query)
    a=connection.commit()
    return a,b,cur.fetchall()

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
    Employee_return(host=args.host,port=args.port,user=args.user,dbname=args.dbname)