def checkio(words: str) -> bool:
    count = 0               # create a count variable
    for i in words.split(): # go through the splited string
        if not i.isalpha(): # if element i contain not letters    
            count = 0       # set counter to zero
        else:               # all characters are letters
            count += 1      # count up   
        if count == 3:      # if the counter is 3 
            return True     # we have three words in a raw
    return False
