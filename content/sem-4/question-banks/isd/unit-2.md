# Unit 2

## 1) What are Sensors? Explain the classification of sensor. Specify two examples of each type of Sensor.

**Sensors** are devices that detect and respond to physical or chemical inputs from the environment and convert them into electrical signals. These signals can be used for measurement, monitoring, or control purposes in various applications. Sensors play a crucial role in modern technology, enabling the development of smart systems and IoT devices.

**Classification of Sensors:**

Sensors can be classified based on several criteria, including the type of input they detect, their working principle, and their application. Here are some common classifications:

1. **Based on the Type of Input:**
   - **Temperature Sensors:** Detect temperature changes. Example: Thermocouples, thermistors.
   - **Pressure Sensors:** Measure pressure changes. Example: Barometers, piezoelectric sensors.
2. **Based on Working Principle:**
   - **Resistive Sensors:** Change resistance in response to stimuli. Example: Light-dependent resistors (LDRs), strain gauges.
   - **Capacitive Sensors:** Change capacitance based on input. Example: Touch sensors, humidity sensors.
3. **Based on Application:**
   - **Biomedical Sensors:** Used in healthcare for monitoring physiological parameters. Example: ECG sensors, blood glucose sensors.
   - **Environmental Sensors:** Used for monitoring environmental conditions. Example: Weather sensors, pollution sensors.

**Examples of Sensors:**

1. **Temperature Sensors:**
   - **Thermocouples:** These sensors generate a voltage proportional to the temperature difference between two junctions.
   - **Thermistors:** These sensors change resistance with changes in temperature.
2. **Pressure Sensors:**
   - **Barometers:** Measure atmospheric pressure to predict weather changes.
   - **Piezoelectric Sensors:** Generate a voltage in response to applied pressure.
3. **Resistive Sensors:**
   - **Light-Dependent Resistors (LDRs):** Change resistance based on the intensity of light.
   - **Strain Gauges:** Change resistance when subjected to mechanical strain.
4. **Capacitive Sensors:**
   - **Touch Sensors:** Detect touch or proximity by changes in capacitance.
   - **Humidity Sensors:** Measure humidity by changes in capacitance due to moisture absorption.
5. **Biomedical Sensors:**
   - **ECG Sensors:** Measure the electrical activity of the heart.
   - **Blood Glucose Sensors:** Monitor blood glucose levels in diabetic patients.
6. **Environmental Sensors:**
   - **Weather Sensors:** Measure temperature, humidity, pressure, and other weather-related parameters.
   - **Pollution Sensors:** Detect and measure pollutants in the air or water.

These examples illustrate the diverse range of sensors and their applications in various fields.

## 2) Define the following specifications of Sensors:

a) Accuracy
b) Resolution
c) Sensitivity
d) Range
e) Repeatability/Precision
f) Bandwidth

a) **Accuracy:** Accuracy refers to how close a sensor's measurement is to the true value of the quantity being measured. It is usually expressed as a percentage of the full-scale range of the sensor. A sensor with high accuracy will have measurements that are very close to the actual value.

b) **Resolution:** Resolution is the smallest change in the quantity being measured that can be detected by the sensor. It is determined by the number of bits in the sensor's output signal. For example, a sensor with 12-bit resolution can detect changes as small as \( \frac{1}{2^{12}} \) of its full-scale range.

c) **Sensitivity:** Sensitivity is a measure of how much the output of a sensor changes in response to a change in the input quantity. It is usually expressed as the ratio of the change in output to the change in input. A sensor with high sensitivity will produce a large change in output for a small change in input.

d) **Range:** Range refers to the minimum and maximum values of the quantity that a sensor can measure. It is important to choose a sensor with a range that includes the expected range of the quantity being measured to ensure accurate measurements.

e) **Repeatability/Precision:** Repeatability, also known as precision, is the ability of a sensor to produce the same output for the same input under the same conditions. It is usually expressed as a percentage of the full-scale range of the sensor. A sensor with high repeatability will produce consistent measurements for repeated tests.

