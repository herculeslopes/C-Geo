if ((option == 'ACIMA') and (Ycg + fibra <= y + b)) or ((option == 'ABAIXO') and (Ycg - fibra >= 0)):
                    if Ycg > y:
                        if option == 'ABAIXO':
                            if Ycg - fibra < y:
                                h = Ycg - fibra
                                S = h * z * ((h / 2) + fibra)
                                print('1')
                            
                            elif Ycg - fibra > y:
                                d = Ycg - fibra - y
                                S = (d * x * ((d / 2) + fibra)) + (y * z * ((y / 2) + d + fibra))
                                print('2')

                            elif Ycg - fibra == y:
                                S = y * z * (y / 2) + fibra
                                print('3')

                        elif option == 'ACIMA':
                            if Ycg + fibra < ( y + b):
                                i = y + b  - (Ycg + fibra)
                                S = i * x * ((i / 2) + fibra)
                                
                            print('4')
                            

                        
                    elif Ycg < y:
                        if option == 'ACIMA':

                            if (Ycg + fibra) == y:

                                S = b * x * ((b / 2) + fibra)

                            elif (Ycg + fibra) < y:

                                i = y - (Ycg + fibra)

                                S = (b * x * ((b / 2 )+ (fibra + i))) + (i * z * ((i/2) + fibra))

                            elif (Ycg + fibra) > y: 
                                
                                a = (Y + b) - (Ycg + fibra)

                                S = a * x * ((a/2) + fibra)        

                         
                         elif option == 'ABAIXO':

                            if(Ycg - fibra < y):

                               d = Ycg - fibra
                                
                               S = d * z * ((d / 2 ) + fibra)
  
                        print('5')
                        

                    else Ycg == y:
                        if option 'ACIMA':

                            if (Ycg + fibra) > y:

                                a = b - fibra

                                S = a * x * ((a / 2) + fibra)
                        
                        print('6')
                        
                        elif option 'ABAIXO':

                            if ( Ycg - fibra) < Y   

                                a = Ycg - fibra

                                S = a * z * ((a / 2) + fibra) 

                        print('7')

                    sLabel['text'] = S
                    
                else:
                    sLabel['fg'] = '#eb4034'
                    sLabel['text'] = 'NÃO É POSSÍVEL CALCULAR'
                    print('8')




                                            CALCULO DO I Romano

