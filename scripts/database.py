from app.db.models import Document,DocumentChunk
from app.db.database import engine, Base


def  init_db():
    print("Connecting to Database.....")
    Base.metadata.create_all(bind=engine)
    print("Tables created successfully")


if __name__ == "__main__":
    init_db()


