from map import Map

class Weather:

    def __init__(self, temp, precipitation):
        self.temp = temp
        self.precipitation = precipitation

    # when adding __eq__ you can't use it in a dictionary without adding __hash__
    def __eq__(self, other):
        return (self.temp == other.temp and
                self.precipitation == other.precipitation)

    def __hash__(self):
        # please don't do this
        # return 0

        # use something that is immutable, or it won't work
        return self.temp

map = Map()

map["Eric"] = 'A'
map['Jeb'] = 'B'

for value in range(10):
    map[value] = value

print(map['Eric'])
print(map['Jeb'])

map['Jeb'] = 'A'

print(map['Eric'])
print(map['Jeb'])


today = Weather(40, "rainy")
another = Weather(40, "rainy")

weather_feelings = { today : "gross" }

print(weather_feelings[today])
today.temp = 50
print(weather_feelings[today])

temps = [ 40, 45, 50]

# weather_feelings[temps] = "cold"

print(hash(today))
print(hash(another))

third = today
print(hash(third))

print(today.temp)
print(third.temp)

today.temp = 50

print(today.temp)
print(third.temp)