f) **Bandwidth:** Bandwidth is the range of frequencies over which a sensor can accurately measure a quantity. It is usually expressed in hertz (Hz) and is determined by the sensor's response time and filtering characteristics. A sensor with a higher bandwidth can respond to changes in the input quantity more quickly.

## 3) Explain with suitable example each of the following sensors.

a) Mechanical Sensor
b) Pneumatic Sensor
c) Optical Sensor

**a) Mechanical Sensor:**

- **Definition:** Mechanical sensors detect mechanical or physical changes such as position, pressure, or acceleration and convert them into an electrical signal.
- **Example:** A strain gauge is a mechanical sensor that measures the deformation (strain) of an object under applied force. When the object deforms, the resistance of the strain gauge changes, which can be measured as a change in voltage. Strain gauges are used in load cells, pressure sensors, and structural health monitoring systems.

**b) Pneumatic Sensor:**

- **Definition:** Pneumatic sensors detect changes in air pressure or flow and convert them into an electrical signal.
- **Example:** A pneumatic pressure sensor is used to measure the pressure of a gas or air. It consists of a diaphragm that flexes in response to changes in pressure. This movement is then converted into an electrical signal using a mechanism such as a potentiometer or a piezoelectric sensor. Pneumatic pressure sensors are used in pneumatic systems, HVAC systems, and automotive applications.

**c) Optical Sensor:**

- **Definition:** Optical sensors use light to detect changes in various parameters such as distance, presence, or motion and convert them into an electrical signal.
- **Example:** A photoelectric sensor is an optical sensor used to detect the presence or absence of an object. It consists of a light source (such as an LED) and a photodetector (such as a photodiode) placed opposite each other. When the object obstructs the light beam, the photodetector detects a change in light intensity, which is then converted into an electrical signal. Photoelectric sensors are used in automation, robotics, and packaging industries for object detection and counting.

## 4) Explain following Electrical sensors with their working principle & pin details.

a) LM-393 LDR Sensor
b) LM-35 Temperate Sensor
c) DHT-11 Sensor
d) Sound Sensor
e) MQ-2 & MQ5 Gas Sensor

**a) LM393 LDR Sensor:**

- **Working Principle:** The LM393 LDR (Light Dependent Resistor) sensor is a simple light sensor that changes resistance based on the intensity of light falling on it. When light hits the LDR, its resistance decreases, and when there is no light, its resistance is high. The LM393 is a comparator IC often used with the LDR to convert the varying resistance into a digital output.
- **Pin Details:** The LM393 typically has two inputs (non-inverting and inverting), one output, and power supply (Vcc) and ground (GND) pins. The LDR is connected in a voltage divider configuration with a fixed resistor, and the output of the LM393 changes based on the voltage at the LDR.

**b) LM35 Temperature Sensor:**

- **Working Principle:** The LM35 is a precision integrated-circuit temperature sensor that provides an analog output voltage proportional to the temperature in Celsius. It has a linear output characteristic, where each degree Celsius change in temperature corresponds to a 10 mV change in output voltage.
- **Pin Details:** The LM35 typically has three pins: Vcc (power supply), GND (ground), and Vout (analog output). The Vout pin provides an output voltage proportional to the temperature, which can be directly interfaced with an analog-to-digital converter (ADC) for temperature measurement.

**c) DHT11 Sensor:**

- **Working Principle:** The DHT11 is a digital temperature and humidity sensor that uses a capacitive humidity sensor and a thermistor to measure the surrounding air's temperature and humidity. It provides a digital signal output that can be read by a microcontroller.
- **Pin Details:** The DHT11 has four pins: Vcc (power supply), GND (ground), Data (digital output), and NC (not connected). The data pin outputs a serial digital signal containing temperature and humidity information that can be read using a simple protocol.

**d) Sound Sensor:**

