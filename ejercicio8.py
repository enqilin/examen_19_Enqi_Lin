import re
def search(frase):
    patron = re.compile(r'(\w+)(\s)(\w+)')
    resultado = patron.search(frase)
    if resultado:
        print resultado.group(1)
        print resultado.group(3)
    else:
        print "No se encontro coincidencia"

if __name__ == '__main__':
    search("Siempre va a tratarse de Tree Fiddy")
