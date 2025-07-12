from mongoengine import connect

db = None
def init_db():
    try:
        global db
        db = connect(
            "sskmProjectPro",
            host = "localhost",
            port = 27017,
        )
    except Exception as e:
        print(f"Error connecting to database: {e}")
    print("Database connection successful")
    
    