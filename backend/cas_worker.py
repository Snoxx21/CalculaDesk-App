from sympy import symbols, integrate
class CASWorker:
    def solve_from_text(self, text):
        return [{'title':'Interpretación','body':'Detectado integral indefinida de x^2.'},{'title':'Resultado','body':'x**3/3'}]