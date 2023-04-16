# python3

def read_input():
    # this function needs to aquire input both from keyboard and file
    # as before, use capital i (input from keyboard) and capital f (input from file) to choose which input type will follow

    mode = input()
    if mode.startswith('I'):
        # input from keyboard
        P = input() # first line is pattern 
        T = input() # second line is text in which to look for pattern 

    elif mode.startswith('F'):
        # input from file
        file_name = input()
        if 'a' not in file_name:
            f = open('tests/'+file_name, 'r')

            # first line is pattern 
            # second line is text in which to look for pattern
            text = f.read().split('\n')
            P = text[0]
            T = text[1]

            f.close()
    
    
    # returns both lines in one return with the rstrip function
    return (P.rstrip(), T.rstrip())

def print_occurrences(output):
    # this function should control output, it doesn't need any return
    print(' '.join(map(str, output)))

def get_occurrences(P, T):
    # this function should find the occurrences using Rabin Karp alghoritm 
    # and return an iterable variable

    occurrences = []

    m_P = len(P)
    m_T = len(T)

    if m_P <= m_T:
        b = 10

        character_id = 1

        # hash codes for the characters in the pattern - P and text - T
        characters = {}




        # hash code for the pattern - P
        pattern_hash = 0
        i = 1

        for character in P:
            if character in characters:
                c = characters[character]
            else:
                characters[character] = character_id
                c = character_id
                character_id  += 1
            
            pattern_hash += c * b**(m_P-i)
            i += 1




        # temporary hash code for the substring of text - T
        temp_text_hash = 0
        i = 1

        for character in T:
            if character in characters:
                c = characters[character]
            else:
                characters[character] = character_id
                c = character_id
                character_id  += 1

            # the "temp_text_hash%(b**(m_P-1))" part is like the example "(hash_hel - h*b**2)" from the presentation
            temp_text_hash = (temp_text_hash%(b**(m_P-1)))*b + c

            # print(pattern_hash, temp_text_hash, occurrences)
            
            if temp_text_hash == pattern_hash:
                occurrences.append(i-m_P)
            
            i += 1




    return occurrences


# this part launches the functions
if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

