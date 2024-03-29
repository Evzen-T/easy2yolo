from export_yolov5 import YoloV5Exporter
from pathlib import Path

downloadpth = Path("./yolov5/runs/train/exp/weights")
filepth = "best.pt"
input_shape = [640,416]
conv_id = 1

exporter = YoloV5Exporter(downloadpth, filepth, input_shape, conv_id)

try:
    exporter.export_onnx()
except Exception as e:
    raise RuntimeError("onnx conversion failed")
version = "v5"
try:
    exporter.export_openvino(version)
except Exception as e:
    raise RuntimeError("openvino conversion failed")
try:
    exporter.export_blob()
except Exception as e:
    raise RuntimeError("blob conversion failed")
try:
    exporter.export_json()
except Exception as e:
    raise RuntimeError("json export failed")