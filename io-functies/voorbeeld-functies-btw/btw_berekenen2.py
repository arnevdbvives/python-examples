def korting(prijs: float, korting: float) -> float:
    """Berekent de prijs na korting
    """
    return prijs * (1 - korting/100)

def bedrag_met_btw(prijs: float) -> float:
    """Berekent de prijs met btw
    """
    return prijs * 1.21


bedrag = float(input("Geef een bedrag: "))
kortingspercentage = float(input("Geef het kortingspercentage: "))
prijs = bedrag_met_btw(korting(bedrag, kortingspercentage))
print(f"Het te betalen bedrag is {prijs:.2f}.")

