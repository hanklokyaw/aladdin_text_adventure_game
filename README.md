# Aladdin Text Adventure Game

This is a simple text adventure game designed to run on a Raspberry Pi with a 20x4 LCD screen and a numeric keypad.

## Prerequisites

- Raspberry Pi
- 20x4 LCD screen
- Numeric Keypad or Keyboard
- Internet Connection (to download libraries)

## Step 1: Setup I2C on Raspberry Pi

1. **Connect your LCD to your Raspberry Pi:**
   - Connect VCC to Pin 4
   - Connect GND to Pin 6
   - Connect SDA to Pin 3
   - Connect SCL to Pin 5

2. **Enable I2C:**
   - Navigate to Preferences > Raspberry Pi Configuration > Interfaces > I2C > Enable.

3. **Add I2C Modules:**
   - Open the module file: `sudo nano /etc/modules`
   - Add the following lines if they are not present, then press `Ctrl + O` to save, and `Ctrl + X` to exit:
     ```
     i2c-bcm2835
     i2c-bcm2708
     i2c-dev
     ```

## Step 2: Setup Virtual Environment for Libraries

1. **Open a terminal and create a project folder:**
   ```
   sh
   mkdir aladdin
   cd aladdin
   ```

2. **Create and activate a virtual environment:**
   ```
   python3 -m venv my_env
   source my_env/bin/activate
   ```

3. **Install necessary libraries:**
   ```
   sudo apt-get install -y i2c-tools python3-smbus
   pip3 install RPLCD smbus2
   ```

4. **Reboot the Raspberry Pi:**
   ```
   sudo reboot
   ```

## Step 3: Verify LCD Setup

1. **After reboot, activate your virtual environment:**
   ```
   source aladdin/my_env/bin/activate
   ```

2. **Ensure the LCD is connected to the Raspberry Pi and the backlight is on.**

3. **Check if the I2C kernel modules are loaded:**
   ```
   lsmod | grep i2c_
   ```
   - You should see output similar to:
   ```
   i2c_bcm2708  5386  0
   i2c_dev     6047  0
   ```

4. **Detect the I2C address:**
   ```
   sudo i2cdetect -y 1
   ```
   - If successful, you will see a grid with many "-" and "27" in one of the slots.

## Step 4: Copy and Run Aladdin Python File


1. **Download and save the main.py file from this GitHub repository to the aladdin folder.**

2. **Ensure the virtual environment is activated and you are in the aladdin directory.**

3. **Run the application:**
   ```
   python main.py
   ```

4. **By following these steps, you should have the Aladdin Text Adventure Game running on your Raspberry Pi. If you encounter any issues, please refer to the Raspberry Pi documentation or seek help from the community. Enjoy your adventure!**

