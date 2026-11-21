import json,os
import urllib.request as u
B="A?AAAA?A"
R="A?????B@"
Q="A@@A@@?A"
A=["@A?ACDJ@","8<ADAC<8",B,R,Q,"CB@:8888"]
E=["@@ABDFJ@",":<ADAC<8",B,R,Q,"9<ABBA<9"]
V=(0,82,337,365,477,1025,0)
Y=(0,0,1,1,2,4,0)
Z={4:12,116:3,0:13,7:14,112:7,119:11}
G=(-33,-31,-18,-14,14,18,31,33)
K=(-17,-16,-15,-1,1,15,16,17)
GK=G+K
L=(-17,-15,15,17)
M=(-16,-1,1,16)
S=lambda x:ord(x[0])+ord(x[1])*16-881
b=[0]*128
w=True
CA=0
EP=-1
J=[116,4]
U=[]
D={}
H=set()
C=0
F=0
N=50000
def att(s,q):
 e=1 if q else -1
 for o in GK:
  if not (s+o)&136 and (b[s+o]==(6*e if o in K else 2*e) or (b[s+o]==e and o*e in (-15,-17))):return 1
  if o in K:
   t=s+o
   while not t&136 and not b[t]:t+=o
   if not t&136 and (b[t]==5*e or b[t]==(3*e if o in L else 4*e)):return 1
 return 0
def gn():
 m=[]
 e=1 if w else -1
 for s in range(120):
  if s&8:continue
  p=b[s]
  if not p or (p>0)!=w:continue
  q=abs(p)
  if q==1:
   d=32*w-16
   for t in (s+d,s+d-1,s+d+1):
    if t&136:continue
    c=b[t]
    if (t==s+d and not c) or (t!=s+d and (c*e<0 or t==EP)):
     if (t>>4)==7*w:
      for r in range(5,1,-1):m.append(s|t<<7|r<<14)
     else:
      m.append(s|t<<7)
      if t==s+d and (s>>4)==6-5*w:
       u=s+d*2
       if not b[u]:m.append(s|u<<7)
  elif q==2 or q==6:
   for o in (G,K)[q==6]:
    t=s+o
    if not t&136 and b[t]*e<=0:m.append(s|t<<7)
  else:
   for o in (L,M,K)[q-3]:
    t=s+o
    while not t&136 and b[t]*e<=0:
     m.append(s|t<<7)
     if b[t]:break
     t+=o
 for i,(f,t) in enumerate(((4,6),(4,2),(116,118),(116,114))):
  if CA>>i&1 and i//2^w and not (b[(f+t)//2] or b[t] or b[f+1 if t>f else f-3]) and all(not att(x,i>1) for x in (f,(f+t)//2,t)):m.append(f|t<<7)
 return m
def mu(m,k):
 global CA,EP,w
 f=m&127;t=(m>>7)&127;pr=m>>14
 if k>0:
  p=b[f];c=b[t];cs=t
  if p*p==1 and t==EP:
   cs=t-16*p;c=b[cs];b[cs]=0
  U.append((p,c,cs,CA,EP))
  b[f]=0
  b[t]=pr*p if pr else p
  if p*p==36:J[w]=t
  CA&=Z.get(f,15)&Z.get(t,15)
  EP=(f+t)//2 if p*p==1 and abs(t-f)==32 else -1
  w=not w
 else:
  p,c,cs,ca,ep=U.pop()
  b[f]=p;b[t]=0
  if c:b[cs]=c
  if p*p==36:J[not w]=f
  CA,EP=ca,ep
  w=not w
 if p*p==36 and abs(t-f)==2:
  r=t+1-3*(t<f);d=t-1+2*(t<f)
  b[r],b[d]=b[d],b[r]
def ev():
 a=c=h=0
 for s,p in enumerate(b):
  if p:
   q=abs(p)
   i=(s>>4)^(7*(p<0))
   v=(ord(A[q-1][i])-64)*5+V[q]
   u=(ord(E[q-1][i])-64)*5+V[q]
   if p<0:v=-v;u=-u
   a+=v;c+=u;h+=Y[q]
 s=(a*h+c*(24-h))//24
 return s if w else -s
def sr(d,a,be,pl):
 global C,F
 C+=1
 if C>N:F=1;return 0
 k=(tuple(b),w,CA,EP)
 if k in H:return 0
 ic=att(J[w],1-w)
 if d<=0 and not ic:
  s=ev()
  if s>=be:return s
  if s>a:a=s
  ms=[m for m in gn() if b[m>>7&127] or m>>7&127==EP]
 else:
  ms=gn()
 pv=D.get(k)
 ms.sort(key=lambda m:(m==pv)*7+abs(b[m>>7&127]),reverse=True)
 n=0
 for m in ms:
  mu(m,1)
  if att(J[not w],w):
   mu(m,-1);continue
  n+=1
  s=-sr(d-1,-be,-a,pl+1)
  mu(m,-1)
  if F:return 0
  if s>=be:return s
  if s>a:a=s;D[k]=m
 if not n and (d>0 or ic):return ic*(pl-99999)
 return a
def rt(ms):
 global C,F,D
 C=0;F=0;D={}
 R=[[0,S(u)|S(u[2:])<<7|('..nbrq'+u[4:]).index(u[4:5])<<14] for u in ms]
 best=R[0][1]
 for d in range(9):
  a=-10**6;nb=best
  for p in R[::-1]:
   mu(p[1],1)
   v=-sr(d-1,-10**6,-a,1)
   mu(p[1],-1)
   p[0]=v
   if v>a:a=v;nb=p[1]
  if F:break
  best=nb;R.sort()
 return best
def ld(f):
 global w,CA,EP
 p=f.split()
 b[:]=[0]*128
 s=112
 for ch in p[0]:
  if ch=='/':s-=24
  elif ch<'A':s+=int(ch)
  else:
   v='PNBRQK'.index(ch.upper())+1
   if ch>'Z':v=-v
   b[s]=v
   if v*v==36:J[v>0]=s
   s+=1
 w=p[1]=='w'
 CA=sum(1<<'KQkq'.find(ch) for ch in p[2] if ch!='-')
 EP=-1 if p[3]=='-' else S(p[3])
def ps(x,d):
 return json.loads(u.urlopen(os.getenv('MAKEFUN_ENV_URL')+x,json.dumps(d).encode()).read())
if __name__=='__main__':
 while 1:
  r=ps('/game',{})
  if r['status']=='done':break
  g=r['game'];H=set()
  while r['status']!='over':
   ld(r['fen'])
   H.add((tuple(b),w,CA,EP))
   m=rt(r['legal_moves'])
   f=m&127;t=(m>>7)&127
   v=chr(97+(f&7))+str((f>>4)+1)+chr(97+(t&7))+str((t>>4)+1)
   if m>>14:v+='..nbrq'[m>>14]
   r=ps('/move',{'game':g,'move':v})
