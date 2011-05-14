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

import os.path

from xdg import BaseDirectory as basedir

from ConfigParser import SafeConfigParser, NoSectionError, NoOptionError, Error

class Config:
	DEFAULTPATH = os.path.join(basedir.xdg_config_home, "pydof", "pydof.rc")
	def __init__(self):
		defaults = { "verbose": False }
		self.__parser = SafeConfigParser(defaults)
	
	def read(self,filename = None):
		if filename is None:
			self.read(Config.DEFAULTPATH)
		else:
			self.__parser.read(filename)
	
	def write(self,filename = None):
		if filename is None:
			basedir.save_config_path("pydof")
			self.write(Config.DEFAULTPATH)
		else:
			with open(filename, 'w') as configfile:
				self.__parser.write(configfile)

	def username(self, value = None):
		if value is None:
			return self.__parser.get('auth','username')
		else:
			self.__parser.set('auth','username',value)

	def password(self, value = None):
		if value is None:
			return self.__parser.get('auth','password')
		else:
			self.__parser.set('auth','password',value)

	def verbose(self, value = None):
		if value is None:
			return self.__parser.get('config','verbose')
		else:
			self.__parser.set('config','verbose',value)
	
