# INT Variable
# INT is include A Real number 

x = int(input("Enter X : "))
y = int(input("Enter Y : "))

print("Z Are : ",x + y)

# FLOAT Variable

x = float(input("Enter X : "))
y = float(input("Enter Y : "))

# z = round(x / y   ,5)
z = x / y

# Next parameter number is to show how much you wanna see the decimal

# round adalah pembulatan bilangan desimal

print(f"Z round are : {z:,}")
# print(f"Z round are : {z:.2f}")

# f are for formated to string

# Boolean / Bool (True / False)

def main():
    x = int(input("Masukan variable x"))
    if test(x):
        print("angka genap")
    else:
        print("ganjil")

def test(n):
    if n % 2 == 0 :
        return True
    else :
        return 
    
def test(n):
    return True if n % 2 == 0 else False


main()

