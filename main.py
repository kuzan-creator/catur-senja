import os,json,urllib.request as u
V=[100,320,330,500,1000,0]
D=[-17,-15,15,17,-16,-1,1,16]
O=[[-33,-31,-18,-14,14,18,31,33],D[:4],D[4:],D,D]
R={0:13,7:14,112:7,119:11}
T="PPPPQRRLQONPPPPTQQRURRTVZZZZPPPPFHJJHLPQLQRSLPSSJQSSJPRSHLPPFHJJLNNNNQPPNRRRNPRRNQQRNPQRNPPPLNNNPPPQOPPPOPPPOPPPOPPPOPPPQRRRPPPPLNNONPQPNQQQPPQQOPQQNPQQNPPPLNNOTVRPTTPPNLLLLJHHJHHFJHHFJHHFJHHFFJJJJJPPJNTVJNVXJNVXJNTVJLNPFHJL"
B=[0]*128;W=1;C=0;E=-1;Kw=4;Kb=116;N=0;BD=80e3
def atk(s,y):
 g=1 if y else-1
 for o in O[0]:
  t=s+o
  if not t&136 and B[t]==2*g:return 1
 for i,o in enumerate(D):
  t=s+o
  while not t&136:
   q=B[t]
   if q:
    if q==5*g or q==(3*g if i<4 else 4*g)or(q==g and t==s+o and(i<2 if g>0 else 1<i<4))or(q==6*g and t==s+o):return 1
    break
   t+=o
 return 0
def gen(c=0):
 m=[]
 A=lambda t:m.__iadd__([s|t<<7|z<<14 for z in(5,4,3,2)]if(t>>4)==l else[s|t<<7])
 for s in range(128):
  if s&136:continue
  p=B[s]
  if not p or(p>0)!=W:continue
  a=abs(p)
  if a==1:
   d=(16,-16)[p<0];l=(7,0)[p<0]
   t=s+d
   if not t&136 and not B[t]and(not c or(t>>4)==l):
    A(t)
    if(s>>4)==(1,6)[p<0]and not B[s+2*d]:m.append(s|(s+2*d)<<7)
   for o in(d-1,d+1):
    t=s+o
    if t&136:continue
    q=B[t]
    if(q and(q>0)!=(p>0))or t==E:A(t)
  else:
   for o in O[a-2]:
    t=s+o
    while not t&136 and(not B[t]or(B[t]>0)!=(p>0)):
     if B[t]or not c:m.append(s|t<<7)
     if B[t]or a in(2,6):break
     t+=o
   if a==6 and not c:
    k=4 if W else 116;y=not W
    for b,d in((1,1),(2,-1)):
     if C&(b if W else 4*b)and not(B[k+d]or B[k+2*d]or(d<0 and B[k+3*d]))and not any(atk(x,y)for x in(k,k+d,k+2*d)):m.append(k|(k+2*d)<<7)
 return m
def mk(m):
 global W,C,E,Kw,Kb
 st=(B[:],W,C,E,Kw,Kb)
 f=m&127;t=m>>7&127;z=m>>14&7;p=B[f]
 if abs(p)==1 and t==E and not B[t]:B[t+(16,-16)[p>0]]=0
 if abs(p)==6:
  (Kw:=t)if p>0 else(Kb:=t)
  if abs(t-f)==2:
   x=f+3 if t>f else f-4;y=f+1 if t>f else f-1;B[y]=B[x];B[x]=0
 B[t]=z*(1,-1)[p<0]if z else p;B[f]=0
 C&=(12 if p==6 else 3 if p==-6 else 15)&R.get(f,15)&R.get(t,15)
 E=(f+t)//2 if abs(p)==1 and abs(t-f)==32 else-1
 W=not W
 return st
def un(st):
 global W,C,E,Kw,Kb
 B[:]=st[0];W,C,E,Kw,Kb=st[1:]
def ev():
 g=h=y=0
 for s,p in enumerate(B):
  if p and not s&136:
   a=abs(p)-1;w=1 if p>0 else-1;t=s if p>0 else s^112
   j=(t>>4)*4+min(t&7,7-(t&7))
   g+=w*(V[a]+(ord(T[a*32+j])-80)*5)
   h+=w*(V[a]+(ord(T[(a+(a==5))*32+j])-80)*5)
   y+=V[a]//250
 y=min(y,24)
 s=(g*y+h*(24-y))//24
 return s if W else-s
om=lambda ms:(ms.sort(key=lambda m:-V[abs(B[m>>7&127])-1]),ms)[1]
def sr(d,a,b,p):
 global N
 N+=1
 if N>BD:return 0
 K=Kw if W else Kb
 if d<=0:
  k=atk(K,not W)
  if not k:
   s=ev()
   if s>=b:return b
   a=max(a,s)
  ms=om(gen(not k))
 else:ms=om(gen());k=0
 n=0
 for m in ms:
  st=mk(m)
  if atk(Kw if not W else Kb,W):un(st);continue
  n+=1
  v=-sr(d-1,-b,-a,p+1)
  un(st)
  if v>a:a=v
  if a>=b:break
 if not n and(d>0 or k):return-99999+p if atk(K,not W)else 0
 return a
def root():
 global N
 ms=gen()
 bm=ms[0];N=0
 for d in range(1,25):
  db=0;a=-9**9;n=0
  for m in [bm]+[x for x in om(ms)if x!=bm]:
   st=mk(m)
   if atk(Kw if not W else Kb,W):un(st);continue
   n+=1
   v=-sr(d-1,-9**9,-a,1)
   un(st)
   if v>a:a=v;db=m
  if N>BD or not n:break
  bm=db
 return bm
def setfen(f):
 global B,W,C,E,Kw,Kb
 B=[0]*128;C=0;E=-1
 z=f.split();s=112
 for ch in z[0]:
  if ch=='/':s-=24
  elif ch.isdigit():s+=int(ch)
  else:
   p='PNBRQK'.index(ch.upper())+1
   B[s]=p if ch<'a' else-p
   if p==6:(Kw:=s)if ch<'a' else(Kb:=s)
   s+=1
 W=z[1]=='w'
 C=sum(1<<'KQkq'.index(c)for c in z[2]if c in'KQkq')
 E=z[3]!='-'and(ord(z[3][0])-97)+16*(int(z[3][1])-1)or-1
def uci(m):
 z=m>>14&7
 return''.join(chr(97+(x&7))+str((x>>4)+1)for x in(m&127,m>>7&127))+('nbrq'[z-2]if z else'')
def call(p,d):
 return json.load(u.urlopen(U+p,json.dumps(d).encode()))
U=os.getenv('MAKEFUN_ENV_URL','')
if U:
 g=call('/game',{})
 while g['status']!='done':
  while g['status']=='your_move':
   setfen(g['fen']);v=uci(root());L=g['legal_moves']
   if v not in L:v=L[0]
   g=call('/move',{'game':g['game'],'move':v})
  g=call('/game',{})
