import os
from time import sleep


PWM_DIR = "/sys/class/pwm"
PWM_CHIP = "pwmchip0"
CHIP_PATH=f"{PWM_DIR}/{PWM_CHIP}"
OVERLAYS = {"pwm-f":1}
OVERLAY="pwm-f"  # CHANGE ME!

PIN_DIR = f"{CHIP_PATH}/pwm{OVERLAYS[OVERLAY]}"


def PWM_echo(fil: str, msg) -> None:
    with open(fil, "w") as f:
        f.write("{msg}\n".format(msg=msg))


def PWM_enable(enabled: bool, pin_dir):
    if enabled:
        PWM_echo(f"{pin_dir}/enable", 1)
    else:
        PWM_echo(f"{pin_dir}/enable", 0)


def PWM_set_duty_cycle_ns(duty_cycle_ns: int, pin_dir):
    # assert pct >= 0
    PWM_echo(f"{pin_dir}/duty_cycle", duty_cycle_ns)


def PWM_motor_pct(pct, pin_dir):
    pct = pct / 2  # btwn -0.5 and +0.5
    pct_as_ns = pct * 1_000_000
    dc_ns = 1_500_000 + pct_as_ns
    PWM_set_duty_cycle_ns(int(dc_ns), pin_dir)

# def PWM_set_duty_cycle_pct(pct: float, pin_dir):
#     # assert pct >= 0 and 1 >= pct
#     duty_cycle_ns = int(pct * period_ns)
#     print(f"{pct = }\n{period_ns = }")
#     PWM_echo(f"{pin_dir}/duty_cycle", duty_cycle_ns)


def PWM_set_period_ns(period_ns: int, pin_dir):
    # assert period_ns > 0
    PWM_echo(f"{pin_dir}/period", period_ns)


###  Main  ###
if not os.path.isdir(f"{PWM_DIR}/{PWM_CHIP}"):
    raise Exception("Please enable an overaly via `ldto enable <overlay_name>` and update OVERLAY accordingly")

PERIOD_MS = 5

if True:
    # PWM_echo(f"{CHIP_PATH}/export", OVERLAYS[OVERLAY])

    PERIOD_NS = PERIOD_MS * 1_000_000
    PWM_enable(False, PIN_DIR)

    PWM_set_period_ns(PERIOD_NS, PIN_DIR)

    PWM_set_duty_cycle_ns(1_500_000, PIN_DIR)
    PWM_motor_pct(-0.2, PIN_DIR)

    PWM_enable(True, PIN_DIR)
    sleep(2)
    PWM_enable(False, PIN_DIR)