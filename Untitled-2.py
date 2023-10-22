def vault_access():
    correct_password = "123"
    attempts = 3
    x=0
 
    for x in range(attempts):
        user_password = input("Enter the vault password: ") 
        if user_password == correct_password: 
           print("correct")
           exit()
        else: 
            print("Incorrect password.") 
            x=x+1


if __name__ == "__main__":
    print(vault_access()) 