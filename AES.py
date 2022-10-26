def hextobin(s):
    changehex = { '0' : '0000',
               '1' : '0001',
               '2' : '0010',
               '3' : '0011',
               '4' : '0100',
               '5' : '0101',
               '6' : '0110',
               '7' : '0111',
               '8' : '1000',
               '9' : '1001',
               'A' : '1010',
               'B' : '1011',
               'C' : '1100',
               'D' : '1101',
               'E' : '1110',
               'F' : '1111' }
    binary = ''
    for i in range(len(s)):
        binary = binary + changehex[s[i]]
    return binary

def bintohex(s) :
    changebin = { '0000' : '0',
                  '0001' : '1',
                  '0010' : '2',
                  '0011' : '3',
                  '0100' : '4',
                  '0101' : '5',
                  '0110' : '6',
                  '0111' : '7',
                  '1000' : '8',
                  '1001' : '9',
                  '1010' : 'A',
                  '1011' : 'B',
                  '1100' : 'C',
                  '1101' : 'D',
                  '1110' : 'E',
                  '1111' : 'F' }
    heximal = ''
    for i in range(0,len(s),4):
        ch = ''
        ch += s[i]
        ch += s[i+1]
        ch += s[i+2]
        ch += s[i+3]
        heximal = heximal + changebin[ch]
    return heximal
pt = "123456ABCD132536"
def ge_matrix(pt):
    c_matrix =[]
    for i in range(0,len(pt),2):
        ch =''
        ch += pt[i]
        ch += pt[i+1]
        c_matrix.append(ch)
    for i in range(len(c_matrix)):
        c_matrix[i]=hextobin(c_matrix[i])
    return c_matrix

def permute(k,arr,n):
    permutation =''
    for i in range(0,n):
        permutation += k[arr[i]- 1]
    return permutation

def xor(a,b):
    cal = ''
    for i in range(len(a)):
        if a[i] == b[i] :
            cal += '0'
        else:
            cal += '1'
    return cal

def addroundkey():
#test

#pre tranform -> input
# pretranform = xor(c_matrix(pt),key[0]) = in_input
def encrypt():
    if len(key) == 128 :
        n = 10
    else if len(key) == 192 :
        n = 12
    else :
        n = 14
    for i in range(n):
        #s box algorithm
        sbox_str = ''
        for j in range (0,16):
            row = bintodec(int(in_input[j*8] + in_input[j*8+1] + in_input[j*8+2] + in_input[j*8+3]))
            column = bintodec(int(in_input[j*8+4] + in_input[j*8+5] + in_input[j*8+6] + in_input[j*8+7]))
            value = sbox[row][column]
            sbox_str += hextobin(value)
        #shiftrow algorithm
        
    
        