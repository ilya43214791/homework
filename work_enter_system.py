loggin = input("Enter please your login(only word) >>>")
password = input("Enter please your password(word and numer) >>>")
loggin_word = loggin.isalpha()
password_num_word = password.isalnum()
replay_enter_password = input("Repley please your password(word and numer) >>>")
replay_password_num = replay_enter_password.isalnum()

if password_num_word == True and replay_password_num == password_num_word:
    print("You enter system")
else:
    print("Wrong login or password")

unlogin = "You are broken because I wanted it so, repley write please your password and loggin!!!"
print(unlogin)
repley_loggin = input("Loggin:").isalpha()
repley_password = input("Password:").isalnum()

if repley_loggin == loggin_word and repley_password == replay_password_num:
    print("You enter system")
else:
    print("Wrong login or password")
