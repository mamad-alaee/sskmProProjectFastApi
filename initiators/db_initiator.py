from mongoengine import connect
from initiators.init_env import db_name,db_host,db_port

db = None
def init_db():
    try:
        global db
        db = connect(
            db_name,
            host = db_host,
            port = db_port,
        )
    except Exception as e:
        print(f"Error connecting to database: {e}")
    print("Database connection successful")
    
    