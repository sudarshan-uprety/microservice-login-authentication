from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_URL = "postgresql+psycopg2://{username}:{password}@{host}:{port}/{db_name}".format(
    host=os.getenv("USER_POSTGRES_DB_HOST"),
    port=os.getenv("USER_POSTGRES_DB_PORT"),
    db_name=os.getenv("USER_POSTGRES_DB_NAME"),
    username=os.getenv("USER_POSTGRES_DB_USER"),
    password=os.getenv("USER_POSTGRES_DB_PASSWORD"),
)

ACCESS_TOKEN_EXPIRE_MINUTES = os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES")
REFRESH_TOKEN_EXPIRE_MINUTES = os.getenv("REFRESH_TOKEN_EXPIRE_MINUTES")
ALGORITHM = os.getenv("ALGORITHM")
JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")
JWT_REFRESH_SECRET_KEY = os.getenv("JWT_REFRESH_SECRET_KEY")

ROOT_URL = os.getenv("ROOT_URL")

MAIL_USERNAME = os.getenv('MAIL_USERNAME')
MAIL_FROM = os.getenv('MAIL_USERNAME')
MAIL_PASSWORD = os.getenv('MAIL_PASSWORD')
MAIL_PORT = int(os.getenv('MAIL_PORT'))
MAIL_SERVER = os.getenv('MAIL_SERVER')