import nmap
import argparse

def nmapScan(target_host, target_port):
	nmap_scan = nmap.PortScanner()
	nmap_scan.scan(target_host, target_port)
	nmap_state = nmap_scan[target_host]['tcp'][int(target_port)]\
		['state']
	print target_host + ' tcp/' + target_port + ' ' + nmap_state
def main():
	arg_parser = argparse.ArgumentParser(description='Usage %prog -H' \
		+ '<target host> -p <target port[s]>')
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

	for target_port in target_ports:
		nmapScan(target_host, target_port)

if __name__ == '__main__':
	main()
