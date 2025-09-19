# Euclid's Algorithm

numbers = sorted([66528, 52920], reverse=True)

gcd = None

initial_quotient = numbers[0] // numbers[1]
initial_rest = numbers[0] % numbers[1]

if initial_rest == 0:
    gcd = numbers[1]
    print(gcd)

else:
    sequence_numbers = numbers + [initial_rest]
    
    while gcd == None:
        rest = sequence_numbers[-2] % sequence_numbers[-1]
        
        if rest == 0:
            gcd = sequence_numbers[-1]
            
        else: 
            sequence_numbers.append(rest)
    
    print(gcd)