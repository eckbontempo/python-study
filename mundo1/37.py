
num = int(input('Digite um valor: '))

x = input('1 - Binário \n2 - Octal \n3 - hexadexcimal\n')

if x == 1:

    def dec(num):
        
        if num >= 1:
            dec(num // 2)
        print(num % 2, end = '')
 

''''

# Function to convert decimal number
# to binary using recursion
def DecimalToBinary(num):
     
    if num >= 1:
        DecimalToBinary(num // 2)
    print(num % 2, end = '')
 
# Driver Code
if __name__ == '__main__':
     
    # decimal value
    dec_val = 25
     
    # Calling function
    DecimalToBinary(dec_val)

'''