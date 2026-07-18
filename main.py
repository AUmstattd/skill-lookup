import fetch_user
import llm
import sys

username = input("Which Github User? ")
print(f"fetching: {username}...")
user = fetch_user.fetch_user(username)
if user is None:
    print("Could not find the username")
    sys.exit()
explain = llm.ask_llm(f"Explain this user in two, plain english sentences. Focus on their activity. Don't mention missing profile fields: {user}")
if explain is None:
    print("Could not get a summary")
    sys.exit()
print(explain)