- **Working Principle:** A sound sensor detects sound waves and converts them into electrical signals. It typically uses a microphone to capture sound waves and a circuit to amplify and filter the signals. The output is an analog voltage that varies with the sound intensity.
- **Pin Details:** The pin configuration of a sound sensor can vary, but it generally has power supply (Vcc), ground (GND), and output pins. The output pin provides the analog voltage signal proportional to the sound level.

**e) MQ-2 & MQ-5 Gas Sensor:**

- **Working Principle:** MQ-2 and MQ-5 are gas sensors that detect the presence of various gases in the air. They operate on the principle of gas conductivity, where the presence of a specific gas changes the sensor's conductivity. This change is measured as a change in resistance and is used to detect the gas.
- **Pin Details:** Both sensors typically have four pins: Vcc (power supply), GND (ground), Aout (analog output), and Dout (digital output). The analog output provides a voltage proportional to the gas concentration, while the digital output provides a binary signal indicating the presence or absence of gas above a certain threshold.

## 5) What IR Sensors? Explain working principle of Active IR Sensors & PIR Sensors.

**IR Sensors:**
IR (Infrared) sensors are devices that can detect infrared radiation (IR) emitted by objects. They are widely used for various applications such as proximity sensing, object detection, and motion detection. There are two main types of IR sensors: active IR sensors and passive IR sensors.

**Working Principle of Active IR Sensors:**
Active IR sensors consist of an IR transmitter and an IR receiver. The transmitter emits infrared light, which is reflected by an object and detected by the receiver. The presence of the object is determined based on the amount of reflected IR light received by the receiver.

1. **Emitter:** The IR transmitter emits infrared light, usually in the form of pulses. The emitter is typically an IR LED.
2. **Receiver:** The IR receiver detects the infrared light reflected back from objects in front of the sensor. The receiver is usually a photodiode or phototransistor.
3. **Detection:** When an object comes into the sensor's field of view, it reflects some of the emitted IR light back to the sensor. The receiver detects this reflected light, and the sensor processes the signal to determine the presence of the object.
4. **Output:** The sensor provides an output signal based on the detected IR light, which can be used to trigger an action or provide feedback.

Active IR sensors are used in applications such as proximity sensors, object detection sensors in robotics, and touchless switches.

**Working Principle of PIR (Passive Infrared) Sensors:**
PIR sensors detect changes in infrared radiation emitted by or reflected from objects in their field of view. Unlike active IR sensors, PIR sensors do not emit IR light; instead, they detect changes in the IR radiation already present in their surroundings.

1. **Detection Element:** The core component of a PIR sensor is a pyroelectric sensor, which is a crystalline material that generates a voltage when exposed to IR radiation.
2. **Detection Principle:** When an object moves in front of the PIR sensor, it causes a change in the IR radiation pattern detected by the sensor. This change in IR radiation is converted into a voltage signal by the pyroelectric sensor.
3. **Signal Processing:** The voltage signal from the pyroelectric sensor is amplified and processed by the sensor's electronics to detect the presence of a moving object.
4. **Output:** PIR sensors typically provide a digital output signal indicating the presence or absence of motion in their field of view.

PIR sensors are commonly used in motion-activated lighting, security systems, and automatic doors.

## 6) Explain the working principle of Ultrasonic Sensor & pin details of HC-SR-4 Ultrasonic sensor.

**Working Principle of Ultrasonic Sensor:**
Ultrasonic sensors use sound waves with frequencies higher than the audible range (>20 kHz) to measure distances to objects. The sensor emits ultrasonic pulses and measures the time it takes for the pulses to bounce back after hitting an object. This time is used to calculate the distance to the object based on the speed of sound in air.

