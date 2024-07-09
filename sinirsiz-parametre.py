def limitlessParameters(*args):
    parameteres=list(args)
    print(parameteres)

limitlessParameters("Ali","Veli","Mustafa",5.3)


##############################################################################################

def limitlessDictionary(**parameters):
   for key,value in parameters.items():
       print(f"Anahtar : {key} , Deger : {value}")

    
limitlessDictionary(name="Omer Faruk",surname="BINGOL",job="Computer Programmer")