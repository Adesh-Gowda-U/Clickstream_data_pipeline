#Replace placeholders with actual credentials like host, user, password.
import mysql.connector

# Connect to the MySQL server
connection = mysql.connector.connect(
    host="localhost",
    user="your_username",
    password="your_password"
)

# Create a new database
cursor = connection.cursor()
cursor.execute("CREATE DATABASE IF NOT EXISTS clickstream_data;")
cursor.close()

# Connect to the clickstream_data database
connection.database = "clickstream_data"
cursor = connection.cursor()

# Create the click_data table
click_data_table = """
CREATE TABLE IF NOT EXISTS click_data (
    ID INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT,
    timestamp DATETIME,
    URL VARCHAR(255)
)
"""
cursor.execute(click_data_table)

# Create the geo_data table
geo_data_table = """
CREATE TABLE IF NOT EXISTS geo_data (
    click_id INT PRIMARY KEY AUTO_INCREMENT,
    country VARCHAR(255),
    city VARCHAR(255)
)
"""
cursor.execute(geo_data_table)

# Create the user_agent_data table
user_agent_data_table = """
CREATE TABLE IF NOT EXISTS user_agent_data (
    click_id INT PRIMARY KEY AUTO_INCREMENT,
    browser VARCHAR(255),
    operating_system VARCHAR(255),
    device VARCHAR(255)
)
"""
cursor.execute(user_agent_data_table)

# Close the cursor and connection
cursor.close()
connection.close()