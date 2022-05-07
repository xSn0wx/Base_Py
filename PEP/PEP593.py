from typing import Annotated

def imc(poids: Annotated[float, "kg"], taille: Annotated[float, "m"]) -> float:
    return poids / (taille * taille)

print(imc(67.2, 1.75))
print(imc.__annotations__)