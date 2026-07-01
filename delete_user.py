import sqlite3


conn = sqlite3.connect("notification.db")

cursor = conn.cursor()

cursor.execute("SELECT user_id, username, email FROM users")
print("Before Delete:")
for row in cursor.fetchall():
    print(row)


cursor.execute(
    "DELETE FROM users WHERE email = ?",
    ("sudhirmishra@gmail.com",)
)

conn.commit()

print("\nUser deleted successfully.")

cursor.execute("SELECT user_id, username, email FROM users")
print("\nAfter Delete:")
rows = cursor.fetchall()

if rows:
    for row in rows:
        print(row)
else:
    print("No users found.")

conn.close()