"""
All constants and variables that are needed for calculations and server operation have been moved in this module.
"""
import configparser

# variables that are needed for the server to work, including the IP of the server,
# the port of the server and the delay time between server responses
config = configparser.ConfigParser()
config.read('config.ini')
time_sleap = int(config['SERVER']['time_sleap'])
ip = config['SERVER']['ip']
port = int(config['SERVER']['port'])

# all constants for calculating the coordinates of the moon
angle_slope = 102888.0  # seconds
period_for_on_cycle = 27.3 * 24 * 3600  # seconds
perimeter = 360 * 3600  # seconds
ra_dec_min = '6:45:48.54'
ra_dec_max = '18:45:48.54'
start_date = '2021/6/15 23:59:59'
