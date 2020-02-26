text = ''

while True:
    textinput = (input("Please enter an English phrase: "))
    text = text + str(textinput)
    if textinput == "":
        break

writeFile_Txt = open('demofile.txt','w')
writeFile_Txt.write(text)

writeFile_Txt = open('demofile.txt','r')
print(writeFile_Txt.read())
writeFile_Txt.close()

#print(text)
