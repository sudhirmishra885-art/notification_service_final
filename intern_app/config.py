from dotenv import load_dotenv
import os

load_dotenv()
<<<<<<< HEAD

=======
print(load_dotenv)
>>>>>>> c1d920b4e1198abbfe06cab9643dde77c8dcb4cf
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = int(
    os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 30)
)

<<<<<<< HEAD
DATABASE_URL = os.getenv("DATABASE_URL")
=======
DATABASE_URL = os.getenv("DATABASE_URL")
>>>>>>> c1d920b4e1198abbfe06cab9643dde77c8dcb4cf