1. **Transmitter:** The sensor's transmitter emits ultrasonic pulses (typically 40 kHz) toward the target object.
2. **Receiver:** The sensor's receiver detects the ultrasonic pulses after they bounce back from the object.
3. **Time Measurement:** The sensor measures the time taken for the ultrasonic pulses to travel to the object and back. This time is used to calculate the distance using the formula: Distance = (Speed of Sound × Time) / 2.
4. **Output:** The sensor provides an output signal proportional to the measured distance, which can be used for various applications such as object detection, distance measurement, and obstacle avoidance.

**Pin Details of HC-SR04 Ultrasonic Sensor:**
The HC-SR04 is a popular ultrasonic sensor module that is easy to use with microcontrollers like Arduino. It has four pins:

1. **VCC (or VCC):** Connect this pin to the 5V power supply.
2. **Trig (Trigger):** This pin is used to trigger the sensor to send out an ultrasonic pulse. It should be connected to a digital output pin on the microcontroller.
3. **Echo:** This pin is used to receive the ultrasonic echo. It generates a pulse that is proportional to the distance of the object. Connect this pin to a digital input pin on the microcontroller.
4. **GND (or GND):** Connect this pin to the ground (0V) of the power supply.

To use the HC-SR04 sensor, the trigger pin (Trig) needs to be pulsed high for at least 10 microseconds to initiate the ultrasonic pulse. The sensor then sends out an ultrasonic wave and waits for the echo. The Echo pin goes high when the echo is received, and its duration is proportional to the distance of the object. The microcontroller can measure this duration to calculate the distance.

## 7) What are actuators? Explain working principle of DC motors.

**Actuators** are devices that convert energy (typically electrical, hydraulic, or pneumatic) into mechanical motion to perform a specific action. They are essential components in systems where controlled motion is required, such as in robotics, industrial automation, and automotive systems. Actuators can be classified based on the type of energy they use and the mechanism they employ to produce motion.

**Working Principle of DC Motors:**
DC (Direct Current) motors are a type of electromechanical actuators that convert electrical energy into mechanical motion. They operate based on the principle of Lorentz force, where a current-carrying conductor placed in a magnetic field experiences a force perpendicular to both the current direction and the magnetic field lines. This force causes the motor to rotate.

1. **Construction:** A DC motor consists of a stator (stationary part) and a rotor (rotating part). The stator contains the field windings, which produce the magnetic field, while the rotor contains the armature windings, which carry the current.
2. **Commutation:** DC motors require a mechanism called commutation to continuously change the direction of current in the armature windings, ensuring continuous rotation. This is typically achieved using a commutator and brushes arrangement.
3. **Working:**
   - When a voltage is applied to the motor, current flows through the armature windings, creating a magnetic field.
   - The magnetic field interacts with the magnetic field produced by the stator, causing a torque that rotates the rotor.
   - As the rotor rotates, the commutator switches the direction of current in the armature windings to maintain rotation.
4. **Speed Control:** The speed of a DC motor can be controlled by varying the voltage applied to it. Lower voltages result in lower speeds, while higher voltages result in higher speeds.

DC motors are widely used in various applications due to their simplicity, reliability, and ease of control. They are used in appliances, automobiles, robotics, and industrial machinery, among other applications.

## 8) Write a short note on Brushlees DC motor & Stepper motor.

**Brushless DC Motor (BLDC):**
Brushless DC motors are similar to traditional DC motors but do not use brushes for commutation. Instead, they use an electronic controller to switch the stator windings, making them more efficient, reliable, and durable than brushed motors. The working principle of a BLDC motor involves the use of a permanent magnet rotor and a stator with windings. The electronic controller determines the current direction in the stator windings based on the rotor position, ensuring smooth and efficient operation. BLDC motors are commonly used in applications requiring high efficiency and precise speed control, such as in electric vehicles, drones, and industrial automation.

