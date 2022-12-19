"""
Cree una función hollow_triangle(altura) que devuelva un triángulo hueco de la altura correcta. La altura se pasa a través de la función y la función debe devolver una lista que contiene cada línea del triángulo hueco.

hollow_triangle(6)

 should return : ['_____#_____', '____#_#____', '___#___#___', '__#_____#__', '_#_______#_', '###########']

hollow_triangle(9)

 should return : ['________#________', '_______#_#_______', '______#___#______', '_____#_____#_____', '____#_______#____', '___#_________#___', '__#___________#__', '_#_____________#_', '#################'"""


def hollow_triangle(n):
    lista=[]
    for i in range(n):
        if 0<=i<=n-1:
          lista.append("_"*(n-i-1)+"#"+"_"*(i)+"#"+"_"*(n-i-1))
        else:
            lista.append("#"*(n-+3))
    print(lista)
hollow_triangle(6)



if __name__=='__main__':
