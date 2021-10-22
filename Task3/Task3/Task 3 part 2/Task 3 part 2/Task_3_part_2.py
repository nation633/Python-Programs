
#This program will replace occurances in the sentence stored in the varible and display it in reverse

#Stores the sentences that has occurances
invalid_sentence="The!quick!brown!fox!jumps!over!the!lazy!dog!"

#Replace all the Exclamation marks in the string
invalid_sentence= invalid_sentence.replace("!"," ")
invalid_sentence = invalid_sentence.upper()

#This will print the newly revised string
print(invalid_sentence)

#This will print the string in reverse
print(invalid_sentence[::-1])