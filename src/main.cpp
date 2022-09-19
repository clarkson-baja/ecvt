#define Phoenix_No_WPI
#include "ctre/Phoenix.h"
#include "ctre/phoenix/motorcontrol/can/TalonSRX.h"
#include "ctre/phoenix/platform/Platform.h"
#include "ctre/phoenix/unmanaged/Unmanaged.h"
#include "ctre/phoenix/cci/Unmanaged_CCI.h"
#include <iostream>
#include <chrono>
#include <thread>

using namespace ctre::phoenix;
using namespace ctre::phoenix::platform;
using namespace ctre::phoenix::motorcontrol;
using namespace ctre::phoenix::motorcontrol::can;

void sleepApp(int ms) {
	std::this_thread::sleep_for(std::chrono::milliseconds(ms));
}

int main() {
	TalonSRX shifter(1);
	shifter.ConfigFactoryDefault();
	shifter.ConfigOpenloopRamp(5.0);

	while(true) {
		ctre::phoenix::unmanaged::Unmanaged::FeedEnable(100);
		shifter.Set(ControlMode::PercentOutput, 1.00);
		sleepApp(20);
	}
}
