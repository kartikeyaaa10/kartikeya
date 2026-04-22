while True:
    user_input = input("Enter something (type 'exit' to stop): ")
    
    if user_input == "exit":
        print("Goodbye!")
        break
    
    print(f"You entered: {user_input}")