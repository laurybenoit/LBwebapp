import os

class Config(object):
    SECRET_KY = os.environ.get('SECRET_KEY') or "secret_LAURY"
    
dbusername = "postgres"
dbpassword = "1989Love"