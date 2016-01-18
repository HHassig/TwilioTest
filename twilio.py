import os
from twilio.rest import TwilioRestClient
import time

#An array of the various servers a user may be running
serverIP = ["192.168.0.1", "www.google.com", "www.twilio.com", "www.facebook.com", "www.linkedin.com/in/harrisonhassig"]
hostname = "google.com" #example
response = os.system("ping -c 1 " + hostname)

# twilio info
ACCOUNT_SID = "AC4306249f9baa1f78a602cd114a137edb" 
AUTH_TOKEN = "[AuthToken]" 
client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)
def checkRunning(serverIP):
	i = 0
	working = []
	notWorking = []
	while i < len(serverIP):
		response = os.system("ping -c 1 " + serverIP[i])
		if response == 0:
			working += [serverIP[i]]
		else:
			notWorking += [serverIP[i]]
		i += 1
	return working, notWorking
 


while 1 == 1:
	x = checkRunning(serverIP)
	workingString = "Running: " + str(x[0])
	notWorkingString = "Down: " + str(x[1])
	client.messages.create(
		to = myMobile,
		from_ = "+43720116034",
		body = workingString + ". " + notWorkingString + ".",
		)
	#run every hour
	time.sleep(3600)