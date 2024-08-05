if __name__ == '__main__':
    x = int(input("A"))
    y = int(input("B"))
    z = int(input("C"))
    n = int(input("D"))

    l=[[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i+j+k !=0]
    print(l)