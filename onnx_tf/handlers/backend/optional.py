from onnx_tf.handlers.backend_handler import BackendHandler
from onnx_tf.handlers.handler import onnx_op


@onnx_op("Optional")
class Optional(BackendHandler):

  @classmethod
  def version_15(cls, node, **kwargs):
    if len(node.inputs) > 0:
        return [kwargs["tensor_dict"][node.inputs[0]]]
    else:
        return [None]
