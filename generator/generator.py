import csv
import random
import psycopg2
import psycopg2.extras
import datetime

intros =[]
names = []
additions = []
pretexts = []
verbs = []
events = []
logins = []
authors = []
posts = []
characteristic_post = []
characteristic_author = []

with open('intros.csv', "r", encoding = 'utf-8') as file:
    reader = csv.reader(file)
    for row in reader:
        intros.extend(row)

with open('names.csv', "r", encoding = 'utf-8') as file:
    reader = csv.reader(file)
    for row in reader:
        names.extend(row)

with open('additions.csv', "r", encoding = 'utf-8') as file:
    reader = csv.reader(file)
    for row in reader:
        additions.extend(row)

with open('pretexts.csv', "r", encoding = 'utf-8') as file:
    reader = csv.reader(file)
    for row in reader:
        pretexts.extend(row)

with open('verbs.csv', "r", encoding = 'utf-8') as file:
    reader = csv.reader(file)
    for row in reader:
        verbs.extend(row)

with open('events.csv', "r", encoding = 'utf-8') as file:
    reader = csv.reader(file)
    for row in reader:
        events.extend(row)

with open('logins.csv', "r", encoding = 'utf-8') as file:
    reader = csv.reader(file)
    for row in reader:
        logins.extend(row)

with open('authors.csv', "r", encoding = 'utf-8') as file:
    reader = csv.reader(file)
    for row in reader:
        authors.extend(row)

with open('posts.csv', "r", encoding = 'utf-8') as file:
    reader = csv.reader(file)
    for row in reader:
        posts.extend(row)

with open('characteristic_post.csv', "r", encoding = 'utf-8') as file:
    reader = csv.reader(file)
    for row in reader:
        characteristic_post.extend(row)

with open('characteristic_author.csv', "r", encoding = 'utf-8') as file:
    reader = csv.reader(file)
    for row in reader:
        characteristic_author.extend(row)

def generate_password():
    chars = list('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890')
    str = ''
    for i in range(0, 8):
        str += random.choice(chars)
    return str

def generate_user():
    conn = psycopg2.connect("dbname='blog2' user='postgres' host='localhost' password='root'")
    cur = conn.cursor(cursor_factory = psycopg2.extras.DictCursor)

    for login in logins:
        password = generate_password()

        user = {
            'login' : login,
            'password' : password
        }

        cur.execute('INSERT INTO gotblog_user(login, password) VALUES (%(login)s, %(password)s)', user)
        conn.commit()

def generate_post():
    conn = psycopg2.connect("dbname='blog2' user='postgres' host='localhost' password='root'")
    cur = conn.cursor(cursor_factory = psycopg2.extras.DictCursor)

    for i in range(20, 10001):
        user_id = random.randint(20, 30)
        name = random.choice(names)
        title = random.choice(intros) + ' ' + random.choice(additions) + ' ' + name + '.'
        body = name + ' ' + random.choice(verbs) + ' ' + random.choice(names) + ' ' + random.choice(pretexts) + ' ' + random.choice(events) + '.'
        date = datetime.date(2018, random.randint(1, 12), random.randint(1, 28))

        post = {
            'user_id' : user_id,
            'title' : title,
            'body' : body,
            'date' : date
        }

        cur.execute('INSERT INTO gotblog_post(user_id, title, body, date_pub) VALUES (%(user_id)s, %(title)s, %(body)s, %(date)s)', post)
        conn.commit()

def generate_comment():
    conn = psycopg2.connect("dbname='blog2' user='postgres' host='localhost' password='root'")
    cur = conn.cursor(cursor_factory = psycopg2.extras.DictCursor)

    for i in range(1, 10001):
        user_id = random.randint(100, 2000)
        post_id = random.randint(100, 2000)
        body = random.choice(authors) + ' - ' + random.choice(characteristic_author) + ', ' + random.choice(posts) + ' - ' + random.choice(characteristic_post)
        date = datetime.date(2018, random.randint(1, 12), random.randint(1, 28))

        comment = {
            'user_id' : user_id,
            'post_id' : post_id,
            'body' : body,
            'date' : date
        }

        cur.execute('INSERT INTO gotblog_comment(user_id, post_id, body, date_pub) VALUES (%(user_id)s, %(post_id)s, %(body)s, %(date)s)', comment)
        conn.commit()

def generate_subscriber():
    conn = psycopg2.connect("dbname='blog2' user='postgres' host='localhost' password='root'")
    cur = conn.cursor(cursor_factory = psycopg2.extras.DictCursor)

    for i in range(100, 2000):
        user_id = random.randint(100, 2000)
        subscriber_id = i
        if user_id != subscriber_id:
            subscriber = {
                'user_id' : user_id,
                'subscriber_id' : subscriber_id
            }

            cur.execute('INSERT INTO gotblog_subscriber(user_id, subscriber_id) VALUES (%(user_id)s, %(subscriber_id)s)', subscriber)
            conn.commit()


if __name__ == '__main__':
    # generate_user()
    # generate_post()
    # generate_comment()
    generate_subscriber()
