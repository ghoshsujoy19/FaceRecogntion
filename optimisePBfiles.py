import tensorflow as tf
from tensorflow.python.tools import freeze_graph
from tensorflow.python.tools import optimize_for_inference_lib

input_graph_def = tf.GraphDef()
with tf.gfile.Open('fruitRecog.pb', "rb") as f:
    input_graph_def.ParseFromString(f.read())
input_node_names = ['input_1']
output_node_name = 'dense_2/Softmax'
output_graph_def = optimize_for_inference_lib.optimize_for_inference(
    input_graph_def, input_node_names, [output_node_name],
    tf.float32.as_datatype_enum)

with tf.gfile.FastGFile('optimisedFruit2.pb', "wb") as f:
    f.write(output_graph_def.SerializeToString())

print("graph saved!")

# import os, glob
# from pprint import pprint
# dirlist = glob.glob('/home/sujoy/*')
# pprint(dirlist)