**Stepper Motor:**
Stepper motors are electromechanical devices that convert electrical pulses into discrete mechanical movements. Unlike DC motors, which rotate continuously, stepper motors move in precise increments called steps. Stepper motors consist of a rotor with permanent magnets and a stator with coils. The stator windings are energized in a sequence to generate a magnetic field that pulls the rotor to the next step. Stepper motors are widely used in applications that require precise positioning, such as 3D printers, CNC machines, and robotics. They offer excellent control over position and speed but may require a specialized driver to operate.

## 9) Explain PWM method to control speed of a motor.

**Brushless DC Motor (BLDC):**
A brushless DC motor is a type of synchronous motor that uses a digital drive system to control its speed and direction. Unlike brushed motors, which use brushes and a commutator for rotor energization, BLDC motors use electronic commutation for more precise control and higher efficiency. They are widely used in various applications, including computer disk drives, electric vehicles, and industrial machinery.

**Stepper Motor:**
A stepper motor is a brushless, synchronous electric motor that converts digital pulses into mechanical shaft rotation. Each pulse moves the shaft in discrete steps, making stepper motors ideal for applications requiring precise positioning or speed control. They are commonly used in 3D printers, CNC machines, and robotic systems.

**PWM (Pulse Width Modulation) for Motor Speed Control:**
PWM is a method used to control the speed of DC motors by varying the average voltage applied to the motor. It works by rapidly switching the power supplied to the motor on and off at a fixed frequency. The width of the on-time (duty cycle) determines the average voltage applied to the motor and, consequently, the speed of the motor.

**Working Principle:**

1. **Generation of PWM Signal:** A microcontroller or PWM generator generates a PWM signal with a fixed frequency (e.g., 500 Hz to 20 kHz) and a variable duty cycle (0% to 100%).
2. **Control of Motor Speed:** The PWM signal is applied to a motor driver, which regulates the power supplied to the motor based on the duty cycle of the PWM signal. A higher duty cycle corresponds to a higher average voltage and faster motor speed, while a lower duty cycle results in a lower speed.
3. **Smooth Speed Control:** PWM provides smooth speed control without the need for complex circuitry or components. By adjusting the duty cycle, the motor speed can be precisely controlled over a wide range.
4. **Advantages of PWM:** PWM is an efficient method for controlling motor speed as it reduces power losses and heat generation compared to other speed control methods. It is also simple to implement and provides precise speed control.

Overall, PWM is a widely used method for controlling the speed of DC motors in various applications due to its simplicity, efficiency, and effectiveness.

## 10) Explain the pin details of Liquid Crystal Display and Seven Segment LED Display.

**Pin Details of a Liquid Crystal Display (LCD):**

1. **VSS (Ground):** Connect to ground (0V) of the power supply.
2. **VDD (Power Supply):** Connect to a +5V power supply.
3. **VO (Contrast Adjustment):** Connect to a potentiometer to adjust the contrast of the display.
4. **RS (Register Select):** Selects between data (RS=1) and command (RS=0) modes.
5. **RW (Read/Write):** Selects between read (RW=1) and write (RW=0) modes. Usually connected to ground for write-only operation.
6. **E (Enable):** Enables writing data or commands to the LCD when transitioning from high to low.
7. **D0-D7 (Data Lines):** Eight bidirectional data lines for transferring data and commands between the LCD and the microcontroller.
8. **A (LED Anode):** Anode of the LED backlight, connected to a current-limiting resistor and a +5V supply.
9. **K (LED Cathode):** Cathode of the LED backlight, connected to ground.

**Pin Details of a Seven Segment LED Display:**

1. **Common Anode (CA) or Common Cathode (CC):** Seven individual LEDs are arranged in a pattern to form a numeric digit. Each LED segment can be a common anode (CA) or common cathode (CC) type.
2. **Segment LEDs (a-g):** Seven LEDs labeled a to g form the segments of the display. Each segment is connected to a pin.
3. **Decimal Point (DP):** An eighth LED segment that can be used to display a decimal point.
4. **Forward Voltage (VF):** Typical forward voltage for each LED segment, usually around 2V.
5. **Forward Current (IF):** Typical forward current for each LED segment, usually around 20mA.
6. **Maximum Ratings:** Maximum ratings for forward voltage and forward current to avoid damaging the LEDs.
7. **Common Pin (CA or CC):** The common pin for the common anode or common cathode configuration. This pin is connected to a voltage source (CA) or ground (CC) to light up the corresponding segments.

