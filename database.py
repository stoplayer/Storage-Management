import mysql.connector
import configparser


class Connection:
    def __init__(self):
       config = configparser.ConfigParser()
       config.read('config.ini')
       self.cnx = mysql.connector.connect(user=config['mysql']['user'], password=config['mysql']['password'],
                                host=config['mysql']['host'],
                                database=config['mysql']['database'])

       self.cursor = self.cnx.cursor()

    def __enter__(self):
        return self.cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.cursor.close()
        self.cnx.commit()
        self.cnx.close()

    @staticmethod
    def verifylogin(username, password):
        query=("SELECT * FROM user WHERE username=%s AND password=%s")
        with Connection() as conn:
            conn.execute(query, (username,password[::-1]))
            result=conn.fetchone()
            print(result)
        return result     
