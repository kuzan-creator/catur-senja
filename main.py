import json,os,urllib.request as u
U=os.getenv('MAKEFUN_ENV_URL')
M=[82,337,365,477,1025,0]
P="kkkkuuuummoqllmpkkkoljiklmmgkkkk"
J="aceecgkkekmnelnoeknoelmncgklacee"
W="eccaeccaeccaeccageecigggookkoqmk"
Z="k"*32
Y=[P,J,Z,Z,Z,W]
D=[0,[-33,-31,-18,-14,14,18,31,33],[-17,-15,15,17],[-16,-1,1,16],[-17,-16,-15,-1,1,15,16,17]]
b=bytearray(128);S=1;C=15;EP=-1;KW=4;KB=116;n=0;NB=6e4
def k(q,w):
 for d in (-15,-17) if w else (15,17):
  o=q+d
  if not o&136 and b[o]==(1 if w else 7):return 1
 for d in D[1]:
  o=q+d
  if not o&136 and b[o]==(2 if w else 8):return 1
 for d in D[4]:
  o=q+d;j=0
  while not o&136:
   v=b[o]
   if v:
    if (v<7)==w:
     t=(v-1)%6
     if t==4 or t==(2 if d in D[2] else 3) or (j==0 and t==5):return 1
    break
   o+=d;j+=1
 return 0
def G():
 L=[];a=L.append
 def ap(f,t):
  if t>>4 in (0,7):
   for pr in (5,2,4,3):a(f+t*128+pr*16384)
  else:a(f+t*128)
 for s in range(128):
  if s&136:continue
  q=b[s]
  if not q or (q<7)!=S:continue
  t=(q-1)%6
  if t==0:
   d=16 if S else -16
   o=s+d
   if not b[o]:
    ap(s,o)
    if (s>>4)==(1 if S else 6) and not b[s+2*d]:a(s+(s+2*d)*128)
   for o in (s+d-1,s+d+1):
    if o&136:continue
    v=b[o]
    if v and (v<7)!=S:ap(s,o)
    elif o==EP:a(s+o*128)
  else:
   for d in D[t if t<5 else 4]:
    o=s+d
    while not o&136:
     v=b[o]
     if v:
      if (v<7)!=S:a(s+o*128)
      break
     a(s+o*128)
     if t in (1,5):break
     o+=d
 if S and not k(4,0):
  if C&1 and not b[5] and not b[6] and not k(5,0):a(772)
  if C&2 and not b[1] and not b[2] and not b[3] and not k(3,0):a(260)
 elif not S and not k(116,1):
  if C&4 and not b[117] and not b[118] and not k(117,1):a(15220)
  if C&8 and not b[113] and not b[114] and not b[115] and not k(115,1):a(14708)
 return L
def K(m):
 global S,C,EP,KW,KB
 z=(bytes(b),S,C,EP,KW,KB)
 f=m&127;t=(m>>7)&127;pr=m>>14
 q=b[f];pt=(q-1)%6
 if pt==0 and t==EP:b[t-16 if S else t+16]=0
 b[t]=pr+(0 if S else 6) if pr else q
 b[f]=0
 if pt==5:
  if S:KW=t
  else:KB=t
  if t-f==2:b[t-1]=b[t+1];b[t+1]=0
  elif f-t==2:b[t+1]=b[t-2];b[t-2]=0
 for x in (f,t):C&=~(2*(x==0)+(x==7)+8*(x==112)+4*(x==119))
 if pt==5:C&=~(3 if S else 12)
 EP=-1
 if pt==0 and abs(t-f)==32:EP=(f+t)//2
 S=not S
 return z
def V(z):
 global S,C,EP,KW,KB
 b[:]=z[0];S,C,EP,KW,KB=z[1:]
def N():
 L=[]
 for m in G():
  z=K(m)
  if not k(KW if not S else KB,S):L.append(m)
  V(z)
 return L
def E():
 m=0
 for r in range(8):
  for f in range(8):
   q=b[r*16+f]
   if q:
    t=(q-1)%6
    w=1 if q<7 else -1
    i=((7-r) if w>0 else r)*4+min(f,7-f)
    m+=w*(M[t]+(ord(Y[t][i])-107)*5)
 d=abs((KW&7)-(KB&7))+abs((KW>>4)-(KB>>4))
 if m>300:m+=(14-d)*2
 elif m<-300:m-=(14-d)*2
 return m if S else -m
def O(m):
 v=b[(m>>7)&127]
 return 10000+M[(v-1)%6] if v else 0
def R(d,a,be,pl):
 global n
 n+=1
 if n>NB:b[200]
 if d<1:return E()
 ms=N()
 if not ms:return -100000+pl if k(KW if S else KB,not S) else 0
 ms.sort(key=O,reverse=True)
 for m in ms:
  z=K(m);v=-R(d-1,-be,-a,pl+1);V(z)
  if v>=be:return be
  if v>a:a=v
 return a
def F(m):
 f=m&127;t=(m>>7)&127;pr=m>>14
 return '%c%d%c%d%s'%(97+(f&7),f//16+1,97+(t&7),t//16+1,'  nbrq'[pr] if pr else '')
def H(f):
 global S,C,EP,KW,KB
 p=f.split()
 b[:]=[0]*128
 s=112
 for ch in p[0]:
  if ch=='/':s-=24
  elif ch.isdigit():s+=int(ch)
  else:
   q='PNBRQKpnbrqk'.index(ch)+1
   b[s]=q;s+=1
   if q==6:KW=s-1
   elif q==12:KB=s-1
 S=p[1]=='w'
 C=sum(1<<i for i,c in enumerate('KQkq') if c in p[2])
 EP=-1 if p[3]=='-' else (ord(p[3][0])-97)+(int(p[3][1])-1)*16
def B(legal):
 global n
 ms=[m for m in N() if F(m) in legal]
 ms.sort(key=O,reverse=True)
 bb=ms[0];n=0
 try:
  for d in range(1,64):
   a=-100000
   for m in ms:
    z=K(m);v=-R(d-1,-100000,-a,1);V(z)
    if v>a:a=v;bb=m
 except IndexError:pass
 return F(bb)
def T(p,d):
 q=u.Request(U+p,json.dumps(d).encode(),{'content-type':'application/json'})
 return json.load(u.urlopen(q))
if __name__=='__main__':
 while 1:
  g=T('/game',{})
  if g['status']=='done':break
  while g['status']=='your_move':
   H(g['fen'])
   g=T('/move',{'game':g['game'],'move':B(g['legal_moves'])})
