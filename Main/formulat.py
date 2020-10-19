# REGRAS GERAIS PARA CALCULAR O T
#jentry
#posicionentry ACIMA OR ABAIXO
#qual a posição da sua fibra em relação ao cg?
#qual a distancia da sua fibra em relação ao cg?




posicionentry acima 


if ycg + jentry < y + b 

se a informação acima é false ela dira que não é possivel calcular, se é true ela usara formulas abaixo

else:
sLabel['fg'] = '#eb4034'
 sLabel['text'] = 'NÃO É POSSÍVEL CALCULAR'

 posicionentry abaixo 

 if ycg - jentry > 0 

 else:
sLabel['fg'] = '#eb4034'
 sLabel['text'] = 'NÃO É POSSÍVEL CALCULAR'

 ESSAS REGRAS ACIMA SÃO GERAIS IRA PASSAR EM TODOS, AGORA IREI CRIAR REGRAS PARA CADA POSIÇÃO POSSIVEL DO YCG. NO RETANGULO DEBAIXO,
 BEM NO MEIO OU NO RETANGULO ACIMA.

 CONDIÇÃO PARA QUANDO O YCG > Y , ELE UTILIZARA AS FORMULAS ABAIXO

 BOM ELE ESCOLHEU UM 'jentry' E A posicionentry 'ABAIXO'

ELE VAI RODAR PARA VERIFICAR AS CONDICOES 


                        CONDIÇÃO ONE

if ((ygc - j )< y)

se essa condição é true o programa efetuara os seguintes caluclos
caso ela seja falsa ele vera a condição abaixo elif

   h = ycg - jentry


   e jogara na formula abaixo para dar a resposta (s)


   				S = h * z * ((h/2)+ jentry)

   				Essa seria a resposta exibida 


   						
   						CONDIÇÃO TWO

elif ((ycg - jentry )> y)
se essa condição é true o programa efetuara os seguintes caluclos
caso ela seja falsa ele vera a condição abaixo elif

	d = (ycg - jentry) - y

	S = (d * x * ((d/2) + jentry)) + (y * z * ((y/2) + d + jentry))


			Essa seria minha resposta


elife (ycg - j) = y 

se essa condição é true o programa efetuara os seguintes caluclos
caso ela seja falsa ele vera a condição abaixo elif		

	
	S = (y * z *(y/2) + jentry)
