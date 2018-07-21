def minmax(depth,nodeIndex,maximizingPlayer,values,alpha,beta):
    
    if depth==3:
        return values[nodeIndex]
    
    if (maximizingPlayer):
        for i in range(2):
            val =minmax(depth+1 ,nodeIndex *2 +i,False ,values,alpha,beta)
            alpha =max(alpha,val)
            if (beta <=alpha):
                break
        return alpha
    
    else:
        for i in range(2):
            val =minmax(depth+1,nodeIndex *2 +i ,True ,values ,alpha ,beta)
            beta =min(beta,val)
            if(beta<=alpha):
                break
        return beta

values=[-1,3,5,1,-6,-4,0,9]
print("The optimal value is : {}" .format(minmax(0, 0, True, values, -1000, 1000)))

#-1000 is negative infinity which is worst possible score for white  (alpha)
#+1000 is positive infinity which is worst possiblke score for black  (beta)
        
