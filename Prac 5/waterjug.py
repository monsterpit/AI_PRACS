def min(d,f):
    if(d<f):
        return d
    else:
        return f
def steps(n):
    x,y,step=0,0,0
    print("             Vessel A       Vessel B       StepNo.")
    while (x!=n):
        if (x==0):
            x=xcapacity
            step+=1
            print("Fill A        {}".format(display(x,y,step)))
        elif(y==ycapacity):
            y=0
            step+=1
            print("Empty B       {}".format(display(x,y,step)))
        else:
            temp =min(ycapacity -y ,x)
            y=y+temp
            x=x-temp
            step+=1
            print("Pour A in B   {}".format(display(x,y,step)))
    return step

def display(a,b,s):
    return("{}               {}               {} ".format(a,b,s))

n=input("Enter the liters(GOAL) of water required to be filled in Vessel A:")
xcapacity=input("Enter the capacity of the  vessel A: ")
ycapacity=input("Enter the capacity of the  vesssel B ")

ans=steps(n)
print("Steps Required:",ans)
