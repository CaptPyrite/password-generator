import random

password_length = int(input("length of password: "))
alphabet = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
password =  "".join(random.sample(alphabet,password_length))
print(password)
