# Enumerate

# Iterasi : Loop

def enu():
    
    waifu = ['Kaga','Yae MIko','Admiral grav']

    fruits = ['apple', 'banana', 'cherry']

    for index, fruit in enumerate(fruits):
        print(f'{index}: {fruit}')

    for index, waifu in enumerate(waifu):
        print(f'{index+1}: {waifu}')
    


# Range
    
# for i in range(Angka mulai, Angka Akhir(tidak termasuk angka itu sendiri), Kelipatan):
#     print(i)

def rng():
    
    for i in range(-5, 21, 3):
        print(i)


# Reversed 

# Membalik perhitungan atau variable 

# seq_string = 'Python' <--- variable

# print(list(reversed(variable)))
def resv():
    seq_string = 'Python'

    # reverse of a string
    print(list(reversed(seq_string)))




# Set 

# A set is a collection of unique data. That is, elements of a set cannot be duplicate


def st():
    
    
    # empty set
    print(set())

    # from string
    print(set('Python'))

    # from tuple
    print(set(('a', 'e', 'i', 'o', 'u')))

    # from list
    print(set(['a', 'e', 'i', 'o', 'u']))

    # from range
    print(set(range(5)))
    

# Test code

# Enumerate
# enu()

# Range
# rng()

# Resersed
# resv()

# Set
st()
