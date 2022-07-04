letter=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

end=False
while not end:   
    def word(direction,word,key):
        direction=input("Respond with 'encrypt' or 'decrypt':").lower()
    
        cypher=""
        if direction=="encrypt":
            word=input(f"Type a word to {direction}:").lower()
            key=int(input(f"Enter the key to {direction}:"))
            for letters in word:
                suggest=letter.index(letters)
                new_position=suggest+key
                cypher+=letter[new_position]
            print (cypher)
        elif direction=="decrypt":
            word=input(f"Type a word to {direction}:")
            key=int(input(f"Enter the key to {direction}:"))
            for letters in word:
                suggest=letter.index(letters)
                new_position=suggest+key
                cypher-=letter[new_position]
            print (cypher)
        else:
            print("You typed a wrong argument")
            
             
    word("cypher","note","stage")
    cont=input("Do you wish to continue with another operation,'yes'  or 'no': ")
    if cont=="yes":
        end=False
    else:
        end=True
        print("Thank you for trying out our platform")
    
    