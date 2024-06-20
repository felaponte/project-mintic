import pymysql

db_host = 'instance-proyect-mintic.cdyc0ucs6ghp.us-east-1.rds.amazonaws.com'
db_user = 'felaponte'
db_password = 'pandora0706'
db_database = 'db_proy'
db_table = 'pets'

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
           return True
        else:
            print('Error connecting to database')
    except:
        print("error creting user")

def consult_user(id):
    instruction_sql= "SELECT * FROM pets WHERE id = "+ id
    connection_sql = connectionSQL()
    try:
        cursor = connection_sql.cursor()
        cursor.execute(instruction_sql)
        result_data = cursor.fetchall()
        return(result_data)
    except Exception as err:
        print("Error", err)
        return False