c = (input("Introduce texto: "))

empiezaPalabra = True

while(c!='.'):
    while(c != '.' and c == ' '):
        c = input()
    
    while(empiezaPalabra == True):
        print(c)
        empiezaPalabra = False
    
    empiezaPalabra = True
    
    while(c != '.' and c !=' '):
        c = input()
