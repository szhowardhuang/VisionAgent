import os
from typing import List, Optional, Tuple, Union

import requests

from lagent.schema import ActionReturn, ActionStatusCode
from .base_action import BaseAction

DEFAULT_DESCRIPTION = """一个进行图片识别的API。
当你需要对于一个图片进行识别时，可以使用这个API。
优先使用ImageRecognition来进行图片识别。
输入应该是一张图片文件的路径，或者是图片的URL。
"""


class ImageRecognition(BaseAction):

    def __init__(self,
                 description: str = DEFAULT_DESCRIPTION,) -> None:
        super().__init__(description)


    def __call__(self, query: str) -> ActionReturn:
        """Return the image recognition response.

        Args:
            query (str): The query include the image content path.

        Returns:recognition
            ActionReturn: The action return.
        """

        tool_return = ActionReturn(url=None, args=None)
        try:
            response = self._image_recognition(query)
            print("Enter Image Recognition entry")
            tool_return.result = dict(text=str(response))
            tool_return.state = ActionStatusCode.SUCCESS
        except Exception as e:
            tool_return.result = dict(text=str(e))
            tool_return.state = ActionStatusCode.API_ERROR
        return tool_return

    def _image_recognition(self,
                query: str) -> str:
        return 'image recognition response here is a apple'
