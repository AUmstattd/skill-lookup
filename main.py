import fetch_user
import llm

def main():
    username = input("Which Github User? ")
    print(f"fetching: {username}...")
    user = fetch_user.fetch_user(username)
    if user is None:
        print("Could not find the username")
        return
    explain = llm.ask_llm(f"Explain this user in two, plain english sentences. Focus on their activity. Don't mention missing profile fields: {user}")
    if explain is None:
        print("Could not get a summary")
        return
    print(explain)

if __name__ == "__main__":
    main()