def country_n_city(country,city,population):
    return(f"{city.title()},{country.title()} - population {population}")

A = country_n_city('china','shanghai',3000)
print(A)