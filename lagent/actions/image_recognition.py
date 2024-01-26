import os
from typing import List, Optional, Tuple, Union

import requests
import json

from lagent.schema import ActionReturn, ActionStatusCode
from .base_action import BaseAction

#mmdetection
from mmdet.apis import DetInferencer

#initial model
inferencer_mmdet = DetInferencer(model='rtmdet_tiny_8xb32-300e_coco')

# COCO dataset class
classes_cocodataset = ('person', 'bicycle', 'car', 'motorcycle', 'airplane', 
           'bus', 'train', 'truck', 'boat', 'traffic light', 'fire hydrant',
           'stop sign', 'parking meter', 'bench', 'bird', 'cat', 'dog',
           'horse', 'sheep', 'cow', 'elephant', 'bear', 'zebra',
           'giraffe', 'backpack', 'umbrella', 'handbag', 'tie',
           'suitcase', 'frisbee', 'skis', 'snowboard', 'sports ball',
           'kite', 'baseball bat', 'baseball glove', 'skateboard',
           'surfboard', 'tennis racket', 'bottle', 'wine glass', 'cup',
           'fork', 'knife', 'spoon', 'bowl', 'banana', 'apple',
           'sandwich', 'orange', 'broccoli', 'carrot', 'hot dog', 'pizza',
           'donut', 'cake', 'chair', 'couch', 'potted plant', 'bed',
           'dining table', 'toilet', 'tv', 'laptop', 'mouse', 'remote',
           'keyboard', 'cell phone', 'microwave', 'oven', 'toaster',
           'sink', 'refrigerator', 'book', 'clock', 'vase', 'scissors',
           'teddy bear', 'hair drier', 'toothbrush')


DEFAULT_DESCRIPTION = """一个进行图片识别的API。
当你需要对于一个图片进行识别时，可以使用这个API。
优先使用ImageRecognition来进行图片识别。
输入应该是一张图片文件的路径，或者是图片的URL。
"""


class ImageRecognition(BaseAction):

    def __init__(self,
                 description: str = DEFAULT_DESCRIPTION,
                 name: Optional[str] = None,
                 enable: bool = True,
                 disable_description: Optional[str] = None) -> None:
        super().__init__(description)


    def __call__(self, query: str) -> ActionReturn:
        """Return the image recognition response.

        Args:
            query (str): The query include the image content path.

        Returns:recognition
            ActionReturn: The action return.
        """

        tool_return = ActionReturn(url=None, args=None, type=self.name)
        try:
            response = self._image_recognition(query)
            tool_return.result = dict(text=str(response))
            tool_return.state = ActionStatusCode.SUCCESS
        except Exception as e:
            tool_return.result = dict(text=str(e))
            tool_return.state = ActionStatusCode.API_ERROR
        return tool_return

    def _image_recognition(self,
                query: str) -> str:
        print("Enter Image Recognition entry")
        data = json.loads(query)
        image_path = data.get("image_path", None)
        if image_path is not None:
            result = inferencer_mmdet(image_path, out_dir='./outputs/', no_save_pred=False, print_result=False)   
            result_prediction = result.get('predictions')[0]
            result_labels = result_prediction.get('labels')
            result_scores = result_prediction.get('scores')
            result_bboxes = result_prediction.get('bboxes')

            #only the first class
            image_class = classes_cocodataset[result_labels[0]]
        else:
            print("image_path不存在")
            image_class = "unknown"
        return 'image recognition response here is a ' + image_class

