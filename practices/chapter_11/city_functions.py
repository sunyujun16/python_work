def describe_city(city, country, population=0):
    if population != 0:
        description = city + ' is in ' + country + ', and the population is ' + str(population)
    else:
        description = city+' is in '+country
    return description


