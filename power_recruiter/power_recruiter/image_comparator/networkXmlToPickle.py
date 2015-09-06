"""
Power Recruiter - a browser-based FSM-centered database application profiled for IT recruiters
Copyright (C) 2015 Krzysztof Fudali, Andrzej Jackowski, Cezary Kosko, Filip Ochnik

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

from pybrain.tools.xml.networkreader import NetworkReader
import pickle
import sys

# Version for modified Reader which loads data partially
#net = NetworkReader.readFrom(sys.argv[1], None, netwowrk=None)
#net = NetworkReader.readFrom(sys.argv[2], None, network=net)
net = NetworkReader.readFrom(sys.argv[1])
with open(sys.argv[2], 'wb') as f:
    pickle.dump(net, f, pickle.HIGHEST_PROTOCOL)