import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'
import tensorflow as tf
#declare 2 symbolic floating point scalars
a = tf.placeholder(tf.float32)
b = tf.placeholder(tf.float32)
#create a simple symbolic expression using the add function
add = tf.add(a, b)
#bind 1.5 to 'a', 2.5 to 'b' and  compute
sess = tf.Session()
binding = {a: 1.5, b: 2.5}
c = sess.run(add, feed_dict=binding)
print(c)
