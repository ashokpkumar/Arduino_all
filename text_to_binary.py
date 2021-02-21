# read textfile into string 
with open('sample_txt.txt', 'r') as txtfile:
    mytextstring = txtfile.read()

# change text into a binary array
binarray = ' '.join(format(ch, 'b') for ch in bytearray(mytextstring))

# save the file
with open('binfileName', 'w') as binfile:
    binfile.write(binarray)