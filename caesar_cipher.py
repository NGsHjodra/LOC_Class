# chr num to letter
# ord letter to num

password = "AriosetnakCoicurs320"
step = 3

encryted_password = ""
for letter in password:
    letter_ord = ord(letter)
    encryted_letter = chr(letter_ord + step)
    encryted_password += encryted_letter

print(encryted_password)