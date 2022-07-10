#
# sendmail.py
# created by Adam Wu on 7/9/2022
# A simple program that sends email (gmail) with python
# Takes approx. 1 sec send time per person.
#
#------------------------------------------------------------------------------
# imports
import smtplib, ssl
import os
import time # optional, I use it for speed test.
#------------------------------------------------------------------------------
# functions
def read_file(filename):
	""" Reads a file to send as message."""
	message = ""
	with open(filename) as file:
		message += file.read()
	return message

def edit_message(message, editname):
	"""
	replaces '{}' with name. Returns updated message.
	"""
	n_mess = message.replace("{}", editname)
	return n_mess

def people(filename):
	"""
	Reads a file of the receivers. Returns a list of people.
	"""
	with open(filename) as file:
		lst = file.read().splitlines()

	# partitioning each item in list
	new_lst = [p.partition(",") for p in lst]
	return new_lst

def send(user, passw, rec, mess):
	"""simply sends message given its parameters."""
	port = 465 # port for gmail
	context = ssl.create_default_context()

	with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
		server.login(user, passw)
		server.sendmail(user, rec, mess)
#------------------------------------------------------------------------------
# function main()
def main():
	# Your own username and password with gmail.
	# I set my email & password in my env vars.
	user = os.environ.get("Email")
	passw = os.environ.get("password")

	message = read_file("Message.txt")
	rec = people("Receivers.txt")
	
	start = time.time()
	for ppl in rec:
		nmessage = edit_message(message, ppl[0])
		send(user, passw, ppl[2], nmessage)
	end = time.time()
	print(end-start)
#------------------------------------------------------------------------------
# closing conditional that calls main()
if __name__=='__main__':
	main()
#------------------------------------------------------------------------------