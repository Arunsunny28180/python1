#8. Get a string from an input string where all occurrences of first character replaced with ‘$’, except first character.

txt=str(input("Enter a word:"))
txt1=txt
frst=txt[0]
txt=txt.replace(frst,"$")
txt=frst+txt[1:]
print(txt1,"-->",txt)