# -*- coding: utf-8 -*-
"""
Created on Sat May 25 19:39:05 2019

@author: ME DELL'
"""

import ibm_db

dsn_hostname = "" # e.g.: "dashdb-txn-sbox-yp-dal09-04.services.dal.bluemix.net"
dsn_uid = ""        # e.g. "abc12345"
dsn_pwd = ""      # e.g. "7dBZ3wWt9XN6$o0J"

dsn_driver = "{IBM DB2 ODBC DRIVER}"
dsn_database = "BLUDB"            # e.g. "BLUDB"
dsn_port = "50000"                # e.g. "50000" 
dsn_protocol = "TCPIP"            # i.e. "TCPIP"

dsn = (
    "DRIVER={0};"
    "DATABASE={1};"
    "HOSTNAME={2};"
    "PORT={3};"
    "PROTOCOL={4};"
    "UID={5};"
    "PWD={6};").format(dsn_driver, dsn_database, dsn_hostname, dsn_port, dsn_protocol, dsn_uid, dsn_pwd)

#print the connection string to check correct values are specified
print(dsn)


try:
    conn = ibm_db.connect(dsn, "", "")
    print ("Connected to database: ", dsn_database, "as user: ", dsn_uid, "on host: ", dsn_hostname)

except:
    print ("Unable to connect: ", ibm_db.conn_errormsg() )
    
createQuery = "create table REVIEW(USERNAME VARCHAR(20) PRIMARY KEY NOT NULL, FNAME VARCHAR(20), LNAME VARCHAR(20), REVIEWS VARCHAR(100), SENTIMENT VARCHAR(20))"
#Now fill in the name of the method and execute the statement
createStmt = ibm_db.exec_immediate(conn, createQuery)

ibm_db.close(conn)
