import pymysql

db_host = 'instance-proyect-mintic.cdyc0ucs6ghp.us-east-1.rds.amazonaws.com'
db_user = 'felaponte'
db_password = 'pandora0706'
db_database = 'db_proy'
db_table = 'users'

def connectionSQL():
    try:
        connection_sql = pymysql.connect(
            host = db_host,
            user = db_user,
            password = db_password,
            database = db_database
        )
        print('succesfull connection to database')
        return connection_sql
    except:
        print('Error connecting to database')
        return None 

def add_user(id, name, ownername, ownerlastname, birthday, animal, breed):
    instruction_sql =  "INSERT INTO " + db_table + \
    " (id, name, ownername, ownerlastname, birthday, animal, breed) Values ("\
    +id+", '"+name+"', '"+ownername+"', '"+ownerlastname+"', '"+birthday+"', '"+animal+"', '"+breed+"')" 
    connection_sql = connectionSQL()
    try:
        if connection_sql != None:
           cursor = connection_sql.cursor()
           cursor.execute(instruction_sql)
           connection_sql.commit()
           print("user added")
        else:
            print('Error connecting to database')
    except:
        print("error creting user")