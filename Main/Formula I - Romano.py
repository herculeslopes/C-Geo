Formula I - Romano.py



if ((option == 'ACIMA') and (Ycg + fibra <= y + d + h)) or ((option == 'ABAIXO') and (Ycg - fibra >= 0)):
					if Ycg >= (h + d):
						if option == 'ACIMA':
                            if (Ycg + fibra) < (y + d + h):
                            	i = ((Ycg + fibra) - (y + h + d))
                            	S = i * x * ((i/2) + fibra)

                        elif option == 'ABAIXO':
                            if ( Ycg - fibra) <= (d + h) and (Ycg - fibra) > (d):
                                i = ( d + h) - (Ycg - fibra)
                                S = ((i * a * ((i / 2) + fibra)) + (d * r * ((d / 2) + i + fibra)))

                            elif (Ycg - fibra) <= (d):
                                u = ( Ycg - fibra)  
                                S = u * r * ((u / 2) + fibra)

                            elif (Ycg - fibra) > (d + h):    
                                u = (Ycg - fibra) - (h + d)
                                S = (u * x * ((u / 2 ) + fibra)) + (h * a * ((h / 2) + u + fibra)) + d * r * ((d / 2) + h + u + fibra)

                    elif ( Ycg > d ) and Ycg <= ( d + h):     
                        if option =='ACIMA':      
                        	if (Ycg + fibra) >= (d + h):
                        	    i = ( d + h + y) - (Ycg + fibra)
                        	    S = i * x * ((i / 2) + fibra)
                        	
                        	elif (Ycg + fibra) <= ( d + h) and (Ycg + fibra) >= (d):
                        	    i = (d + h) - (Ycg + fibra)
                        	    S = (y * x * ((y / 2) + i + fibra)) + (i * a * ((i / 2) + fibra))

                        elif option == 'ABAIXO':
                            if (Ycg - fibra) > (d):
                                v = (d + h) - ( Ycg - fibra)    
                                S = (v * a * ((v / 2) + fibra)) + (d * r * ((d / 2) + fibra))

                            elif (Ycg - fibra) <= (d): 
                                v = (Ycg - fibra)
                                S = v * r * ((v / 2) + fibra)

                    elif ( Ycg <= d ):
                        if option == 'ABAIXO':
                        	if ( Ycg - fibra) <= (d):
                        	    g = (Ycg - fibra)
                        	    S = g * r * ((g / 2)+ fibra)

                        elif option == 'ACIMA':
                        	if (Ycg + fibra) >= (d + h):
                        	    i = (d + h + fibra) - (Ycg + fibra)
                        	    S = (i * x * ((i / 2)+ fibra))

                        	elif (Ycg + fibra) >= (d):
                        	    m = (h + d) - (Ycg + fibra)    
                        	    S = y * x * ((y / 2) + fibra)

                        	elif (Ycg + fibra) < (d):   
                        	    m = (d) - (Ycg + fibra)
                        	    S = (y * x * ((y / 2) + h + m + fibra)) + (h * a * ((h / 2) + m + fibra)) + (m * r * ((m / 2) + fibra)) 