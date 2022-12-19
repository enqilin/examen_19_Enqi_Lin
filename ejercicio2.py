
"""Cuando asistíamos a la escuela secundaria, se nos pidió que simplificáramos expresiones matemáticas como "3x-yx+2xy-x" (o generalmente más grande), y eso fue muy fácil ("2x+xy"). ¡Pero díselo a tu pc y ya veremos!

Existen varias formas de simplificar una expresión matemática, pero una posible solución a su problema sería utilizar la regla de la suma y del producto de los exponentes para combinar términos similares en la expresión.

Por ejemplo, la expresión "3x-zx+2xy-x" se podría simplificar de la siguiente manera:

Identificar los términos que tienen la misma base (por ejemplo, "x") y agruparlos juntos: "3x - x + 2xy - zx"
Aplicar la regla de la suma y del producto de los exponentes para cada grupo de términos:
Para el grupo "3x - x", el exponente de la base "x" es 1 en ambos términos, por lo que se pueden combinar utilizando la regla de la suma de exponentes: 3x - x = 2x
Para el grupo "2xy - zx", el exponente de la base "x" es 1 en ambos términos, por lo que se pueden combinar utilizando la regla de la suma de exponentes: 2xy - zx = (2-z)xy
Reemplazar cada grupo de términos simplificados en la expresión original: "3x - x + 2xy - zx" se convierte en "2x + (2-z)xy"""


import numpy as np
def simplify(polimonio):
    
    if polimonio[0] == "+":
        polimonio = polimonio[1:]




if __name__ == '__main__':
    simplify(3x-zx+2xy-x)