import os
from typing import List, Optional, Tuple, Union

import requests

from lagent.schema import ActionReturn, ActionStatusCode
from .base_action import BaseAction

DEFAULT_DESCRIPTION = """一个进行图片识别的API。
当你需要对于一个特定问题找到简短明了的回答时，可以使用它。Recognition
输入应该是一张图片。
"""


class ImageRecognition(BaseAction):

    def __init__(self,) -> None:
        super().__init__()


    def __call__(self, query: str) -> ActionReturn:
        """Return the search response.

        Args:
            query (str): The search content.

        Returns:recognition
            ActionReturn: The action return.
        """

        tool_return = ActionReturn(url=None, args=None, type=self.name)
        tool_return.result = dict(text=str('need implement'))
        tool_return.state = ActionStatusCode.SUCCESS
        print("Enter Image Recognition entry")
        return tool_return


