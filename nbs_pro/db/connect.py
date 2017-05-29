import psycopg2
import json

config = json.loads(open('nbs_pro/db/connect_details.json').read())
try:
    conn = psycopg2.connect( "dbname=" + config['dbname']  +  " user=" + config['user'] + " host=" + config['host']  + " password=" + config['password'] )
except:
    print ("I am unable to connect to the database")


cursor = conn.cursor()

# str = 'CREATE TABLE accounts_limited(' + \
#         'id INT PRIMARY KEY NOT NULL,' + \
#         'bank CHAR(50),' + \
#         'branch CHAR(50),' + \
#         'account CHAR(50)' + \
#     ');'



# str =  ' SELECT * FROM  accounts_limited '
account = {
    'bank' : '11',
    'branch' :  '11',
    'account' : '12345'
}
# str = 'INSERT INTO accounts_limited  (id, bank, branch, account) VALUES ("" , "11", "11" , "123");'
# str = 'INSERT INTO accounts_limited(id, bank, branch, account) VALUES(default ,'+ account["bank"] + ',' + account["branch"] + ',' + account["account"] + ');'

# str = 'CREATE SEQUENCE seq_blades_id;' + \
# 'SELECT setval(100, max(id)) FROM accounts_limited; ' + \
# 'ALTER TABLE accounts_limited ALTER COLUMN id SET DEFAULT ' + \
# 'nextval(100);'
str = 'ALTER TABLE accounts_limited ALTER COLUMN id TYPE serial;'
print(str)
cursor.execute(str)
# records = cursor.fetchall()
#
# print(records[0][2])
