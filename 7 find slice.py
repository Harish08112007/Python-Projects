text = "X-DSPAM-Confidence:    0.8475"
start = text.find("0")
num = text[start:]
num = float(num)
print(num)
       
