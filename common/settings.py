
#
# Hubblemon - Yet another general purpose system monitor
#
# Copyright 2015 NAVER Corp.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

#
# data path
#

import os, sys, socket


collect_server_port = 40000

# should be sorted by addr
#  add listener if you want
listener_list =[('%s:40001' % socket.gethostname(), 'collect_server/listener_40001')]


#
# setting values
#

chart_resolution = 400


#
# main link settings
# 
# remove or add links you want
#
main_link = [	('system', '/system'),
		('expr', '/expr'),
		('arcus_graph', '/graph?type=arcus_graph'),
		('arcus_stat', '/chart?type=arcus_stat'),
		('arcus_prefix', '/chart?type=arcus_prefix'),
		('arcus_list', '/addon?type=arcus_list'),
		('redis_stat', '/chart?type=redis_stat'),
		('memcached_stat', '/chart?type=memcached_stat'),
		('cubrid_stat', '/chart?type=cubrid_stat'),
		('mysql_stat', '/chart?type=mysql_stat'),
		('jstat_stat', '/chart?type=jstat_stat'),
		('redis_query', '/query?type=redis_query'),
		('memcached_query', '/query?type=memcached_query'),
		('cubrid_query', '/query?type=cubrid_query'),
		('arcus_query', '/query?type=arcus_query'),
		('mysql_query', '/query?type=mysql_query') ]


# for arcus_mon
arcus_zk_addrs = []
'''
# example
arcus_zk_addrs.append('arcuscloud.yourcompany.com:17288')
'''

