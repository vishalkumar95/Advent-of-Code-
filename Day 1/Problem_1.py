def determineFloor():
    count = 0
    with open('input.txt') as f:
        while True:
            c = f.read(1)
            if c == '(':
                count = count + 1
            elif c == ')':
                count = count - 1
            if not c:
                print ("End of file")
                return count
    
