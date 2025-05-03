import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="accounts"
)

cursor = db.cursor(dictionary=True)

def handle_login():
    username = username_entry.get()
    password = password_entry.get()

    if check_credentials(username, password):
        print("Login successful!";
    else:
        print("Login failed. Invalid credentials.")


def check_balance(user_id):
    cursor.execute("SELECT balance FROM accounts WHERE user_id = %s", (user_id))
    result = cursor.fetchone()
    return result["balance"] if result else None

def deposit(user_id, amount):
    cursor.execute("UPDATE accounts SET balance = balance + %s WHERE user_id = %s", (amount, user_id))
    db.commit()

def withdraw(user_id, amount):
    cursor.execute("SELECT balance FROM accounts WHERE user_id = %s", (user_id,))
    result = cursor.fetchone()
    if result and result["balance"] >= amount:
        cursor.execute("UPDATE accounts SET balance = balance - %s WHERE user_id = %s", (amount, user_id))
        db.commit()
        return True
    return False  # not enough funds

def create_account(name, pin, is_admin=False):
    cursor.execute("INSERT INTO users (name, pin, is_admin) VALUES (%s, %s, %s)", (name, pin, is_admin))
    db.commit()
    user_id = cursor.lastrowid
    if not is_admin:
        cursor.execute("INSERT INTO accounts (user_id, balance) VALUES (%s, %s)", (user_id, 0.00))
        db.commit()
    return user_id
