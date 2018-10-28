import geocoder
from weather import Weather, Unit

g = geocoder.ip('me')

weather = Weather(Unit.CELSIUS)
lookup = weather.lookup_by_latlng(g.latlng[0], g.latlng[1])
condition = lookup.condition
print(condition.temp)
