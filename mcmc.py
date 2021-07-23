# imports ====================================================================================================
from pyjoycon import JoyCon, get_R_id, get_L_id
import yaml
import sys
import pyautogui
import time
# load config ====================================================================================================
try:
    config = yaml.safe_load(open('config.yml'))
    print('Loading config.yml...')
    time.sleep(0.5)
    start_cooldown = config['settings']['start_cooldown']
    print(f'- start_cooldown = {start_cooldown}')
    time.sleep(0.5)
    min_accel_left = config['settings']['min_accel_left']
    print(f'- min_accel_left = {min_accel_left}')
    time.sleep(0.5)
    min_accel_right = config['settings']['min_accel_right']
    print(f'- min_accel_right = {min_accel_right}')
    time.sleep(0.5)
    refresh_rate_left = config['settings']['refresh_rate_left']
    print(f'- refresh_rate_left = {refresh_rate_left}')
    time.sleep(0.5)
    refresh_rate_right = config['settings']['refresh_rate_right']
    print(f'- refresh_rate_right = {refresh_rate_right}')
    time.sleep(0.5)
except:
    input('Something went wrong when loading config.yml. Press enter to exit the program.')
    sys.exit()
# start cooldown ====================================================================================================
print('Waiting for cooldown...')
time.sleep(start_cooldown)
# initialize stuff ====================================================================================================
joycon_r = JoyCon(*get_R_id())
joycon_l = JoyCon(*get_L_id())
time_below_min = [0, 0]
# main loop ====================================================================================================
print('Program started.')
while True:
    # getting and storing acceleration
    output_l = joycon_l.get_status()
    output_r = joycon_r.get_status()
    # left mouse button
    if output_l['accel']['x'] >= min_accel_left or output_l['accel']['y'] >= min_accel_left or output_l['accel']['z'] >= min_accel_left:
        pyautogui.mouseDown(button='left')
        time_below_min[0] = 0
    elif time_below_min[0] < refresh_rate_left:
        time_below_min[0] = time_below_min[0] + 1
    else:
        pyautogui.mouseUp(button='left')
    # right mouse button
    if output_r['accel']['x'] >= min_accel_right or output_r['accel']['y'] >= min_accel_right or output_r['accel']['z'] >= min_accel_right:
        pyautogui.mouseDown(button='right')
        time_below_min[1] = 0
    elif time_below_min[1] < refresh_rate_right:
        time_below_min[1] = time_below_min[1] + 1
    else:
        pyautogui.mouseUp(button='right')
    # wait a bit
    time.sleep(0.05)
