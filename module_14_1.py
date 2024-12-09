import sqlite3

connect = sqlite3.connect("not_telegram.db")
cursor = connect.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)
''')

cursor.execute("CREATE INDEX IF NOT EXISTS idx_email ON Users (email)")

# for i in range(10):
#     cursor.execute("INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)",
#                    (f"User{i+1}", f"example{i+1}@gmail.com", f"{(i+1)*10}", "1000"))

# for i in range(10):
#     if i % 2 != 0:
#         cursor.execute("UPDATE Users SET balance = ? WHERE id = ?", ("500", f"{i}"))

# a = 1
# for i in range(10):
#     cursor.execute("DELETE FROM Users WHERE id = ?", (f"{a}",))
#     a += 3

cursor.execute("SELECT username, email, age, balance FROM Users WHERE age != ?", ("60",))
users = cursor.fetchall()
for user in users:
    print(f'Имя: {user[1]} | Почта: {user[2]} | Возраст: {user[3]} | Баланс: {user[4]}')

connect.commit()
connect.close()
