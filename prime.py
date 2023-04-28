def prime(num):
    if num>1:
        for i in range(2,int(num/2)+1):
            if num%i==0:
                print("Not Prime Number")
                break
        else:
             print(num,"is a Prime Number")
    else:
        print(num,"is not a Prime Number")

num=14
prime(num)