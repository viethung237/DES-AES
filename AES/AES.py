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

def bintodec(binary): #ham chuyen bin ve dec
    decimal = 0
    i = 0
    while(binary != 0 ):
        dec = binary % 10
        decimal += dec*pow(2,i)
        binary = binary // 10
        i += 1
    return decimal

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
re_mixed_tabel = [1,5,9,13,
                  2,6,10,14,
                  3,7,11,15,
                  4,8,12,16]
    
shiftrow_table = [1,2,3,4,
                  6,7,8,5,
                  11,12,9,10,
                  16,13,14,15]
def gmul(a,b):
    if b == 1:
        return a
    tmp = (a << 1) & 0xFF
    if b == 2:
        if  a < 128 :
            return tmp
        else :
            return tmp ^ 0x1b
    if b == 3:
        return gmul(a,2) ^ a
    
def transform_to_hex(val):
    newval = '{:02x}'.format(val)
    return newval.upper()
    
def mix_columns(a,b,c,d,mixed_matrix):
    mixed_matrix.append(gmul(a, 2) ^ gmul(b, 3) ^ gmul(c, 1) ^ gmul(d, 1))
    mixed_matrix.append(gmul(a, 1) ^ gmul(b, 2) ^ gmul(c, 3) ^ gmul(d, 1))
    mixed_matrix.append(gmul(a, 1) ^ gmul(b, 1) ^ gmul(c, 2) ^ gmul(d, 3))
    mixed_matrix.append(gmul(a, 3) ^ gmul(b, 1) ^ gmul(c, 1) ^ gmul(d, 2))
    return mixed_matrix

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
        shifted_matrix = permute(sbox_str,shiftrow_table,16)
        #Mix column algorithm
        if i == ( n - 1) :
            continue
        else :
            for i in range(len(shifted_matrix)):
                cal_matrix.append(hex(int(bintodec(shifted_matrix[i])))) # chuyen phan tu cua ma trix ve dang hexa 0x
                mixed_matrix = []
            for i in range(0,4):
                mix_columns(cal_matrix[i],cal_matrix[i+4],cal_matrix[i+8],cal_matrix[i+12],mixed_matrix)
                re_mixed_matrix = permute(mixed_matrix,re_mixed_table,16)
            for i in range(len(re_mixed_matrix)):
                m_matrix.append(transform_to_hex(re_mixed_matrix[i]))
        #Addroundkey algorithm
                cipher_text = xor(m_matrix,key)
        