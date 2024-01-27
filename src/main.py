import time
import RPi.GPIO as GPIO

def get_max_temperature():
    import glob
    file_list = glob.glob('/sys/class/thermal/thermal_zone*/temp')
    temp_array = []
    for file_path in file_list:
        with open(file_path, 'r') as file:
            temp_raw = file.read().strip()
            temp = float(temp_raw)/1000
            temp_array.append(temp)
    return max(temp_array)


# Configuration
FAN_PIN            = 18     # BCM pin used to drive PWM fan
PWM_FREQ           = 1000   # [Hz] Noctua PWM control
REFRESH_TIME       = 30     # [s] Time to wait between each refresh
DUTY_CYCLE_INITIAL = 50     # [%] Fan speed
DUTY_CYCLE_STEP    = 2      # [%] Fan speed step

GPIO.setwarnings(False)
GPIO.cleanup()
GPIO.setmode(GPIO.BCM)
GPIO.setup(FAN_PIN, GPIO.OUT)

fan = GPIO.PWM(FAN_PIN, PWM_FREQ)
fan.start(0)

target_temperature = 40
duty_cycle = 0
duty_cycle_step = 2

while True:
    current_temperature = get_max_temperature()

    if current_temperature > target_temperature:
        duty_cycle = min(100, duty_cycle + DUTY_CYCLE_STEP)
    else:
        duty_cycle = max(0, duty_cycle - DUTY_CYCLE_STEP)

    fan.ChangeDutyCycle(duty_cycle)
    
    print(f"current_temperature: {current_temperature:.3f} °C")
    print(f"duty_cycle: {duty_cycle:.3f} %")

    time.sleep(REFRESH_TIME)