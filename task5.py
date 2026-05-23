user1="sucharitha"
password1="1234567"
user2="alakambhavya"
password2=98765
username=input("enter username:")
password=input("enter password:")
login1=(username==user1 ) and (password==password1)
login2=(username==user2) and (password2==password)
result = login1 or login2
print("Login Successful:", result is True)
