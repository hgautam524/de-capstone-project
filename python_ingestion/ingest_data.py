import os
import json
import requests
import snowflake.connector
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Snowflake connection parameters
SNOWFLAKE_USER = os.getenv("SNOWFLAKE_USER")
SNOWFLAKE_PASSWORD = os.getenv("SNOWFLAKE_PASSWORD")
SNOWFLAKE_ACCOUNT = os.getenv("SNOWFLAKE_ACCOUNT")
SNOWFLAKE_WAREHOUSE = os.getenv("SNOWFLAKE_WAREHOUSE")
SNOWFLAKE_DATABASE = os.getenv("SNOWFLAKE_DATABASE")
SNOWFLAKE_SCHEMA = os.getenv("SNOWFLAKE_SCHEMA")


def get_snowflake_connection():
    try:
        conn = snowflake.connector.connect(
            user=SNOWFLAKE_USER,
            password=SNOWFLAKE_PASSWORD,
            account=SNOWFLAKE_ACCOUNT,
            warehouse=SNOWFLAKE_WAREHOUSE,
            database=SNOWFLAKE_DATABASE,
            schema=SNOWFLAKE_SCHEMA
        )
        print("Connected to Snowflake successfully!")
        return conn
    except Exception as e:
        print("Error connecting to Snowflake:", e)
        exit(1)


def fetch_data(url):
    print(f"Fetching data from {url}...")
    response = requests.get(url)
    if response.status_code == 200:
        print("Data fetched successfully!")
        return response.json()
    else:
        raise Exception(f"Failed to fetch data. Status code: {response.status_code}")


def load_to_snowflake(conn, table_name, data):
    try:
        cur = conn.cursor()
        print(f"Loading data into {table_name}...")

       
        for record in data:
            cur.execute(
                f"INSERT INTO {table_name} (raw_json) SELECT PARSE_JSON(%s)",
                (json.dumps(record),)
            )

        conn.commit()
        print(f"Loaded {len(data)} records into {table_name}!")
        cur.close()
    except Exception as e:
        print(f"Error loading data into {table_name}: {e}")

def main():
 
    posts_data = fetch_data("https://jsonplaceholder.typicode.com/posts")
    comments_data = fetch_data("https://jsonplaceholder.typicode.com/comments")

  
    conn = get_snowflake_connection()


    load_to_snowflake(conn, "POSTS", posts_data)
    load_to_snowflake(conn, "COMMENTS", comments_data)

    conn.close()
    print("Data ingestion completed successfully!")

if __name__ == "__main__":
    main()