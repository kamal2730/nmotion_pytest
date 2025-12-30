# NMotion Actuator Python API Reference

This document provides a categorized list of all available methods for the `Actuator` class in the `nmotion_transport` Python library.

> **Note:**
> * **Setters:** Generally return a status code (0 = `RETURN_OK`).
> * **Getters:** Generally return a tuple: `(status_code, value)`.
> * **Usage:** `actuator_object.methodName(arguments)`

---

## 1. Motion Control
Methods to move the actuator using different control strategies.

* **`setPositionControl`** - Move to a specific angle.
* **`setPositionControlWithFeedForward`** - Position control with feed-forward terms for better dynamic response.
* **`setVelocityControl`** - Spin at a continuous speed.
* **`setVelocityControlWithFeedForward`** - Velocity control with feed-forward terms.
* **`setVelocityRampControl`** - Velocity control with smooth ramping (acceleration/deceleration).
* **`setTorqueControl`** - Apply a specific torque/force (useful for gripping or tensioning).
* **`setTrapezoidalTrajectoryControl`** - Move with a trapezoidal velocity profile (constant acceleration -> constant velocity -> constant deceleration).
* **`setScurveTrajectoryControl`** - Move with an S-curve profile (smoother jerk-limited motion).
* **`emergencyStop`** - Immediately stop the motor.

---

## 2. Sensor & State Feedback (Getters)
Methods to read real-time data from the actuator.

### Motion Data
* **`getMotorPosition`** / **`getOutputPosition`** - Current angle.
* **`getMotorVelocity`** / **`getOutputVelocity`** - Current speed.
* **`getMotorAcceleration`** / **`getOutputAcceleration`** - Current acceleration.
* **`getMotorTorque`** / **`getOutputTorque`** - Current torque load.
* **`getTrajectoryDoneStatus`** - Check if a trajectory move has finished.
* **`getZeroPosition`** - Get the offset value used for the zero position.

### Electrical & Thermal Data
* **`getBusVoltage`** - Input voltage level.
* **`getBusCurrent`** - Total current consumption.
* **`getMotorPhaseCurrents`** - Currents in the motor phases (U, V, W).
* **`getIdqCurrents`** - Field-oriented control currents ($I_d$, $I_q$).
* **`getMotorTemperature`** - Temperature of the motor windings.
* **`getDriverTemperature`** - Temperature of the motor driver electronics.

### Raw Sensor Data
* **`getMotorEncoderRawData`** - Raw counts from the motor-side encoder.
* **`getOutputEncoderRawData`** - Raw counts from the output-side encoder.
* **`getMotorEncoderState`** / **`getOutputEncoderState`** - Status of the encoders.

---

## 3. Configuration & Tuning
Methods to configure PID gains, filters, and limits.

### Tuning (PID & Bandwidth)
* **`setPositionControllerGain`** - Set P, I, D gains for position loop.
* **`setVelocityControllerGains`** - Set P, I, D gains for velocity loop.
* **`getCurrentControllerGains`** - Set gains for the current (torque) loop.
* **`getPositionControllerGain`** (Getter)
* **`getVelocityControllerGains`** (Getter)
* **`getCurrentControllerBandwidth`** / **`setCurrentControllerBandwidth`**
* **`getMotorEncoderBandwidth`** / **`setMotorEncoderBandwidth`**
* **`getEncoderDataFilter`** / **`setEncoderDataFilter`**
* **`getCurrentFilter`** / **`setCurrentFilter`**

### Safety & Limits
* **`setDCBusTripLevels`** / **`getDCBusTripLevels`** - Set over/under voltage protection limits.
* **`setRegenCurrentTripLevel`** / **`getRegenCurrentTripLevel`** - Limit current generated during braking.
* **`enableMotorThermalLimit`** / **`disableMotorThermalLimit`** - Toggle overheat protection.

---

## 4. Device Management
Methods for setup, calibration, and system status.

### State Management
* **`setDeviceToActive`** - Enable the motor driver (engage).
* **`setDeviceToIdle`** - Disable the motor driver (coast/relax).
* **`getControllerMode`** - Check current operation mode.
* **`getControllerState`** - Check internal controller state.
* **`getMotorState`** - Detailed motor status.

### Diagnostics & Errors
* **`isConnected`** - Check if the device is reachable.
* **`getErrorCode`** - Read general error flags.
* **`getDebugErrorCode`** - Read detailed debug errors.
* **`getDriverFault`** - Check for hardware driver faults.
* **`getCANCommunicationStatus`** - Check CAN bus health.
* **`clearActuatorErrors`** - Reset error states to resume operation.

### Identification & Firmware
* **`id`** - Internal object ID.
* **`getNodeId`** - Get the current CAN ID.
* **`setNodeId`** - Change the CAN ID (Caution: requires reboot/save).
* **`getFirmwareVersion`**
* **`getFirmwareCommit`**
* **`getHardwareVersion`**
* **`getMotorPhaseParameters`** - Read resistance/inductance of motor.
* **`getMotorThermistorConfiguration`**

### Maintenance
* **`flash`** - Flash new firmware (LEDs might blink).
* **`rebootActuator`** - Restart the device.
* **`runCalibrationSequence`** - Auto-tune/calibrate the motor.
* **`saveConfigurations`** - Save current settings to permanent memory (EEPROM).
* **`eraseConfigurations`** - Wipe settings.
* **`setCurrentPostionToZero`** - Zero the encoder at the current location.
* **`getDCCalibPhaseCurrents`** - Calibration data for current sensing.