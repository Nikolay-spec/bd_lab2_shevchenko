import psycopg2

username = 'postgres'
password = 'Sapience69'
database = 'postgres'
host = 'localhost'
port = '5432'

"""student01 postgres"""
query_1 = '''
SELECT player_wage from Players
'''

query_2 = '''
SELECT player_age from Players
'''

query_3 = '''
SELECT country_id,team_id from Players'''

con = psycopg2.connect(user=username, password=password, dbname=database, host=host, port=port)


with con:

    cur = con.cursor()

    print('1.  \n')
    cur.execute(query_1)
    for row in cur:
        print(row)

    print('\n2.  \n')
    cur.execute(query_2)
    for row in cur:
        print(row)

    print('\n3.  \n')
    cur.execute(query_3)
    for row in cur:
        print(row)
