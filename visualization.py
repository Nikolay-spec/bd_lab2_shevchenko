import psycopg2
import matplotlib.pyplot as plt
username = 'Shevchenko_Nikolay'
password = 'Sapience69'
database = 'postgres'
host = 'localhost'
port = '5432'

query_1 = '''
SELECT player_wage from Players
'''

query_2 = '''
SELECT player_age from Players
'''

query_3 = '''
SELECT country_id,team_id from Players'''

con = psycopg2.connect(user=username, password=password, dbname=database, host=host, port=port)

#first part of plotting

print("first query")
number_lst = []
with con:
    cur = con.cursor()
    cur.execute(query_1)
    for row in cur:
        print(row)
        number_lst.append(row[0])

for i in range(len(number_lst)):
    number_lst[i] = int(number_lst[i].replace("€", "").replace("K", "")) * 1000

plt.hist(number_lst,width = 10000)
plt.title("Wage of players per month in dollars")
plt.grid()
plt.show()

#second part of plotting
print("\nsecond query")
team_lst = []
with con:
    cur = con.cursor()
    cur.execute(query_2)
    for row in cur:
        print(row)
        team_lst.append(row[0])

plt.pie(number_lst, labels=team_lst)
plt.title("Age of players")
plt.show()


#third part of plotting
print("\nthird query")
x_lst = []
y_lst = []
with con:
    cur = con.cursor()
    cur.execute(query_3)
    for row in cur:
        print(row)
        x_lst.append(row[0])
        y_lst.append(row[1])

plt.plot(sorted(x_lst), sorted(y_lst))
plt.grid()
plt.title("realtion between id of country and id of club")
plt.xlabel("country_id")
plt.ylabel("team_id")
plt.show()

