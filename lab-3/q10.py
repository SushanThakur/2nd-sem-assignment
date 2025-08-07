temps_c = [36.5, 37.0, 39.2, 35.6, 38.7]
temps_f = list(map(lambda c: (c * 9/5) + 32, temps_c))
above_100 = list(filter(lambda f: f > 100, temps_f))
print(above_100)
