loggin = input("Enter please your login(only word) >>>")
password = input("Enter please your password(word and numer) >>>")
loggin_word = loggin.isalpha()
password_num_word = password.isalnum()
replay_enter_password = input("Repley please your password(word and numer) >>>")
replay_password_num = replay_enter_password.isalnum()

if (loggin_word == True) and (password_num_word == True) and (replay_enter_password == password):
    print("You enter system")
else:
    print("Wrong login or password")

unlogin = "You are broken because I wanted it so, repley write please your password and loggin!!!"
print(unlogin)
repley_loggin = input("Loggin:")
repley_password = input("Password:")
repley_loggin_corect = repley_loggin.isalpha()
repley_password_corect = repley_password.isalnum()
total_result = (repley_loggin_corect == True) and (repley_password_corect == True) and (repley_loggin == loggin) and (repley_password == password)

if total_result == True:
    print("You enter system")
else:
    print("Wrong login or password")
