
def search(frase):
    str=frase.slower()
    if str in "tree fiddy" and "three fifty" or "3.50":
        return True
    else:
        return "No coincidencia"
    
if __name__=="__main__":
    search("Siempre va a tratarse de Tree Fiddy")
