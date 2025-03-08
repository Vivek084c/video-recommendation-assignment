import psycopg2

# Connect to PostgreSQL (default database "postgres")
conn = psycopg2.connect(
    host="localhost",
    database="postgres",  # Connect to the default database to create a new one
    user="postgres",  # Change if you have a different username
    password="vivek@2003",  # Change this to your actual password
    port=8888  # Default PostgreSQL port
)

conn.autocommit = True  # Ensure we can execute CREATE DATABASE outside of a transaction
cursor = conn.cursor()

# Database name
db_name = "vivek"

# Create database
try:
    cursor.execute(f"CREATE DATABASE {db_name};")
    create_script = 
    print(f"Database '{db_name}' created successfully!")
except psycopg2.Error as e:
    print(f"Error creating database: {e}")

# Close connections
cursor.close()
conn.close()