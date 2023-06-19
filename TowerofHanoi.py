def TowerofHanoi(n, source, destination, auxiliary):
   if n==1:
       print("move disk from source",source,"to destination",destination)
       return
   TowerofHanoi(n-1,source,auxiliary,destination)
   print("move disk",n,"from source",source,"to destination",destination)
   TowerofHanoi(n-1,auxiliary,destination,source)

n=4
TowerofHanoi(n, 'A' , 'B' , 'C')
