import sys
import time
import unicornhat
import unicorntools
import urllib2

import simplejson as json

# unicornhat.rotation(180)

'''
http://freegeoip.net/json/
'''


def adjust_prob(prob):
    return int(round(unicorntools.NUM_ROWS * prob)) - 1

COLOR = (0, 0, 255)

with open('forecast_api_key', 'rb') as fo:
    API_KEY = fo.read().strip()

with open('location.txt', 'rb') as fo:
    location = eval(fo.read().strip())

# location = (0.0, 0.0)
latitude = location[0]
longitude = location[1]

forecast_url = 'https://api.forecast.io/forecast/{}/{},{}'.format(
    API_KEY, latitude, longitude
)

# print forecast_url

forecast_data = urllib2.urlopen(forecast_url)
forecast_data = forecast_data.read()
forecast_data = json.loads(forecast_data)

# print forecast_data['currently']

minutely_data = forecast_data['minutely']['data']
print len(minutely_data)

if len(minutely_data) != 61:
    print 'Not enough data (was {})'.format(len(minutely_data))
    sys.exit()

prob_forecast_data = []

for x in range(unicorntools.NUM_COLS):

    index = int(round((len(minutely_data) / unicorntools.NUM_COLS) * x))
    print x, index
    print minutely_data[index]
    prob_forecast_data.append(minutely_data[index]['precipProbability'])

print prob_forecast_data

adjusted_prob_forecast_data = [
    adjust_prob(prob)
    for prob in prob_forecast_data
]

print adjusted_prob_forecast_data

# sys.exit()

# print forecast_data['hourly']

# prob = forecast_data['currently']['precipProbability']
# print prob
#
# # CHANGE TO BE 1-8 INSTEAD OF 0.0-1.0
# adjusted_prob = int(round(8 * prob))
# print adjusted_prob

print adjusted_prob_forecast_data
# adjusted_prob_forecast_data = [0, 1, 2, 3, 4, 5, 6, 7]
print adjusted_prob_forecast_data

for x in xrange(unicorntools.NUM_COLS):
    print x, adjusted_prob_forecast_data[x]
    forecast_point = adjusted_prob_forecast_data[
        (unicorntools.NUM_COLS - 1) - x
    ]
    print
    # print adjusted_prob_forecast_data[x]

    for y in xrange(adjusted_prob_forecast_data[forecast_point] + 1):

        print x, y

        unicorntools.set_pixel_tuple(
            x,
            y,  # adjusted_prob_forecast_data[forecast_point],
            COLOR
        )

unicornhat.show()

while 1:
    time.sleep(1)
