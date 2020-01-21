a=int(input('Enter the number of coin tossed'))
b=int(input('Enter the number of times coin tossed'))
c=int(input('Enter the no of sucess of h/t you want'))
p=1/2
q=1/2
f=a-c
fact1=1
fact2=1
fact3=1
for i in range(1,a+1) :
  fact1=fact1*i
for j in range(1,c+1) :
  fact2=fact2*j
for k in range(1,f+1) :
  fact3=fact3*k

ans=(fact1/fact3*fact2)(pc)(q**(a-c))*b
print('The probability of sucess is', ans)
