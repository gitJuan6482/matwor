## author: Tomas Dvorak
## Example use of code block for plaintext encryption

class Encryption():
    def __init__(self, plaintext, byte1, byte2, key_seed, blockofblocks, safe_number, key):
        self.plaintext = plaintext
        self.byte1 = byte1
        self.byte2 = byte2
        self.key_seed = key_seed
        self.blockofblocks = blockofblocks
        self.safe_number = safe_number
        self.key = key

    def getUserPlain():   #### getting plaintext and key-generating phrase from user- random module is forbidden!!!
        Encryption.plaintext = str(input("Enter message:"))
    def getUserKeygen():
        Encryption.key_seed = str(input("Type any passphrase that we really need (you don't need to remember it!):  "))   #str
        if len(Encryption.key_seed) < 8:
            Encryption.getUserKeygen()
        Encryption.safe_number = int(input("Enter random number: "))                           #int
        Encryption.safe_number = ((Encryption.safe_number) + Encryption.safe_number**32) * 64  #int

    def keygen():
        global keyRawBin
        keyRawBin = (App.StrtoBin(Encryption.key_seed))
        keyRawDec = App.BintoDec(App.StrtoBin(Encryption.key_seed))
        rest = int(len(keyRawBin))%32  
            
        if rest != 0:
            for bit in range((32-rest)):
                keyRawBin += '0'
        block = int(len(keyRawBin)//32)
        
        key_blok = []
        for binblock in range(0, block):
            blck = keyRawBin[binblock*32:binblock*32+32]   
            blck = App.BintoDec(blck)
            blck = (blck *(Encryption.safe_number * (32**binblock)))%(2**32)
            blck = bin(blck)[2:]
            if int(len(blck))%32 != 0:
                void =''
                for bit in range((32-int(len(blck))%32)):
                    void += '0'
                void += blck
                key_blok.append(void) 
            else:
                key_blok.append(blck)      
        blank_data =''
        for data in range(len(key_blok)):
            blank_data = blank_data + key_blok[data]
        print(f'Key for decryption is \'{App.BintoStr(blank_data)}\'')
            
        #https://www.geeksforgeeks.org/python-convert-string-to-binary/
        #Encryption.key_seed = ''.join(format(ord(i), '08b') for i in Encryption.key_seed)   
        #https://www.w3docs.com/snippets/python/python-int-to-binary-string.html#:~:text=You%20can%20use%20the%20built-in%20bin%20%28%29%20function,%3D%205%20binary_string%20%3D%20bin%20%28x%29%20print%20%28binary_string%29
     
        
        #### converts binary to string
        #https://www.geeksforgeeks.org/convert-binary-to-string-using-python/
   
        

    def createCodeBlock():  # creating blocks of code with length 32bits
        times = len(Encryption.byte2) // 32
        #### completes block of code
        rest = len(Encryption.byte2) - 32*times
        adding = 4 - rest/8
        adding = int(adding)
        for re in range(adding):
            Encryption.byte2 = Encryption.byte2 + "01010101" 
        times = times + 1

        for block in range(times):
            blok = Encryption.byte2[(block*32):(block*32+32)]
            Encryption.blockofblocks.append(blok)
        #print(Encryption.blockofblocks)               ### debug
        #print(Encryption.byte2 == (Encryption.blockofblocks[0] + Encryption.blockofblocks[1]))

    def encr():
        Encryption.getUserPlain()
        Encryption.getUserKeygen() 
    ## check bytes length
    #### 1 byte is equal to 8 bits - let's make a 32 bits blocks length!
        Encryption.byte1 = bytes(Encryption.plaintext, "utf-8")
        Encryption.byte2 = App.StrtoBin(Encryption.plaintext)
        Encryption.blockofblocks = []
        Encryption.byte2 = str(Encryption.byte2)
        Encryption.createCodeBlock()
        Encryption.keygen()
        
        ################## debugging ###################
        #print(byte1)            # debug
        #print(len(byte1))       # debug       
        #            # debug   
        #print(key_seed)         # debug

        ### XOR in python > debugging
#print((False or False) and not (False and False)) > False
#print((True or False) and not (True and False)) > True
#print((False or True) and not (False and True)) > True
#print((True or True) and not (True and True)) > False
#print(bool(0)) > False

class Decryption():
    def __init__(self):
        pass

class App():
    def __init__(self, option):
        self.option = option
    
    def menu():
        ## program menu, with several options you can use
        print("""Welcome to Blocky - the cryptography tool 
v 0.1 ------------------

Options:  E - encrypt
          D - decrypt
          end - exit the program
                     """)
        App.askOption()

    def askOption():
        App.option = input("Your option: ")
        App.option.lower()
        if App.option == "e":
        ## Encrypting message
            Encryption.encr()
        elif App.option == "d":
            pass
        elif App.option == "end" or App.option =="exit":
            exit()
            #a way to exit the program
        else:
            print("You can't use this symbol")
            App.askOption()
    
    ## need to convert between 3 types - binary, decimal and string   ## str>bin>dec>bin>dec>str
    ## use bin(int)[2:] > binary
    ## chr(int) > string
    def StrtoBin(string):
        output = ''.join(format(ord(i), '08b') for i in string)
        return output 
    
    def BintoDec(bin):
        dec, n = 0, len(bin)
        for number1 in bin:     # transform binary to decimal          
            dec = dec + (int(number1) * pow(2, n))        
            n -= 1         
        dec = dec/2
        dec = int(dec)
        return dec
    
    def DectoStr(dec):
        dec = chr(dec)
    
    def BintoStr(bin_data):
        str_data =' '
        def BinarytoDecimal(binary):
            binary1 = binary
            decimal, i, n = 0, 0, 0
            while(binary != 0):
                dec = binary % 10
                decimal = decimal + dec * pow(2, i)
                binary = binary//10
                i += 1
            return (decimal)
        for i in range(0, len(bin_data), 7):
            temp_data = int(bin_data[i:i + 7])
            decimal_data = BinarytoDecimal(temp_data)
            str_data = str_data + chr(decimal_data)
        return str_data
    
    def XOR(binvalue1, binvalue2):
        out = ''
        for xix in range(len(str(binvalue1))):
            A = bool(int(binvalue1[xix]))
            B = bool(int(binvalue2[xix]))
            out = out + str(int((A or B) and not (A and B)))
        return out  

    ## loop for the program, for better usage
    def run():
        while True:    
            App.menu()

if __name__ == "__main__":
    App.run() 
    




