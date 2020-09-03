phone=input('input: ')
digits_mapping={
    "s":"1",
    "o":"2",
    "n":"3",
    "a":"4",
    "d":"5",
    "e":"6",
    "v":"7",
    "i":"8",
    "t":"9",
    "x":"0"
}
output=""
for ch in phone:
    output +=digits_mapping.get(ch,"!") + " "

print(output)
