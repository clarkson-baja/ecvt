def _echo(fil: str, msg):
    with open(fil, "w") as f:
        f.write("{msg}\n".format(msg=msg))


def enable(enabled, pin_dir):
    if enabled:
        _echo(f"{pin_dir}/enable", 1)
    else:
        _echo(f"{pin_dir}/enable", 0)


def set_duty_cycle_ns(duty_cycle_ns, pin_dir):
    _echo(f"{pin_dir}/duty_cycle", duty_cycle_ns)


def set_period_ns(period_ns, pin_dir):
    _echo(f"{pin_dir}/period", period_ns)


def set_motor_pct(motor_pct: float, pin_dir):
    pct_as_ns = int(motor_pct * 500_000)
    dc_ns = 1_500_000 + pct_as_ns
    set_duty_cycle_ns(dc_ns, pin_dir)


class PWMPin:
    def __init__(self, pin_dir: str, period: int, duty_cycle: int) -> None:
        self.PIN_DIR = pin_dir
        self._period_ns = period
        self._duty_cycle_ns = duty_cycle

    def _echo(self, subfile, msg):
        with open(f"{self.PIN_DIR}/{subfile}", "w") as f:
            f.write("{msg}\n".format(msg=msg))

    def enable(self):
        self._echo("enable", 1)
        return self

    def disable(self):
        self._echo("enable", 0)
        return self

    def set_period(self, nanoseconds: int):
        if not nanoseconds > 0:
            raise ValueError("Period must be greater than 0 nanoseconds")
        self._echo("period", nanoseconds)
        self._period_ns = nanoseconds
        return self

    def period(self) -> int:
        return self._period_ns

    def duty_cycle(self) -> int:
        return self._duty_cycle_ns

    def set_duty_cycle(self, nanoseconds: int):
        if not (nanoseconds >= 0 and nanoseconds <= self._period_ns):
            raise ValueError("Duty Cycle must be between 0 and the period")
        self._echo("duty_cycle", nanoseconds)
        self._duty_cycle_ns = nanoseconds
        return self
