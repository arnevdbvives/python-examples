import btw_functies as btw

bedrag = float(input("Geef een bedrag: "))
korting = float(input("Geef het kortingspercentage: "))
prijs = btw.bedrag_met_btw(btw.korting(bedrag,korting))
print(f"Het te betalen bedrag is {prijs:.2f}.")

