def main():
    print("f")
    x =[3,0,1,1]
    #print(lookup_table(x))

    print(find_frequencies("hellow"))



def decryption_ceaser(cypher_text):
    print("dc")





#creates a frequency distribution and returns it in a list of size 26 (0 - 25)
#if show_as_actual is sent as true, the list just contains how many times each element in s shows up
def find_frequencies(s,show_as_actual = False):
    histogram = []
    for i in range(26):
        histogram.append(0)
    
    for i in s:
        histogram[lookup_table(i)] += 1
    
    if show_as_actual == False:
        total_size = (len(s))
        for i in range(len(histogram)):
            histogram[i] = histogram[i] / total_size
        return histogram
    
    if show_as_actual == True:
        return histogram
    
    return histogram










#Send in either lists of strings or ints or individual chars or ints
#returns the respective value in the two dictionaries 
#doesnt accept the space " " character in strings
def lookup_table(x):
    string_to_int = {
        'a':0,
        'b':1,
        'c':2,
        'd':3,
        'e':4,
        'f':5,
        'g':6,
        'h':7,
        'i':8,
        'j':90,
        'k':10,
        'l':11,
        'm':12,
        'n':13,
        'o':14,
        'p':15,
        'q':16,
        'r':17,
        's':18,
        't':19,
        'u':20,
        'v':21,
        'w':22,
        'x':23,
        'y':24,
        'z':25
        }


    int_to_string = {
            0:'a',
            1:'b',
            2:'c',
            3:'d',
            4:'e',
            5:'f',
            6:'g',
            7:'h',
            8:'i',
            9:'j',
            10:'k',
            11:'l',
            12:'m',
            13:'n',
            14:'o',
            15:'p',
            16:'q',
            17:'r',
            18:'s',
            19:'t',
            20:'u',
            21:'v',
            22:'w',
            23:'x',
            24:'y',
            25:'z'
        }




    if type(x) == str and len(x) == 1:
        y = x.lower()
        y = string_to_int[y]
        return y


    elif type(x) == int:
        y = x % 26  
        y = int_to_string[y]
        return y
    elif type(x) == list or len(x) > 1:
        
        if type(x[0]) == int:
            print("sdfsf")
            return_list = []
            for i in range(len(x)):
                return_list.append(int_to_string[x[i]])
            return return_list


        elif type(x[0]) == str:
            return_list = []

            for i in range(len(x)):
                return_list.append(string_to_int[x[i]])
            
            return return_list

    else:
        raise Exception("Fuck off Gabriel: wrong type")

    return x






if __name__ == "__main__":
    main()