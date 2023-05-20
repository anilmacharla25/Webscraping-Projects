'''----------A web scraping project which  extacts the data from various websites and updates sqlite
database , It has total 30k websites, it fetchs homepage data of each and every url ---------------'''
import requests
from bs4 import  BeautifulSoup
import sqlite3


class SQL_updater:
    def __init__(self,db_location,table_name):
        self.db_location=db_location
        self.table_name=table_name
    
    def get_table_rows(self):
        conn=sqlite3.connect(self.db_location)
        cursor=conn.cursor()
        sql_query=f'select  Website  from {self.table_name}'
        cursor.execute(sql_query)
        conn.commit()
        # Fetch all the records
        records = cursor.fetchall()

        # Convert the records into a Python list
        urls_list = [record[0] for record in records]

        # Close the database connection
        cursor.close()
        conn.close()

        # Print the resulting list
        print(len(urls_list))
        return urls_list

    def homepage_text_extractor(self,url):
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}
        try:
            response=requests.get(url,headers=headers)
            print(response.status_code)
            if response.status_code==200:
                soup=BeautifulSoup(response.text,'html.parser')
                return soup.get_text().replace('\n','')
        except:
            return 'Unable to fetch'

    def update_table_row(self,url,homepage_text):
        conn=sqlite3.connect(self.db_location)
        cursor=conn.cursor()
        # sql_query=f"update domains set html='{homepage_text}' where  Website='{url}';"
        sql_query = "UPDATE domains SET html = ? WHERE Website = ?;"
        cursor.execute(sql_query,(homepage_text,url))
        conn.commit()
        # Fetch all the records
        records = cursor.fetchall()
        # Convert the records into a Python list
        urls_list = [record[0] for record in records]
        # Close the database connection
        cursor.close()
        conn.close()




sqlite_updater=SQL_updater(r"C:\Users\prave\Downloads\homepage.db",'domains')
urls_list=sqlite_updater.get_table_rows()
# count=0
for url in urls_list:
    homepage_text=sqlite_updater.homepage_text_extractor(f'https://{url}')
    print(homepage_text)
    sqlite_updater.update_table_row(url, homepage_text)
    # if count==10:
    #     break
    # count+=1

print('done')
    

        
