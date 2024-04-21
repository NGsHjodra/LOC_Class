# condition

s = "string long loooong"

if len(s) > 10:
    if "s" in s:
        print("this is long enough and contains \'s\'")


# basic password checker
# 12-20 long password
# contains ! and * in password

password = "23449fpts!eiorastn*"
print(12 <= len(password) <= 20)

if len(password) >= 12 and len(password) <= 20:
    if "!" in password and "*" in password:
        print("password is secure")
    else:
        print("your password not contain \'!\' and \'*\'")
else:
    print("your password is not 12-20 long")