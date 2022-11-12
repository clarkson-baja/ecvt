###### ----  Change These  ---- ######
OVERLAY = "pwm-f"
PWM_PERIOD_MS = 5
PWM_CHIP_PATH = "/sys/class/pwm/pwmchip0"


###### ----  Main Code  ---- ######
import os
import syspwm as pwm
from time import sleep

OVERLAYS = {"pwm-f": 1, "pwm-a": 0}

PIN_DIR = f"{PWM_CHIP_PATH}/pwm{OVERLAYS[OVERLAY]}"


def calc_dc(motor_pct: float) -> int:
    pct_as_ns = int(motor_pct * 500_000)
    return int(1_500_000 + pct_as_ns)


if __name__ == "__main__":

    PERIOD_NS = PWM_PERIOD_MS * 1_000_000

    talon = pwm.PWMPin(PIN_DIR, PERIOD_NS, 0).disable()

    talon.set_duty_cycle(calc_dc(0.2))
    talon.enable()
    sleep(2)
    talon.disable()
