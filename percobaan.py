
test = 4

# def cb () : 
#     print("test" * test)
    
# cb()

# def heighttest ():
#     for i in range(test):
#         print("test" * test)
        
# heighttest()

# How to Avoiid An Error 

def test ():
    # this first code gonna excut
    try :
        x = int(input("Isi Value X : "))
    # if there is any error in ValueError this will be run
    except ValueError :
        print("X Bukan Angka") 
    # if its not this gonna run
    else:   
        print(f"X Adalah : {x}")

        
test()