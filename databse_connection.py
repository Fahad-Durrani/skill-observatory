from imports import *

def connect_to_database(DATABASE_NAME, DATABASE_USERNAME, DATABASE_PASSWORD, DATABASE_URI, PORT):
    try:
        # Establish connection with psycopg2
        conn = psycopg2.connect(
            dbname=DATABASE_NAME,
            user=DATABASE_USERNAME,
            password=DATABASE_PASSWORD,
            host=DATABASE_URI,
            port=PORT
        )
        logger.info('Connection to the database was successful with psycopg2!')
        cursor = conn.cursor()

        try:
            # Create the PostgreSQL connection URI for SQLDatabase
            DATABASE_URI = f"postgresql+psycopg2://{DATABASE_USERNAME}:{DATABASE_PASSWORD}@{DATABASE_URI}:{PORT}/{DATABASE_NAME}"
            # Create a connection to the PostgreSQL database using SQLDatabase
            db = SQLDatabase.from_uri(DATABASE_URI)
            logger.info('Connection to the PostgreSQL database was successful using SQLDatabase!')

            # Return the connections and cursor if both are successful
            return conn, cursor, db

        except Exception as e:
            # Handle and log any error that occurs during the SQLDatabase connection attempt
            logger.error(f"Error: Unable to connect to the database using SQLDatabase\n{e}")
            return None, None, None

    except Exception as e:
        # Handle and log any error that occurs during the psycopg2 connection attempt
        logger.error(f"Error: Unable to connect to the database with psycopg2\n{e}")
        return None, None, None

