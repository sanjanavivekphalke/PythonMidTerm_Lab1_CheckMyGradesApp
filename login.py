import csv
import base64


class LoginUser:
    def __init__(self, email_id, password, role):
        self.email_id = email_id
        self.password = password
        self.role = role


def Encrypt_password(password):
    return base64.b64encode(password.encode()).decode()


def decrypt_password(encrypted_password):
    return base64.b64decode(encrypted_password.encode()).decode()


def load_users():
    users = []
    with open("Login.csv", "r", newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            users.append(LoginUser(
                row["email_id"],
                row["password"],
                row["role"]
            ))
    return users


def save_users(users):
    with open("Login.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["email_id", "password", "role"])
        for user in users:
            writer.writerow([user.email_id, user.password, user.role])


def register_user():
    email_id = input("Enter new email id: ").strip()
    password = input("Enter new password: ").strip()
    role = input("Enter role (student/professor/admin): ").strip()

    if not email_id or not password or not role:
        print("Email, password and role cannot be empty.")
        return

    users = load_users()

    for user in users:
        if user.email_id == email_id:
            print("User already exists.")
            return

    encrypted_password = Encrypt_password(password)
    users.append(LoginUser(email_id, encrypted_password, role))
    save_users(users)

    print("User registered successfully!")


def Login():
    email_id = input("Enter user id: ").strip()
    password = input("Enter password: ").strip()

    users = load_users()

    for user in users:
        original_password = decrypt_password(user.password)
        if user.email_id == email_id and original_password == password:
            print("Login successful!")
            print("Role:", user.role)
            return

    print("Invalid user id or password.")


def Logout():
    print("Logout successful!")


def Change_password():
    email_id = input("Enter user id: ").strip()
    old_password = input("Enter old password: ").strip()

    users = load_users()

    for user in users:
        original_password = decrypt_password(user.password)
        if user.email_id == email_id and original_password == old_password:
            new_password = input("Enter new password: ").strip()
            user.password = Encrypt_password(new_password)
            save_users(users)
            print("Password updated successfully!")
            return

    print("Invalid user id or old password.")