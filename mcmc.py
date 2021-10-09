# imports ////////////////////////////////////////////////////////////////////////////////////////////////////
from pyjoycon import JoyCon, get_R_id, get_L_id
import yaml
import sys
import pyautogui
import time
# load config ////////////////////////////////////////////////////////////////////////////////////////////////////
try:
    config = yaml.safe_load(open('config.yml'))
    start_cooldown = config['settings']['start_cooldown']
    min_accel_left = config['settings']['min_accel_left']
    min_accel_right = config['settings']['min_accel_right']
    hold_time_left = config['settings']['hold_time_left']
    hold_time_right = config['settings']['hold_time_right']
except:
    print('Error when loading config: please check "config.yml".')
    input('Press [ENTER] to exit the program.')
    sys.exit();
print('Configuration file loaded.')
# load joycons ////////////////////////////////////////////////////////////////////////////////////////////////////
joycon_r = JoyCon(*get_R_id())
joycon_l = JoyCon(*get_L_id())
print('Connected to joycons.')
# cooldown ////////////////////////////////////////////////////////////////////////////////////////////////////
cooldown = start_cooldown
while cooldown > 0:
    print(f"Starting in {cooldown}...", end = "\r")
    cooldown = cooldown - 1
    time.sleep(1.0)
print('Starting program.', end = "\r")
# load and press loop ////////////////////////////////////////////////////////////////////////////////////////////////////
hold_left = 0
hold_right = 0
def control_loop():
    global hold_left
    global hold_right
    while True:
        # get status of both joycons ---------------------------------------
        output_left = joycon_l.get_status()
        gyro_left_z = abs(output_left['gyro']['z'])
        output_right = joycon_r.get_status()
        gyro_right_z = abs(output_right['gyro']['z'])
        # controls ---------------------------------------
        # left mouse button
        if gyro_left_z >= min_accel_left and hold_left == 0:
            pyautogui.mouseDown(button='left')
            hold_left = hold_time_left
        elif hold_left > 0:
            hold_left -= 1
        else:
            pyautogui.mouseUp(button='left')
        # right mouse button
        if gyro_right_z >= min_accel_right and hold_right == 0:
            pyautogui.mouseDown(button='right')
            hold_right = hold_time_right
        elif hold_right > 0:
            hold_right -= 1
        else:
            pyautogui.mouseUp(button='right')
        # sleep ---------------------------------------
        time.sleep(0.01)

control_loop()
