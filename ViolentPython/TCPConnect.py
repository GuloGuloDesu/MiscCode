import argparse
import socket
from socket import *
from threading import *

thread_lock = Semaphore(value=1)
def connectionScan(target_host, target_port):
	try:
		connection_socket = socket(AF_INET, SOCK_STREAM)
		connection_socket.connect((target_host, target_port))
		connection_socket.send('ViolentPython\r\n')
		connection_results = connection_socket.recv(100)
		thread_lock.acquire()
		print '%d/tcp open' % target_port
		print str(connection_results)
	except:
		thread_lock.acquire()
		print '%d/tcp closed' % target_port
	finally:
		thread_lock.release()
		connection_socket.close()

def portScan(target_host, target_ports):
	try:
		target_ip = gethostbyname(target_host)
	except:
		print 'Cannot resolve \'%s\':  Unknown host' % target_host
		return
	try:
		target_name = gethostbyaddr(target_ip)
		print '\n Scan Results for: ' + target_name[0]
	except:
		print '\n Scan Results for: ' + target_ip
	setdefaulttimeout(1)
	for target_port in target_ports:
		scan_thread = Thread(target=connectionScan, \
			args=(target_host, int(target_port))
		scan_thread.start
		#print 'Scanning port ' + target_port
		#connectionScan(target_host, int(target_port))

def main():
	arg_parser = argparse.ArgumentParser(description='Usage %prog -H' \
		+ '<target host> -p <target port>')
	arg_parser.add_argument('-H', dest='target_host', \
		help='Specify the target host (string)')
	arg_parser.add_argument('-p', dest='target_ports', \
		help='Specify the target port[s] (int)')
	args = arg_parser.parse_args()

	target_host = args.target_host
	target_ports = str(args.target_ports).split(',')

	if (target_host == None) | (target_ports == None):
		print arg_parser.print_help()
		exit(0)
	portScan(target_host, target_ports)

	print "Complete"

if __name__ == '__main__':
	main()
