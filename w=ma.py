print("Weight on planets different planets")
mass = float(input("m: "))

planets = ["Sun", "Mercury", "Venus", "Earth", "Moon", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune", "Pluto"]
gravity = [274.13, 3.59, 8.87, 9.81, 1.62, 3.77, 25.95, 11.08, 10.67, 14.07, 0.42]

dic = {planet:gravity for planet, gravity in zip(planets, gravity)}

for planet in dic:
    print(planet + ": " + str(round(mass * dic[planet])) + "n")
    
    
    
    
