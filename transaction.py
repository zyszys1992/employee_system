#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  3 17:42:43 2018

@author: yishanzhang

This python script is for making transaction where we insert partons' last and 
first name, and employess ID, transaction date.

This file can be executed by "python newtables.py -h YOUR_HOST_NAME, -p YOUR_PORT_NUMBER,
-d YOUR_DB_NAME, -u YOUR_USERNAME, -D DATE_OF_TRANSACTION, -e EMPLOYEEID, -l LASTNAME_PATRON
, -f FIRSTNAME_PATRON" 
"""

import psycopg2, getpass, argparse


def make_transaction(host,port,user,dbname,Date,EmployeeID,LastName,FirstName):
    connection = psycopg2.connect(
    host=host,
    port=port,
    user=user,
    password=getpass.getpass('password: '),
    dbname=dbname)
    cur=connection.cursor()
    query='''INSERT INTO Transactions(Date,EmployeeID,LastName,FirstName) VALUES (%s,%d,%s,%s)'''
    a,b=cur.execute(query,(Date,EmployeeID,LastName,FirstName,)),connection.commit()
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
    
    date="the date of transaction"
    parser.add_argument("-D", "--date", help=date, required=True)
    
    employeeid="the ID of employee who checked out the book to patrons"
    parser.add_argument("-e", "--employeeid", help=employeeid, required=True)
    
    lastname="The Last Name of patron who borrowed the book"
    parser.add_argument("-l", "--lastname", help=lastname, required=True)
    
    firstname="The First Name of the parton who borrowed the book"
    parser.add_argument("-f", "--firstname", help=firstname, required=True)
    

    return parser.parse_args()

if __name__=="__main__":
    args = parse_args()
    make_transaction(host=args.host,port=args.port,user=args.user,dbname=args.dbname,
                 Date=args.date,EmployeeID=args.employeeid, LastName=args.lastname,
                 FirstName=args.firstname)
    