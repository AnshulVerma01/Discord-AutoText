from http.client import HTTPSConnection
from sys import stderr
from json import dumps
from time import sleep

def get_connection():
    return HTTPSConnection("discordapp.com", 443)

def send_message(conn, channel_id, message_data):
    try:
        conn.request(
            "POST", f"/api/v6/channels/{channel_id}/messages", message_data, header_data)
    except:
        stderr.write("Failed to send_message\n")

def msg(variable):
    message_data = {
        "content": variable,
        "tts": "false",
    }
    send_message(get_connection(), config.channel_ID,
                 dumps(message_data))

def program():
    if (config.auth_token == "" or config.channel_ID=="" or config.channel_URL==""):
        print("Enter configurations in the \"config.py\" file.")
        exit()
    try:
        msg_list = []
        time_list = []
        count = 0
        num = int(input("Number of messages to send : "))
        for i in range(0, num):
            message = input("Enter message "+str(i+1)+" : ")
            time = int(
                input("Time (in seconds) to wait after message "+str(i+1)+" : "))
            msg_list.append(message)
            time_list.append(time)
        loop = int(input("Number of times to send message (0 for infinite) : "))
        if (loop == 0):
            while True:
                count = count+1
                print("Loop Number "+str(count))
                sleep(1)
                for j in range(0, num):
                    print("Sending Message "+str(j+1))
                    sleep(1)
                    msg(msg_list[j])
                    sleep(time_list[j])
        elif(loop > 0):
            k = 1
            while k <= loop:
                count = count+1
                print("Loop Number "+str(count))
                sleep(1)
                for j in range(0, num):
                    print("Sending Message "+str(j+1))
                    sleep(1)
                    msg(msg_list[j])
                    sleep(time_list[j])
                k = k+1
    except ValueError:
        print("Enter a valid integer!!")

if __name__ == '__main__':
	print("1. Enter new configurations.\n2. Load configurations.")
	option = int(input("Enter Option : "))
	if(option==1):
		auth = input("Enter auth-token  : ")
		url  = input("Enter channel url : ")
		id   = input("Enter channel ID  : ")
		f = open("config.py", "w")
		f.write("auth_token = \""+auth+"\"\n")
		f.write("channel_URL = \""+url+"\"\n")
		f.write("channel_ID = \""+id+"\"\n")
		f.close()
	elif(option==2):
		b=1
	import config
	header_data = {
    "content-type": "application/json",
    "authorization": config.auth_token,
    "host": "discordapp.com",
    "referer": config.channel_URL
	}
	program()


