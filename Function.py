## learn about function
currect_word = "pritom"
word = ""
changes = 6
print("Hello welcome to hangman game.\n"
      f"your changes : {changes}")
while  not :
    givenumbr = input("type your guess word : ")
    if givenumbr in currect_word:
        word += givenumbr
    
    else:
        changes -= 1
    print(word)
    print(changes)