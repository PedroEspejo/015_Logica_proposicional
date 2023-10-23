import sympy

# Definimos símbolos para p y q
p = sympy.symbols('p')
q = sympy.symbols('q')

# Ejemplo de proposición p or not p (tautología)
proposicion_tautologia = p | ~p

# Ejemplo de proposición p and q (no es una tautología)
proposicion_no_tautologia = p & q

# Función para verificar si una proposición es una tautología
def es_tautologia(proposicion):
    return sympy.simplify_logic(proposicion) == True

# Verificamos si las proposiciones son tautologías
tautologia = es_tautologia(proposicion_tautologia)
no_tautologia = es_tautologia(proposicion_no_tautologia)

print(f"(p ∨ ¬p) es una tautología: {tautologia}")
print(f"(p ∧ q) no es una tautología: {not no_tautologia}")
