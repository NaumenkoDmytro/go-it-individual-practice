'''
Dict task: 3 
'''

def user_update(user_data:list) -> None:
    for user in user_data:
        if user["status"] == "disabled":
            user.pop("country")

        

users = [
  { "name": "Emma", "status": "active", "country": "Ukraine" },
  { "name": "Avram", "status": "disabled", "country": "Poland" },
  { "name": "Avram", "status": "active", "country": "Poland" },
  { "name": "Avram", "status": "disabled", "country": "Poland" },
]

print(user_update(users))
print(users)
