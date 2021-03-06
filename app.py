import requests
from datetime import datetime,timedelta
import time
import json

#used to create desktop notification, tested in linux OS
import subprocess as s

# importing twilio library
from twilio.rest import Client


def sent_sms(message, receiver_no=[]):

	# Your Account Sid and Auth Token from twilio.com console
	account_sid = '<Account Sid>'
	auth_token = '<Auth Token>'

	client = Client(account_sid, auth_token)

	for number in receiver_no:
		message = client.messages.create(
	                              from_='<twilio no.>',
	                              body = message,
	                              to = number
	                          )
	  
		# print(message.sid)
		print(message.status)


def notify(age,pincodes,actual_dates,notification_interval,sms=False):
	i=0
	while True:
		counter = 0
		i+=1

		for pincode in pincodes:

			for given_date in actual_dates:
				URL = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode={}&date={}".format(pincode, given_date)
				header = {'User-Agent':"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36"}
				print(given_date)
				result = requests.get(URL, headers=header)

				if result.ok:
					response_json = result.json()

					
					if response_json['centers']:
						
						for center in response_json['centers']:
							for session in center['sessions']:
							
								if session['min_age_limit']<=age and session['available_capacity']>0:

									if counter==0:
										try:
											if sms:
												#pass list of twilio verified phone no., eg. send_sms(message,[987654321])
												sent_sms("Vaccination slots available") 		  #sms via twilio	
										except:
											print('Something is wrong with Twilio')

									try:
										s.call(['notify-send','Vaccination','Slot Available']) #Desktop notification 
									except:
										print("Not able to trigger desktop notification")


									if session['vaccine']!='':
										print('\t Vaccine type:',session['vaccine'])
									print('\n')

									counter+=1
									print('Search Completed')
									return 1
								else:
									pass
					else:
						pass
				else:
					print("No Response")


		if counter==0:
			print("No vaccination slot available, ping",i)
		else:
			return 0
			
		#increment the datetime by notification interval
		dt = datetime.now() + timedelta(minutes=notification_interval)

		try:
			#if current date time is greater than 8:00AM, don't consider current date for slots availability 
			if datetime.now().strftime("%d-%m-%Y %H:%M") > actual_dates[0]+' 08:00':
				actual_dates = actual_dates[1:]
				if len(actual_dates)==1:
					return 0

		except:
			return 0

		#wait for notification interval
		while datetime.now()<dt:
			time.sleep(0.1)


if __name__ == "__main__":
	age = 24
	pincodes = [] #eg. [123456]
	num_days = 2 #Current date + next 2 days
	notification_interval = 1 #in minutes


	while True:
		current_dt = datetime.today()
		print("Searching Covid vaccine slots",current_dt.strftime('%d-%m-%Y %H:%M'))

		#eg. current_dt=28-05-2021, actual dates=[28-05-2021,29-05-2021,30-05-2021]
		actual_dates = [(current_dt + timedelta(days=i)).strftime("%d-%m-%Y") for i in range(num_days+1)]
	
		flag =notify(age,pincodes,actual_dates,notification_interval,sms=False)	#set sms=True to sent notify via sms using Twilio api
		
		#once we received the notification, pause the script for 10 minutes
		if flag:
			time.sleep(600)

		print("*"*20)
		time.sleep(1)
