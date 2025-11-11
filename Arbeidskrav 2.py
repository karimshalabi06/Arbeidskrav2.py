#Arbeidskrav 2 

#Oppgave 1)

# Spør om fødselsåret og lagrer det som et heltall
alder = int(input("Hvilket år er du født? "))

# Beregner alder i 2024
alder_i_2024 = 2024 - alder

# Skriv resultatet
print(f"Du blir {alder_i_2024} år i løpet av 2024.")



#Oppgave 2)

import math  #  Jeg bruker math.ceil() slik at jeg runder opp til nærmeste hel tall

# Ber brukeren først om antall elever
antall_elever = int(input("Skriv inn antall elever: "))

# Hver elev spiser 1/4 pizza.
pizza_per_elev = 1/4

# Beregner totalt antall pizzaer
antall_pizzaer = math.ceil(antall_elever * pizza_per_elev)

# Skriver resultatet 
print(f"Det må handles inn {antall_pizzaer} pizzaer til festen.")



#Oppgave 3)

import numpy as np

# Ber brukeren om å skrive inn gradtallet
v_grad = float(input("Skriv inn gradtallet: "))

# Gjør om fra grader til radianer
v_rad = v_grad * np.pi / 180

# Skriv resultatet 
print(f"{v_grad} grader tilsvarer {v_rad:.4f} radianer.")


#Oppgave 4a)

# Oppretter dictionary med land som nøkkel(key), og [hovedstad, antall innbyggere i mill.] som verdi (value)
data = {
        "Norge": ["Oslo", 0.634],
        "England": ["London", 8.982],
        "Frankrike": ["Paris", 2.161],
        "Italia": ["Roma", 2.873]
        }

# Skriv ut dictionaryen for å sjekke ut at det stemmer  
print("Informasjon om land og hovedsteder:")
print(data)


#Oppgave 4b)


# Oppretter dictionary fra oppgave 4a.
data = {
        "Norge": ["Oslo", 0.634],
        "England": ["London", 8.982],
        "Frankrike": ["Paris", 2.161],
        "Italia": ["Roma", 2.873]
        }

# Ber brukeren skrive inn et land
land = input("Skriv inn et land: ")

# Sjekker om landet finnes i dictionaryen
if land in data:
    hovedstad = data[land][0]
    innbyggere = data[land][1]
    print(f"{hovedstad} er hovedstaden i {land} og det er {innbyggere} mill. innbyggere i {hovedstad}.")
else:
    print(f"Beklager, jeg har ingen informasjon om {land}.")


#Oppgave 4c)

# Bruker den opprinnelige dictionaryen fra oppgave 4a
data =  {
        "Norge": ["Oslo", 0.634],
        "England": ["London", 8.982],
        "Frankrike": ["Paris", 2.161],
        "Italia": ["Roma", 2.873]
        }

# Ber brukeren om informasjon om det nye landet
nytt_land = input('Skriv inn navnet på det nye landet: ')
ny_hovedstad = input('Skriv inn hovedstaden for dette landet: ')
ny_innbyggere = float(input('Skriv inn antall innbyggere i millioner: '))

# Legger til det nye landet i dictionaryen.
# Nøkkelen er navnet på landet, og verdien er en liste med hovedstad og innbyggere.
data[nytt_land] = [ny_hovedstad, ny_innbyggere]

# Skriver ut den oppdaterte dictionaryen 
print('\nOppdatert database:')
print(data)



#Oppg 5)

import numpy as np

def figur_egenskaper(a, b):
    
    # Beregner hypotenusen ved hjelp av Pythagoras
    hypotenus = np.sqrt(a**2 + b**2)

    # Areal av trekant
    areal_trekant = (a * b) / 2

    # Halvsirkel har diameter = a
    radius = a / 2
    areal_halvsirkel = 0.5 * np.pi * radius**2

    # Totalt areal
    areal_total = areal_trekant + areal_halvsirkel

    # Ytre omkrets = kateten b + hypotenus + halvsirkelbue
    omkrets = b + hypotenus + np.pi * radius

    return areal_total, omkrets


# Ber brukeren taste inn verdier
a = float(input("Skriv inn lengden på katet a (i cm): "))
b = float(input("Skriv inn lengden på katet b (i cm): "))

# Kaller funksjonen og henter ut verdiene
areal, omkrets = figur_egenskaper(a, b)

# Skriver resultatet 
print(f"\nArealet av figuren er: {areal:.2f} cm²")
print(f"Den ytre omkretsen av figuren er: {omkrets:.2f} cm")


#Oppg6)

import numpy as np
import matplotlib.pyplot as plt

# Lager 200 punkter jevnt fordelt mellom -10 og 10
x = np.linspace(-10, 10, 200)

# Definerer funksjonen f(x)
y = -x**2 - 5

# Plotter grafen
farge = "red"
plt.plot(x, y, color = farge , label='f(x) = -x² - 5' , linewidth=3)

# Legger til tittel , ruternett, forklaring og div.
plt.title("Plot av funksjonen f(x) = -x² - 5")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.grid(True)
plt.legend()

# Viser grafen på skjermen
plt.show()


