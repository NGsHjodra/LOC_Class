# f string

num = 10
num_mul_ten = num * 10

print(f"My number is {num}")

print(f"My number is {num} multiply by 10 got {num_mul_ten}")
# print(f"My number is %d" % (num))

txt = ""
age = 16
name = "sam"

if age < 15:
    txt = "can"
else:
    txt = "can\'t"

print(f"{name} {txt} join our below 15 club!!")