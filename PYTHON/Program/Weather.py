from pyowm import OWM
# from pyowm.utils import config
# from pyowm.utils import timestamps

# ---------- FREE API KEY examples ---------------------

owm = OWM('my_API_key')
mgr = owm.weather_manager()

place = input('Input your City: ')
#
# # Search for current weather in London (Great Britain) and get details
# observation = mgr.weather_at_place(place)
# w = observation.weather

# Search for current weather in London (Great Britain) and get details
observation = mgr.weather_at_place(place)
w = observation.weather
temp = w.temperature('celsius') ['temp']
print('In ' + place + ' now is ' + str(w.detailed_status) + '. Humidity is ' + str(w.humidity) + '. Temperature is ' + str(temp))

if temp < 10:
    print('Now is cold. Put on warm coat')
elif temp < 20:
    print('The weather is cool')
else:
    print('Great weather ))')