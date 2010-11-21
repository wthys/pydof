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

version = '0.1a'

from pydof.parsers import T4TParser
from pydof.config import Config

Parser = T4TParser

if __name__ == "__main__":
	t4t = Parser()
	config = Config()
	config.read()
	usage = t4t.get_usage(config.username(), config.password())
