str = "X-DSPAM-Confidence: 0.8475"
position = str.find(":")
number = str[position+1: ]
number = number.lstrip()
number = float(number)
print(number)
