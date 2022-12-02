from geopy.geocoders import Nominatim
app = Nominatim(user_agent='test')
location = app.geocode("Хаджиева 53,Грозный, Россия").raw
# print raw data
print(location)