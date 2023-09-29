"""
	# Netpy - Network Python, 2023 by INovomiast2

	Netpy is a module that will help you with your network related projects.
	You can use it to check if you have internet connection, to get your public IP address, etc.

	Netpy has the next functions and classes:

"""

import requests
from colorama import Fore, Back, Style, init


class check:
		@staticmethod
		def connection():
			"""
				This function will check if you have internet connection.
				It will return True if you have internet connection and False if you don't have internet connection.
			"""
			try:
				req = requests.get("https://www.google.com")
				return True
			except:
				return False
		def ip():
			"""
				This function will return your public IP address.
			"""
			try:
				req = requests.get("https://api.ipify.org")
				return req.text
			except:
				return None
		def ip_info():
			"""
				This function will return your public IP address and some other information about your IP address.
			"""
			try:
				req = requests.get("https://ipinfo.io/json")
				return req.json()
			except:
				return None

class server:
    def __init__(self):
        self.server = None

    def start(port):
        """
        This function will start a server on the specified port.
        It will return True if the server has started and False if the server hasn't started.
        """
        try:
            import http.server
            import socketserver
            self.server = socketserver.TCPServer(("", port), http.server.SimpleHTTPRequestHandler)
            self.server.serve_forever()
            return True
        except:
            return False

    def stop(self):
        try:
            self.server.shutdown()
            return True
        except:
            return False

class pyaxios:
	def get(url):
		"""
		Make a GET Request to a desired URL.
  
		Args:
			url (string): The URL you whant to get data from.

		Returns:
			data: The data parsed from the URL.
		"""
		try:
			req = requests.get(url)
			return req.text
		except:
			return print(Fore.RED + "Error: " + Fore.WHITE + "Couldn't get data from the url provided.")
	def post(url, body):
		try:
			req = requests.post(url, body)
			if req.status_code == 200:
				return body
		except:
			return print(Fore.RED + "Error: " + Fore.WHITE + "Couldn't post data to url provided")