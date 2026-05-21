user1="sucharitha"
password1=1234567
user2="alakambhavya"
password2=98765
username=input("enter username:")
password=input("enter password:")
login1=("sucharitha"==user1 ) and (1234567==password1)
login2=("alakambhavya"==user2) and (password2==98765)

print("login successful:",(login1 is False) or(login2 is False) )
