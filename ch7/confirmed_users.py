# pylint: disable=invalid-name
"""
Moving items from one list to another
"""

unconfirmed_users = ["Alice", "Bob", "Charlie"]
confirmed_users = []
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print("Verifying user: " + current_user)
    confirmed_users.append(current_user)
print("\nThe following users have been confirmed: ")
for confirmed_user in confirmed_users:
    print(confirmed_user)
