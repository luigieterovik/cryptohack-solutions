# Extended Euclidean Algorithm

numbers = sorted([26513, 32321], reverse=True)

gcd = None

initial_rest = numbers[0] % numbers[1]

quotient_sequence = [numbers[0] // numbers[1]]
sequence_numbers = numbers + [initial_rest]

if initial_rest == 0:
    gcd = numbers[1]
    sequence_numbers.append(initial_rest)
    print("GCD: ", gcd)
    
else:
    
    while gcd == None:
        rest = sequence_numbers[-2] % sequence_numbers[-1]
        quotient_sequence.append(sequence_numbers[-2] // sequence_numbers[-1])
        
        if rest == 0:
            gcd = sequence_numbers[-1]
            sequence_numbers.append(rest)
            
        else: 
            sequence_numbers.append(rest)
    
    print(print("GCD: ", gcd))
    
reversed_numbers = [1, 0, 0, 1]
quotient_sequence.pop()

while len(quotient_sequence) != 0:
    v = reversed_numbers[-2] - (quotient_sequence[-1]) * reversed_numbers[-1]
    reversed_numbers.append(v)
    quotient_sequence.pop()
    
u = reversed_numbers[-2]
v = reversed_numbers[-1]

print("u: ", u)
print("v: ", v)