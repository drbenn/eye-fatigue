import tensorflow as tf
import numpy as np

# Basic TensorFlow operation
x = tf.constant([1.0, 2.0, 3.0])
y = tf.constant([3.0, 2.0, 1.0])
result = tf.reduce_sum(x * y)

# Return result
print(f"TensorFlow Result: {result.numpy()}")