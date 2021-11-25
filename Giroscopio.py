


'''
        Read Gyro and Accelerometer by Interfacing Raspberry Pi with MPU6050 using Python
	http://www.electronicwings.com
'''
import smbus			#import SMBus module of I2C
from time import sleep          #import
import smtplib
from email.message import EmailMessage
from datetime import datetime
import requests

email_subject = "Email test from Python"
sender_email_address = "andretama1010@gmail.com"
receiver_email_address = "willferosa@gmail.com"
email_smtp = "smtp.gmail.com"
email_password = "Angcolaba9@"


#some MPU6050 Registers and their Address
PWR_MGMT_1   = 0x6B
SMPLRT_DIV   = 0x19
CONFIG       = 0x1A
GYRO_CONFIG  = 0x1B
INT_ENABLE   = 0x38
ACCEL_XOUT_H = 0x3B
ACCEL_YOUT_H = 0x3D
ACCEL_ZOUT_H = 0x3F
GYRO_XOUT_H  = 0x43
GYRO_YOUT_H  = 0x45
GYRO_ZOUT_H  = 0x47


def MPU_Init():
	#write to sample rate register
	bus.write_byte_data(Device_Address, SMPLRT_DIV, 7)

	#Write to power management register
	bus.write_byte_data(Device_Address, PWR_MGMT_1, 1)

	#Write to Configuration register
	bus.write_byte_data(Device_Address, CONFIG, 0)

	#Write to Gyro configuration register
	bus.write_byte_data(Device_Address, GYRO_CONFIG, 24)

	#Write to interrupt enable register
	bus.write_byte_data(Device_Address, INT_ENABLE, 1)

def read_raw_data(addr):
	#Accelero and Gyro value are 16-bit
	high = bus.read_byte_data(Device_Address, addr)
	low = bus.read_byte_data(Device_Address, addr+1)

	#concatenate higher and lower value
	value = ((high << 8) | low)

	#to get signed value from mpu6050
	if(value > 32768):
		value = value - 65536
	return value


bus = smbus.SMBus(1) 	# or bus = smbus.SMBus(0) for older version boards
Device_Address = 0x68   # MPU6050 device address

MPU_Init()

print (" Reading Data of Gyroscope and Accelerometer")

while True:


	## Creacion estructura email##


	# Create an email message object
	message = EmailMessage()

	# Configure email headers
	message['Subject'] = email_subject
	message['From'] = sender_email_address
	message['To'] = receiver_email_address

	# Set email body text
	message.set_content("Alerta de derrumbe")

	# Set smtp server and port
	server = smtplib.SMTP(email_smtp, '587')

	# Identify this client to the SMTP server
	server.ehlo()

	# Secure the SMTP connection
	server.starttls()

	# Login to email account
	server.login(sender_email_address, email_password)


	#Read Accelerometer raw value
	acc_y = read_raw_data(ACCEL_YOUT_H)


	Ay = acc_y/18500.0*100
	now= datetime.now()
	format= now.strftime('Día :%d,Mes: %m')
	print (format)
	print ("\tAy=%.2f " %Ay+"%")
	sleep(1)

	if(Ay<90):
		print("alerta de derrumbe")
		# Send email
		server.send_message(message)

		# Close connection to server
		server.quit()

		sleep(1)

	# envio thikspeack

	enviar2= requests.get("https://api.thingspeak.com/update?api_key=P6EFFTBGBWGB8EGN&field1="+str(now)+"&field2=" +str(Ay))

