import boto3
from credentials.keys import ACCES_KEY, SECRET_KEY

bucket_name = "proy-vet-mintic"

def connection_s3() :
    try:
        session_aws = boto3.session.Session(ACCES_KEY, SECRET_KEY)
        s3_resource = session_aws.resource('s3')
        print("Connected to S3")
        return s3_resource
    except Exception as err:
        print("Error" , err)
        
def save_file(photo): #argumento que es el archivo foto subido
    try:    
        photo_path_local = "/tmp/photo" #la ruta local
        photo.save(photo_path_local ) #se guarda la foto localmente
        print("photo saved")
        return photo_path_local
    except Exception as err:
        print("Error", err)
        return None
        
def upload_file(s3_resource, photo, photo_path_local, id): # los argumentos son la conexion, el archivo de la foto, el path local, y el id 
    try:
        photo_name = photo.filename
        extension_photo = photo_name.split(".")[len(photo_name.split("."))-1] # solo sacamos la extensión
        photo_pad_s3 = "images_pets/" + id + "." + extension_photo # se une el id con la extensión, para guardarlo
        bucket_connection = s3_resource.meta.client.upload_file(photo_path_local, bucket_name, photo_pad_s3) # se carga el archivo en el bucket
        print("File uploaded")
        return True
    except Exception as err:
        print("Error", err)
        return False
        
def consult_file(s3_resource, id): # los parámetros con la conexión y el id de consulta
    bucket_repo = s3_resource.Bucket(bucket_name) #conecta al bucket
    bucket_objects = bucket_repo.objects.all() # descarga todos los objetos del bucket
    for obj in bucket_objects:
        path_file_s3 = obj.key
        path_photo_s3 = path_file_s3.split("/")[len(path_file_s3.split("/"))-1] # separa las extensiones de carpeta del archivo
        name_photo_process = path_photo_s3.split(".")[0] # separa el nombre de la extensión
        if name_photo_process == id: #confirmamos el archivo con el mismo
            print("Found")
            return path_file_s3
    return None