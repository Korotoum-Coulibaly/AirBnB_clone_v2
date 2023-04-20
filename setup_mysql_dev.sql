-- Mysql configuration
import mysql.connector
connection = mysql.connector.connect(
		HBNB_ENV = "dev",
		HBNB_MYSQL_USER = "hbnb_dev",
		HBNB_MYSQL_PWD = "hbnb_dev_pwd",
		HBNB_MYSQL_HOST = "localhost",
		HBNB_MYSQL_DB = "hbnb_dev_db",
		HBNB_TYPE_STORAGE = "DBStorage")
cursor = connection.cursor(prepared = true)
GRANT ALL PRIVILEGES ON `hbnb_dev_db`.* TO 'hbnb_dev'@'localhost'
GRANT SELECT ON `performance_schema`.* TO 'hbnb_dev'@'localhost'
GRANT USAGE ON *.* TO 'hbnb_dev'@'localhost
