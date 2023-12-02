password=input("введите пароль ")
def pass_chek(password):
    if password.isalpha() or password.isdigit() or password.islower() or password.isupper() or len(password)<8:
        print("Пароль ненадежный")
    else:
        if '!' in password or  '=' in password or '@' in password or  '#' in password or  '№' in password:
            print("пароль надежный")
   pass_chek(password) 
