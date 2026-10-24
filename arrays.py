import array
k = array.array('d',[1.2,2.8,3.9,4.0,])
print(k)
#adding an element
k.append(5.0)
print(k)
#extanding an array
k.extend([2.0,6.0])
print(k)
#deleting an element
print(k.pop(5))
print(k)
print(k.pop(5))
print(k)
