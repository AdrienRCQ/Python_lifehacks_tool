import pwd

def list_users():
    users = pwd.getpwall()
    for user in users:
        print(f"Username: {user.pw_name}")

def check_user_exists(username):
    try:
        pwd.getpwnam(username)
        print(f"User {username} exists.")
    except KeyError:
        print(f"User {username} does not exist.")

list_users()
check_user_exists("admin")
