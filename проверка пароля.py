password=input("введите пароль ")
def pass_chek(password):
    if password.isalpha():
        print("есть буквы")
    if password.isdigit():
        print("есть буквы")
    if password.islower():
        print("есть маленькие буквы")
    if password.isupper():
        print("есть большие буквы")
    if len(password)<8:
        print("меньше 8 цифр")
    if '!' in password or  '=' in password or '@' in password or  '#' in password or  '№' in password:
        print("в пароле есть =,@,#,№,!")   
pass_chek(password) 
