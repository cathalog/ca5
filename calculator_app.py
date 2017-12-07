from calculator import Calculator
run = 'y'
inp = ''
inp2 = ''
while run == 'y':
    inp = '' 
    numbers = []
    a = raw_input("add(a), subtract(s), multiply(m), divide(d), exponent(e), square(sq), square root (sqrt), sin(sin), cos(cos) or tan(tan)?")
    if a == "a":
        while inp != 'e':    
            inp = raw_input("Enter numbers individually, e to end: ")        
            if inp == 'e':
                print Calculator().add(numbers)
                run = raw_input("continue?") 
            else:
                inp2=float(inp)
                numbers.append(inp2)
            
    if a == "s":
        while inp != 'e':    
            inp = raw_input("Enter numbers individually, e to end: ")        
            if inp == 'e':
                print Calculator().subtract(numbers)
                run = raw_input("continue?") 
            else:
                inp2=float(inp)
                numbers.append(inp2)
                
    if a == "m":
        while inp != 'e':    
            inp = raw_input("Enter numbers individually, e to end: ")        
            if inp == 'e':
                print Calculator().multiply(numbers)
                run = raw_input("continue?") 
            else:
                inp2=float(inp)
                numbers.append(inp2)
                
    if a == "d":
        while inp != 'e':    
            inp = raw_input("Enter numerator, then denominator(s), e to end: ")        
            if inp == 'e':
                if 0 in numbers[1:]:
                    print "Can't divide by 0"
                else:
                    print Calculator().divide(numbers)
                    run = raw_input("continue?") 
            else:
                inp2=float(inp)
                numbers.append(inp2)
                
    if a == "e":
        while inp != 'e':    
            inp = raw_input("Enter base, then power(s), e to end: ")        
            if inp == 'e':
                print Calculator().exponent(numbers)
                run = raw_input("continue?") 
            else:
                inp2=float(inp)
                numbers.append(inp2)
                
    if a == "sq":
        while inp != 'e':    
            inp = raw_input("Enter numbers individually, e to end: ")        
            if inp == 'e':
                print Calculator().square(numbers)
                run = raw_input("continue?") 
            else:
                inp2=float(inp)
                numbers.append(inp2)
    if a == "sqrt":
        while inp != 'e':    
            inp = raw_input("Enter numbers individually, e to end: ")        
            if inp == 'e':
                print Calculator().squareroot(numbers)
                run = raw_input("continue?")             
            else:
                inp2=float(inp)
                numbers.append(inp2)
    if a == "sin":
        while inp != 'e':    
            inp = raw_input("Enter angles in degrees, e to end: ")        
            if inp == 'e':
                print Calculator().sindegrees(numbers)
                run = raw_input("continue?") 
            else:
                inp2=float(inp)
                numbers.append(inp2)
    if a == "cos":
        while inp != 'e':    
            inp = raw_input("Enter angles in degrees, e to end: ")        
            if inp == 'e':
                print Calculator().cosdegrees(numbers)
                run = raw_input("continue?") 
            else:
                inp2=float(inp)
                numbers.append(inp2)
    if a == "tan":
        while inp != 'e':    
            inp = raw_input("Enter angles in degrees, e to end: ")        
            if inp == 'e':
                print Calculator().tandegrees(numbers)
                run = raw_input("continue?") 
            else:
                inp2=float(inp)
                numbers.append(inp2)
                                              