## 11) Specify the hardware connection of LCD display with Arduino Uno baord.

To connect an LCD display to an Arduino Uno board, you will need to use the following connections:

1. **LCD Pin - Arduino Pin:**
   - RS (Register Select) - Digital Pin 12
   - EN (Enable) - Digital Pin 11
   - D4 - Digital Pin 5
   - D5 - Digital Pin 4
   - D6 - Digital Pin 3
   - D7 - Digital Pin 2
   - VSS (Ground) - Ground (GND)
   - VDD (Power Supply) - 5V
   - VO (Contrast Adjustment) - Connect to a potentiometer to adjust contrast
   - A (LED Anode) - 5V through a current-limiting resistor (220 ohms)
   - K (LED Cathode) - Ground (GND)

Here is a basic wiring diagram for connecting an LCD display to an Arduino Uno:

```
   LCD        Arduino Uno
   -----------------------
   RS         Digital Pin 12
   EN         Digital Pin 11
   D4         Digital Pin 5
   D5         Digital Pin 4
   D6         Digital Pin 3
   D7         Digital Pin 2
   VSS        GND
   VDD        5V
   VO         Potentiometer for contrast adjustment
   A          5V through a 220 ohm resistor
   K          GND

```

Additionally, make sure to include the necessary libraries in your Arduino sketch for interfacing with the LCD display. You can use the LiquidCrystal library for this purpose.

## 12) Write a C++ code for the followings:

(a) Measure room temperature using an LM35 temperature sensor and display it on serial monitor.
(b) Detect the presence of an object and trigger an LED using a PIR sensor.
(c) Detect the level of soil moisture and trigger the RGB LED for “dry”, “wet” and “no action” status.
(d) Measure the distance of an object using an Ultrasonic sensor and display it on serial monitor.
(e) Detect a specific gas using an MQ gas sensor and trigger an alarm when detected.

Here's a sample C++ code for each of the tasks:

**(a) Measure room temperature using an LM35 temperature sensor and display it on the serial monitor:**

```cpp
#include <Arduino.h>

const int lm35Pin = A0; // LM35 sensor connected to analog pin A0

void setup() {
  Serial.begin(9600); // Initialize serial communication
}

void loop() {
  int sensorValue = analogRead(lm35Pin); // Read the sensor value
  float temperature = (sensorValue * 5.0 / 1024) * 100; // Convert the sensor value to temperature in degrees Celsius

  Serial.print("Temperature: ");
  Serial.print(temperature);
  Serial.println(" °C");

  delay(1000); // Delay for 1 second
}

```

**(b) Detect the presence of an object and trigger an LED using a PIR sensor:**

```cpp
#include <Arduino.h>

const int pirPin = 2; // PIR sensor connected to digital pin 2
const int ledPin = 13; // LED connected to digital pin 13

void setup() {
  pinMode(pirPin, INPUT); // Set PIR sensor pin as input
  pinMode(ledPin, OUTPUT); // Set LED pin as output
  Serial.begin(9600); // Initialize serial communication
}

void loop() {
  int pirState = digitalRead(pirPin); // Read the PIR sensor state

  if (pirState == HIGH) {
    Serial.println("Motion detected!");
    digitalWrite(ledPin, HIGH); // Turn on the LED
  } else {
    digitalWrite(ledPin, LOW); // Turn off the LED
  }

  delay(500); // Delay for 0.5 second
}

```

**(c) Detect the level of soil moisture and trigger the RGB LED for “dry”, “wet” and “no action” status:**

