# Copyright 2010 Wim Thys
#
# This file is part of pydof.
#
# pydof is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# pydof is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with pydof.  If not, see <http://www.gnu.org/licenses/>.

class Parser:
	def get_usage(self, username, password):
		pass
	def clear_cache(self):
		pass

class AuthenticationError(Exception):
	def __init__(self, value):
		self.value = value
	def __str__(self):
		return repr(self.value)

WSDL = "https://t4t.services.telenet.be/TelemeterService.wsdl"

from xdg import BaseDirectory as basedir
CACHE = "%s/pydof" % basedir.xdg_cache_home

from beaker.cache import CacheManager
from beaker.util import parse_cache_config_options

cache_opts = {
		'cache.type': 'file',
		'cache.data_dir': '%s/data' % CACHE,
		'cache.lock_dir': '%s/lock' % CACHE
		}

cache = CacheManager(**parse_cache_config_options(cache_opts))

class T4TParser(Parser):
	def __init__(self):
		self.__xml_cache = cache.get_cache("usage_xml", type='file', expire=3600)

	def get_usage(self, username, password):
		from suds.client import Client, SimClient
		soap = Client(WSDL)
		soap.wsdl.services[0].setlocation(".".join(WSDL.split('.')[:-1]))
		try:
			pwd = self.__xml_cache.get("password")
			usr = self.__xml_cache.get("username")
			if not (usr == username and pwd == password):
				raise AuthenticationError()

			src = self.__xml_cache.get("message")
			xml = SimClient(soap.service.retrieveUsage.client, soap.service.retrieveUsage.method).succeeded(soap.service.retrieveUsage.method.binding.input, src)
		except KeyError:
	 		xml = soap.service.retrieveUsage(UserId=username, Password=password)
			self.__xml_cache.set_value("message", str(soap.messages["rx"]))
			self.__xml_cache.set_value("username", username)
			self.__xml_cache.set_value("password", password)

		return xml

	def clear_cache(self):
		self.__xml_cache.clear()
