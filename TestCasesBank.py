def test_create_account():
    print("Testing create_account...")
    user_id = create_account("TestUser", "1234", is_admin=False)
    if user_id:
        print(f"Account created with user_id = {user_id}")
    else:
        print("Account creation failed.")

def test_check_balance(user_id):
    print("Testing check_balance...")
    balance = check_balance(user_id)
    if balance is not None:
        print(f"Balance for user {user_id} is {balance}")
    else:
        print("Balance not found or account does not exist.")

def test_deposit(user_id):
    print("Testing deposit...")
    deposit(user_id, 100.0)
    balance = check_balance(user_id)
    print(f"New balance after deposit: {balance}")

def test_withdraw(user_id):
    print("Testing withdraw...")
    success = withdraw(user_id, 50.0)
    if success:
        print("Withdraw successful")
        balance = check_balance(user_id)
        print(f"New balance: {balance}")
    else:
        print("Withdraw failed — not enough funds or account not found.")

def test_insufficient_funds(user_id):
    print("Testing withdraw with insufficient funds...")
    success = withdraw(user_id, 1000000.0)
    if not success:
        print("Properly prevented overdraw.")
    else:
        print("Overdraw allowed — this is a bug.")