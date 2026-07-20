import sqlite3

# Database se connect
conn = sqlite3.connect("users.db")
cursor = conn.cursor()

# Table create
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT,
    password TEXT
)
""")

conn.commit()
cursor.execute("INSERT INTO users (username, password) VALUES ('admin', '1234')")
conn.commit()

print("=== Login System ===")
username = input("Enter Username: ")
password = input("Enter Password: ")

# ⚠️ Insecure SQL Query (SQL Injection ke liye)
query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"

print("\nExecuting Query:")
print(query)

try:
    cursor.execute(query)
    result = cursor.fetchone()

    if result:
        print("Login Successful")
    else:
        print("Invalid Username or Password")

except Exception as e:
    print("Error:", e)

conn.close()