# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

from aliyunsdkcore.request import RpcRequest
class CreateResourcePoolRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Emr', '2016-04-08', 'CreateResourcePool')

	def get_Note(self):
		return self.get_query_params().get('Note')

	def set_Note(self,Note):
		self.add_query_param('Note',Note)

	def get_ResourceOwnerId(self):
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self,ResourceOwnerId):
		self.add_query_param('ResourceOwnerId',ResourceOwnerId)

	def get_Name(self):
		return self.get_query_params().get('Name')

	def set_Name(self,Name):
		self.add_query_param('Name',Name)

	def get_Active(self):
		return self.get_query_params().get('Active')

	def set_Active(self,Active):
		self.add_query_param('Active',Active)

	def get_ClusterId(self):
		return self.get_query_params().get('ClusterId')

	def set_ClusterId(self,ClusterId):
		self.add_query_param('ClusterId',ClusterId)

	def get_YarnSiteConfig(self):
		return self.get_query_params().get('YarnSiteConfig')

	def set_YarnSiteConfig(self,YarnSiteConfig):
		self.add_query_param('YarnSiteConfig',YarnSiteConfig)

	def get_Configs(self):
		return self.get_query_params().get('Configs')

	def set_Configs(self,Configs):
		for i in range(len(Configs)):	
			if Configs[i].get('ConfigKey') is not None:
				self.add_query_param('Config.' + str(i + 1) + '.ConfigKey' , Configs[i].get('ConfigKey'))
			if Configs[i].get('ConfigValue') is not None:
				self.add_query_param('Config.' + str(i + 1) + '.ConfigValue' , Configs[i].get('ConfigValue'))
			if Configs[i].get('configType') is not None:
				self.add_query_param('Config.' + str(i + 1) + '.configType' , Configs[i].get('configType'))
			if Configs[i].get('TargetId') is not None:
				self.add_query_param('Config.' + str(i + 1) + '.TargetId' , Configs[i].get('TargetId'))
			if Configs[i].get('Category') is not None:
				self.add_query_param('Config.' + str(i + 1) + '.Category' , Configs[i].get('Category'))
			if Configs[i].get('Note') is not None:
				self.add_query_param('Config.' + str(i + 1) + '.Note' , Configs[i].get('Note'))


	def get_PoolType(self):
		return self.get_query_params().get('PoolType')

	def set_PoolType(self,PoolType):
		self.add_query_param('PoolType',PoolType)