```cpp
#include <Arduino.h>

const int soilMoisturePin = A0; // Soil moisture sensor connected to analog pin A0
const int redPin = 9; // Red LED pin connected to digital pin 9
const int greenPin = 10; // Green LED pin connected to digital pin 10
const int bluePin = 11; // Blue LED pin connected to digital pin 11

void setup() {
  pinMode(soilMoisturePin, INPUT); // Set soil moisture sensor pin as input
  pinMode(redPin, OUTPUT); // Set red LED pin as output
  pinMode(greenPin, OUTPUT); // Set green LED pin as output
  pinMode(bluePin, OUTPUT); // Set blue LED pin as output
  Serial.begin(9600); // Initialize serial communication
}

void loop() {
  int soilMoistureValue = analogRead(soilMoisturePin); // Read the soil moisture sensor value

  Serial.print("Soil Moisture: ");
  Serial.println(soilMoistureValue);

  if (soilMoistureValue < 300) {
    // Dry soil condition
    digitalWrite(redPin, HIGH);
    digitalWrite(greenPin, LOW);
    digitalWrite(bluePin, LOW);
  } else if (soilMoistureValue >= 300 && soilMoistureValue < 700) {
    // Wet soil condition
    digitalWrite(redPin, LOW);
    digitalWrite(greenPin, HIGH);
    digitalWrite(bluePin, LOW);
  } else {
    // No action required
    digitalWrite(redPin, LOW);
    digitalWrite(greenPin, LOW);
    digitalWrite(bluePin, HIGH);
  }

  delay(1000); // Delay for 1 second
}

```

**(d) Measure the distance of an object using an Ultrasonic sensor and display it on the serial monitor:**

```cpp
#include <Arduino.h>

const int trigPin = 2; // Ultrasonic sensor trigger pin connected to digital pin 2
const int echoPin = 3; // Ultrasonic sensor echo pin connected to digital pin 3

void setup() {
  pinMode(trigPin, OUTPUT); // Set trigger pin as output
  pinMode(echoPin, INPUT); // Set echo pin as input
  Serial.begin(9600); // Initialize serial communication
}

void loop() {
  digitalWrite(trigPin, LOW); // Set trigger pin to low
  delayMicroseconds(2); // Delay for 2 microseconds
  digitalWrite(trigPin, HIGH); // Set trigger pin to high
  delayMicroseconds(10); // Delay for 10 microseconds
  digitalWrite(trigPin, LOW); // Set trigger pin to low

  long duration = pulseIn(echoPin, HIGH); // Read the echo pin and calculate the duration of the pulse
  int distance = duration * 0.034 / 2; // Calculate the distance in centimeters

  Serial.print("Distance: ");
  Serial.print(distance);
  Serial.println(" cm");

  delay(1000); // Delay for 1 second
}

```

**(e) Detect a specific gas using an MQ gas sensor and trigger an alarm when detected:**

```cpp
#include <Arduino.h>

const int mqPin = A0; // MQ gas sensor analog pin connected to analog pin A0
const int alarmPin = 12; // Alarm pin connected to digital pin 12

void setup() {
  pinMode(mqPin, INPUT); // Set MQ gas sensor pin as input
  pinMode(alarmPin, OUTPUT); // Set alarm pin as output
  Serial.begin(9600); // Initialize serial communication
}

void loop() {
  int gasValue = analogRead(mqPin); // Read the MQ gas sensor value

  Serial.print("Gas Value: ");
  Serial.println(gasValue);

  if (gasValue > 500) {
    // Gas detected, trigger alarm
    digitalWrite(alarmPin, HIGH);
    Serial.println("Gas detected!");
  } else {
    // No gas detected, turn off alarm
    digitalWrite(alarmPin, LOW);
    Serial.println("No gas detected");
  }

  delay(1000); // Delay for 1 second
}

```

Please note that these codes are examples and may need to be adjusted based on the specific sensors and components you are using. Also, ensure that the sensors and LEDs are connected correctly to your Arduino board.
