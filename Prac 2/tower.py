##def TowerOfHanoi(n , from_rod, to_rod, aux_rod):
##    if n == 1:
##        print ("Move disk 1 from rod",from_rod,"to rod",to_rod)
##        return
##    TowerOfHanoi(n-1, from_rod, aux_rod, to_rod)
##    print ("Move disk",n,"from rod",from_rod,"to rod",to_rod)
##    TowerOfHanoi(n-1, aux_rod, to_rod, from_rod)
##         
### no of disk
##n = 3
##TowerOfHanoi(n, 'A', 'C', 'B') 


def  t(n, beg,  aux,  end):
  if(n == 1):
    print("{} --> {} \n".format( beg ,end))
  else:
    t(n-1, beg, end, aux)
    t(1, beg, aux, end)
    t(n-1, aux, beg, end)

print("Moves\n")
t(3, 'a', 'b', 'c')	




