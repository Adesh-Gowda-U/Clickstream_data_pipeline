Title: Real-Time Data Pipeline to process clickstream data

Introduction:
The purpose of this report is to provide a brief overview of the clickstream data pipeline
that has been developed to process and store messages from kafka into MySQL database. The
stored data is then further processed using SparkSQL and indexed using Elasticserch.

Pipeline Architecture:

1. Kafka:
	Kafka is utilized as a high-throughput distributed messaging system. It acts as a data
	source.
	
2. Data Ingestion:
	A component is developed to read messages from Kafka topics in real-time. It uses Kafka
	consumer APIs to retrieve messages efficiently and handles any necessary deserialization.
	
3. MySQL Database:
	The data retrieved from Kafka is stored in a MySQL database. The MySQL database serves as
	a persistent storage solution
	
4. Spark SQL:
	Spark SQL is used for processing the stored data in the MySQL database. Spark SQL provides
	a unified interface for querying structured and semi-structured data using SQL-like syntax
	
5. ElasticSearch:
	The processed data is further indexed and stored in ElasticSearch, a distributed search and
	analytics engine.
	
6. Airflow:
	Airflow dag is created for data processing and indexing. and is scheduled to run hourly.
	
Data Pipeline Workflow:

1. A schema is created by executing the python file "MySQL_schema" which will be used to store
   data from Kafka.

2. Kafka_consumer file is executed which reads messages from Kafka topics in real-time. The consumed
   messages are transformed into aappropriate format and stored in a MySQL database. This step involves
   mapping the data to the predefined schema and handling any necessary data conversions or validations.
   
3. Spark SQL queries the MySQL database to retrieve the stored data. The retrieved data is then processed
   using various Spark SQL operations, such as filtering, aggregating, joining, or transforming the data as required
   
4. The processed data is indexed in ElasticSearch to enable fast and efficient search capabilities.
   The indexing process involves mapping the data to the appropriate ElasticSearch index schema and
   leveraging ElasticSearch's indexing and searching APIs to store and retrieve the data.
   
5. An Airflow DAG is created for aggregating the data using Spark SQL  and to index the data in ElasticSearch.
   This DAG is scheduled to every hourly.