def solution(n,src,des,aux):
    if n == 1:
        print(f"{n}({src} -> {des})")
    else:
            solution(n-1,src,des,aux)   
            print(f"{n}({src} -> {aux})")
            solution(n-1,des,src,aux)
            print(f"{n}({aux} -> {des})")
            solution(n-1,src,des,aux)

n = int(input("Enter the number of disks: "))
src = input("Enter the source rod: ")
des = input("Enter the destination rod: ")
aux = input("Enter the auxiliary rod: ")
solution(n,src,des,aux)
print("Congratulations, you have solved the Tower of Hanoi")