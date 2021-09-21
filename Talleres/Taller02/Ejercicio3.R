# Planteamos el sistema de ecuaciones
a1<-c(10, 10^2, exp(0.15*10))
a2<-c(15, 15^2, exp(0.15*15))
a3<-c(20, 20^2, exp(0.15*20))
b<-c(25, 130, 650)
# Resolveremos el sistema de ecuaciones utilizando un parámetro w= 1.2
# x(1,k+1)=(w/a11)(-a12x(2,k)-a13x(3,k)+b1)+(1-w)x(1,k)
# x(2,k+1)=(w/a22)(-a21x(1,k+1)-[a(2,3)x(3,k)]+b2)+(1-w)x(2,k)
# x(3,k+1)=(w/a33)(-a31x(1,k+1)-a32x(2,k+1)+b3)+(1-w)x(3,k)

w=1.2 ;  # Parametro de relajacion 
x1<-c(1,1,1) # Aproximacion inicial
x2<-c(0,0,0) 

x2[1]<-(w/a1[1])*(-a1[2]*x1[2]-a1[3]*x1[3]+b[1])+(1-w)*x1[1]
x2[2]<-(w/a2[2])*(-a2[1]*x2[1]-a2[3]*x1[3]+b[2])+(1-w)*x1[2]
x2[3]<-(w/a3[3])*(-a3[1]*x2[1]-a3[2]*x2[2]+b[3])+(1-w)*x1[3]

y<-x2

# Criterio de parada  Abs(X(K)-X(K-1))< 0.01
epsilon<-0.01
iteraciones<-0

while(norm(as.matrix(x2-x1),"f")>0.001){
 y[1]<-(w/a1[1])*(-a1[2]*x2[2]-a1[3]*x2[3]+b[1])+(1-w)*x2[1]
 y[2]<-(w/a2[2])*(-a2[1]*y[1]-a2[3]*x2[3]+b[2])+(1-w)*x2[2]
 y[3]<-(w/a3[3])*(-a3[1]*y[1]-a3[2]*y[2]+b[3])+(1-w)*x2[3]
 x1<-x2
 x2<-y 
 iteraciones<-iteraciones+1
}

y

# Utilizamos un método preprogramado en R

p <- function(x){return(y[1]*x+y[2]*x^2+y[3]*exp(0.15*x)-1500) }
uniroot(p, interval=c(0,100))
# Solucion aprox 23

p <- function(x){return(y[1]*x+y[2]*x^2+y[3]*exp(0.15*x)-1800) }
uniroot(p, interval=c(0,100))
# Solucion aprox 24

p <- function(x){return(y[1]*x+y[2]*x^2+y[3]*exp(0.15*x)-2000) }
uniroot(p, interval=c(0,100))
# Solucion aprox 25


# Verificamos soluciones encontradas programando un método Newton-Rapshon
install.packages("numDeriv")
library(numDeriv)

x0=1        # Valor Inicial
tol=0.001   # Tolerancia 
p <- function(x){return(y[1]*x+y[2]*x^2+y[3]*exp(0.15*x)-1500) }
dx <- genD(func = p, x = x0)$D[1]
aux<-x0-p(x0)/dx
xk<-aux
itera<-0
while (abs(p(x0))>tol) {
  dx <- genD(func = p, x = aux)$D[1]
  xk<-aux-p(aux)/dx
  x0<-xk
  aux<-xk
  itera<-itera+1
}
xk
# Valor obtenido 23.34305
#----------------------------------------------------------------------------

x0=1        # Valor Inicial
tol=0.001   # Tolerancia 
p <- function(x){return(y[1]*x+y[2]*x^2+y[3]*exp(0.15*x)-1800) }
dx <- genD(func = p, x = x0)$D[1]
aux<-x0-p(x0)/dx
xk<-aux
itera<-0
while (abs(p(x0))>tol) {
  dx <- genD(func = p, x = aux)$D[1]
  xk<-aux-p(aux)/dx
  x0<-xk
  aux<-xk
  itera<-itera+1
}
xk
# Valor obtenido 24.14421
#-----------------------------------------------------------------------------

x0=1        # Valor Inicial
tol=0.001   # Tolerancia 
p <- function(x){return(y[1]*x+y[2]*x^2+y[3]*exp(0.15*x)-2000) }
dx <- genD(func = p, x = x0)$D[1]
aux<-x0-p(x0)/dx
xk<-aux
itera<-0
while (abs(p(x0))>tol) {
  dx <- genD(func = p, x = aux)$D[1]
  xk<-aux-p(aux)/dx
  x0<-xk
  aux<-xk
  itera<-itera+1
}
xk
# Valor obtenido 24.6188
