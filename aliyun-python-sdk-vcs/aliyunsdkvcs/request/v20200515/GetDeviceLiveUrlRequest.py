# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

from aliyunsdkcore.request import RpcRequest
from aliyunsdkvcs.endpoint import endpoint_data

class GetDeviceLiveUrlRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Vcs', '2020-05-15', 'GetDeviceLiveUrl','vcs')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_OutProtocol(self):
		return self.get_body_params().get('OutProtocol')

	def set_OutProtocol(self,OutProtocol):
		self.add_body_params('OutProtocol', OutProtocol)

	def get_StreamType(self):
		return self.get_body_params().get('StreamType')

	def set_StreamType(self,StreamType):
		self.add_body_params('StreamType', StreamType)

	def get_CorpId(self):
		return self.get_body_params().get('CorpId')

	def set_CorpId(self,CorpId):
		self.add_body_params('CorpId', CorpId)

	def get_GbId(self):
		return self.get_body_params().get('GbId')

	def set_GbId(self,GbId):
		self.add_body_params('GbId', GbId)

	def get_DeviceId(self):
		return self.get_body_params().get('DeviceId')

	def set_DeviceId(self,DeviceId):
		self.add_body_params('DeviceId', DeviceId)