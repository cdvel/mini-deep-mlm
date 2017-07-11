# Lesson 01: Introduction to Theano

Hi, Theano is a Python library for fast numerical computation to aid in the development of deep learning models.

At its heart, Theano is a compiler for mathematical expressions in Python. It knows how to take your structures and turn them into very efficient code that uses NumPy and efficient native libraries to run as fast as possible on CPUs or GPUs.

The actual syntax of Theano expressions is symbolic, which can be off-putting to beginners used to normal software development. Specifically, expression are defined in the abstract sense, compiled and later actually used to make calculations.

In this lesson, your goal is to install Theano and write a small example that demonstrates the symbolic nature of Theano programs.

For example, you can install Theano using pip as follows:
```
sudo pip install Theano
```

A small example of a Theano program that you can use as a starting point is listed below:
```
import theano
from theano import tensor
# declare two symbolic floating-point scalars
a = tensor.dscalar()
b = tensor.dscalar()
# create a simple expression
c = a + b
# convert the expression into a callable object that takes (a,b)
# values as input and computes a value for c
f = theano.function([a,b], c)
# bind 1.5 to 'a', 2.5 to 'b', and evaluate 'c'
result = f(1.5, 2.5)
print(result)
```


# Lesson 2:  Introduction to TensorFlow

Hi, TensorFlow is a Python library for fast numerical computing created and released by Google. Like Theano, TensorFlow is intended to be used to develop deep learning models.

With the backing of Google, perhaps used in some of its production systems and used by the Google DeepMind research group, it is a platform that we cannot ignore.

Unlike Theano, TensorFlow does have more of a production focus with a capability to run on CPUs, GPUs and even very large clusters.

In this lesson, your goal is to install TensorFlow become familiar with the syntax of the symbolic expressions used in TensorFlow programs.

For example, you can install TensorFlow using pip. There are many different versions of TensorFlow, specialized for each platform. Select the right version for your platform on the TensorFlow installation webpage.

Used method:

```
source activate root # root default conda env
sudo pip install tensorflow  # basic install no CUDA support

```

A small example of a TensorFlow program that you can use as a starting point is listed below:

```
import tensorflow as tf
# declare two symbolic floating-point scalars
a = tf.placeholder(tf.float32)
b = tf.placeholder(tf.float32)
# create a simple symbolic expression using the add function
add = tf.add(a, b)
# bind 1.5 to ' a ' , 2.5 to ' b ' , and evaluate ' c '
sess = tf.Session()
binding = {a: 1.5, b: 2.5}
c = sess.run(add, feed_dict=binding)
print(c)
```
