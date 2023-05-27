"""
consumer to ingest data from kafka_topic 
"""
from kafka import KafkaConsumer
import mysql.connector
from ip2geotools.databases.noncommercial import DbIpCity
from ua_parser import user_agent_parser

TOPIC = 'Kafka_topic'
DATABASE = 'clickstream_data' 
USERNAME = 'username' #replace with your username
PASSWORD = 'password' #replace with your password

print("Connecting to the database")
try:
    connection = mysql.connector.connect(host='localhost', database=DATABASE, user=USERNAME, password=PASSWORD)
except Exception:
    print("Could not connect to database. Please check credentials")
else:
    print("Connected to database")
cursor = connection.cursor()

print("Connecting to Kafka")
consumer = KafkaConsumer(TOPIC, bootstrap_servers='kafka_broker_address', group_id='consumer_group_id')
print("Connected to Kafka")
print(f"Reading messages from the topic {TOPIC}")
for msg in consumer:

    # Extract data from kafka message
    (user_id, timestamp, URL, ip_address, user_agent_string) = message.value.split(",")
    
    #Retrieve country and city from IP_address
    response = DbIpCity.get(ip_address, api_key = 'free')
    country = response.country
    city = response.city
    
    #Parse user agent and retrieve browser, operating_system, device
    parsed_user_agent = user_agent_parser.Parse(user_agent_string)
    browser = parsed_user_agent['user_agent']['family']
    operating_system = parsed_user_agent['operating_system']['family']
    device = parsed_user_agent['device']['family']
    
    #Store data in click_data table
    click_data_sql = "INSERT INTO click_data VALUES(%s, %s, %s)"
    result_1 = cursor.execute(click_data_sql, (user_id, timestamp, URL))
    connection.commit()
    
    #Store data in geo_data table
    geo_data_sql = "INSERT INTO geo_data VALUES(%s, %s)"
    result_2 = cursor.execute(geo_data_sql, (country, city))
    connection.commit()
    
    #Store data in user_agent_data table
    user_agent_data_sql = "INSERT INTO user_agent_data VALUES(%s, %s, %s)"
    result_3 = cursor.execute(user_agent_data_sql, (browser, operating_system, device))
    connection.commit()
    
#Close database connection
connection.close()

"""
timestamp is assumed to be of the format
(start_time - end_time) in the format ("%Y-%m-%d %H:%M:%S - %Y-%m-%d %H:%M:%S")
"""