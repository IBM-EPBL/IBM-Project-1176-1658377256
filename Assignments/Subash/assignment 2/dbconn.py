import ibm_db
def display(conn):
    sql="SELECT * FROM USER"
    stmt = ibm_db.exec_immediate(conn,sql)
    dictionary = ibm_db.fetch_both(stmt)
    while dictionary != False:
        print ("The roll no is : ",  dictionary["ROLLNO"])
        print ("The Name is : ", dictionary["USERNAME"])
        print ("The Email no is : ",  dictionary["EMAIL"])
        print ("The Password is : ", dictionary["PASSWORD"],"\n")
        dictionary = ibm_db.fetch_both(stmt)


def Insert(conn,rollno,name,email,password):
   sql="INSERT INTO USER VALUES('{}','{}','{}','{}')".format(rollno,name,email,password)
   stmt=ibm_db.exec_immediate(conn,sql)
   print("The Number if affected rows: ", ibm_db.num_rows(stmt),"\n")


def Update(conn,rollno,name,email,password):
   sql="UPDATE Users SET  ROLLNO ='{}',  WHERE USERNAME='{};".format(rollno,name)
   stmt=ibm_db.exec_immediate(conn,sql)
   print("The Number if affected rows: ", ibm_db.num_rows(stmt),"\n")

try:
    conn=ibm_db.connect("DATABASE=bludb;HOSTNAME=2f3279a5-73d1-4859-88f0-a6c3e6b4b907.c3n41cmd0nqnrk39u98g.databases.appdomain.cloud;PORT=30756;SECURITY=SSL; SSLServerCertificateDigiCertGlobalRootCA.crt;PROTOCOL=TCPIP;UID=nhl80748;PWD=3yD0G9e6VuQHsOBX;", "", "")
    print("connection Success")
    display(conn)
    Insert(conn,"6213192026","navin raj","winN@gmail.com","euyfuis")
    display(conn)
    
except:
    print("couldn't connect")