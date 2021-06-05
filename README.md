# Cowin-Notify
SMS and Desktop Notification mechanisms for availability of vaccination slots, also partial automation tool for booking slots

- Scripts
	-	app.py        : For Notification service
	-	automation.py : For autofill the details required to book a vaccination slot (except for OTP , that we need to type manually)

* app.py 
	* Check slots availability for specified pincode for next 2 days(default)
	* Hit CoWin public API every 1 minute(default)

* automation.py
	* Use Selenium to partial automate the slot booking process
	* Open the URL,enters the phone number for OTP once the user enters the OTP it will enter the pincode and select 18+ as age group
	* Based on the availability user need to schedule the appointment manually

* How to run
	* Run requirements.txt to install the dependencies

		` pip install -r requirements.txt `

	* To run the scripts with SMS notification ON, create a [twilio](https://www.twilio.com/referral/BCRLIu) account and add the required credentials in the script
	* Add pincode,age and contact number in the script

* Output
	
	* SMS (if sms parameter set to True)
	![SMS notify](../main/imgs/sms.png)

	* Desktop notification
	![Desktop notify](./main/imgs/desktop.png)
