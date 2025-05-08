import psycopg2

conn=psycopg2.connect(user='postgres', password='leshan1234', host='localhost', port='5432', database='usersss')

cur=conn.cursor()

def check_user(email):
    query="select * from users where email = %s"
    cur.execute(query,(email,))
    user=cur.fetchone()
    return user

def add_user(user_details):
    query="insert into users(name,email,phone_number,password)values(%s,%s,%s,%s)"
    cur.execute(query,user_details)
    conn.commit()