# -*- coding: utf8 -*-
# Copyright (c) 2017-2018 THL A29 Limited, a Tencent company. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import json

from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.common.abstract_client import AbstractClient
from tencentcloud.tbp.v20190311 import models


class TbpClient(AbstractClient):
    _apiVersion = '2019-03-11'
    _endpoint = 'tbp.tencentcloudapi.com'


    def Reset(self, request):
        """对当前机器人的会话状态进行复位

        :param request: 调用Reset所需参数的结构体。
        :type request: :class:`tencentcloud.tbp.v20190311.models.ResetRequest`
        :rtype: :class:`tencentcloud.tbp.v20190311.models.ResetResponse`

        """
        try:
            params = request._serialize()
            body = self.call("Reset", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ResetResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def TextProcess(self, request):
        """接收调用侧的文本输入，返回应答文本。

        :param request: 调用TextProcess所需参数的结构体。
        :type request: :class:`tencentcloud.tbp.v20190311.models.TextProcessRequest`
        :rtype: :class:`tencentcloud.tbp.v20190311.models.TextProcessResponse`

        """
        try:
            params = request._serialize()
            body = self.call("TextProcess", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.TextProcessResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def TextReset(self, request):
        """会话重置接口

        :param request: 调用TextReset所需参数的结构体。
        :type request: :class:`tencentcloud.tbp.v20190311.models.TextResetRequest`
        :rtype: :class:`tencentcloud.tbp.v20190311.models.TextResetResponse`

        """
        try:
            params = request._serialize()
            body = self.call("TextReset", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.TextResetResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)