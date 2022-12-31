# Open database connection
import pymysql


db = pymysql.connect(host="localhost", user="Engy ",password="Engy@1234",db="eds")

# prepare a cursor object using cursor() method
cursor = db.cursor()
 ####################################################################Registeration##############################

sql = "INSERT INTO recipient (firstname, lastname, familymembers, Address) VALUES (%s,%s,%s,%s)"
val = ("Jawad", "0000-00-00", 5, "ddhdjkss")
cursor.execute(sql, val)

db.commit()

print(cursor.rowcount, "record inserted.")


# execute SQL query using execute() method.
cursor.execute("SELECT VERSION()")

# Fetch a single row using fetchone() method.
data = cursor.fetchone()
print ("Database version : %s " % data)

# disconnect from server
db.close()
