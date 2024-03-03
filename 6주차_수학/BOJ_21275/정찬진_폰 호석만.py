import sys

dic = {"a":10,"b":11,'c':12,'d':13,'e':14,'f':15,'g':16,'h':17,'i':18,'j':19,'k':20,'l':21,'m':22,'n':23,'o':24,'p':25,'q':26,'r':27,'s':28,'t':29,'u':30,'v':31,'w':32,'x':33,'y':34,'z':35}
a,b = sys.stdin.readline().split()
X, A , B =0, 0, 0
cnt = 0
for i in range(2,37):
  try:
    a_tmp = int(a,i)
  except:
    continue
  for j in range(2,37):
    try:
      b_tmp = int(b,j)

      if a_tmp == b_tmp:
        cnt += 1
        X = a_tmp
        A = i
        B = j
    except:
      continue
if cnt == 1:
  if X >= pow(2,63) or X<0 or A==B:
      print("Impossible")
  else:
    print(X,A,B)
elif cnt == 0:
  print('Impossible')
else:
  print('Multiple')
