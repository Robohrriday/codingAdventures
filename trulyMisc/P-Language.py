name =  input("Enter your name: ")
updated_letters = {}   
for i in range(0, len(name)):
    letters = {
        i:name[i]
    }
    updated_letters.update(letters)
for j in range(0, len(name)):
    if updated_letters.get(j) == 'a':
        updated_a = {
            j:'apa'
        }
        updated_letters.update(updated_a)
    elif updated_letters.get(j) == 'e':
        updated_e = {
            j:'epe'
        }
        updated_letters.update(updated_e)
    elif updated_letters.get(j) == 'i':
        updated_i = {
            j:'ipi'
        }
        updated_letters.update(updated_i)
    elif updated_letters.get(j) == 'o':
        updated_o = {
            j:'opo'
        }
        updated_letters.update(updated_o)
    elif updated_letters.get(j) == 'u':
        updated_u = {
            j:'upu'
        }
        updated_letters.update(updated_u)
    else:
        pass
print("Your name in P-language is: ", end="")
for k in range(0, len(name)):
    print(updated_letters.get(k), end="")