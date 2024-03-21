#<Q1>
user =[]
print("회원 가입")
Name = str(input("Name: "))
ID = str(input("ID: "))
PS = str(input("PS: "))

user.append(Name)
user.append(ID)
user.append(PS)

user_input = []
print("==================================================\n로그인")
input_Name = str(input("Name: "))
input_ID = str(input("ID: "))
input_PS = str(input("PS: "))

user_input.append(input_Name)
user_input.append(input_ID)
user_input.append(input_PS)

if user_input == user:
        print("로그인 성공")

else:
    print("Name, ID, PS 또느 맞지 않습니다.")