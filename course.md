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


# Lesson 02:  Introduction to TensorFlow

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


# Lesson 03: Intro to Keras

Hi, a difficulty of both Theano and TensorFlow is that it can take a lot of code to create even very simple neural network models.

These libraries were designed primarily as a platform for research and development more than for the practical concerns of applied deep learning.

The Keras library addresses these concerns by providing a wrapper for both Theano and TensorFlow. It provides a clean and simple API that allows you to define and evaluate deep learning models in just a few lines of code.

Because of the ease of use and because it leverages the power of Theano and TensorFlow, Keras is quickly becoming the go-to library for applied deep learning.

The focus of Keras is the concept of a model. The life-cycle of a model can be summarized as follows:

1. Define your model. Create a Sequential model and add configured layers.

2. Compile your model. Specify loss function and optimizers and call the compile() function on the model.

3. Fit your model. Train the model on a sample of data by calling the fit() function on the model.

4. Make predictions. Use the model to generate predictions on new data by calling functions such as evaluate() or predict() on the model.
Your goal for this lesson is to install Keras.

For example, you can install Keras using pip:

`sudo pip install keras`

Start to familiarize yourself with the Keras library ready for the upcoming lessons where we will implement our first model.

# Lesson 04: Crash Course in Multi-Layer Perceptrons

Hi, artificial neural networks are a fascinating area of study, although they can be intimidating when just getting started.

The field of artificial neural networks is often just called neural networks or multi-layer Perceptrons after perhaps the most useful type of neural network.

The building block for neural networks are artificial neurons. These are simple computational units that have weighted input signals and produce an output signal using an activation function.

Neurons are arranged into networks of neurons. A row of neurons is called a layer and one network can have multiple layers. The architecture of the neurons in the network is often called the network topology.

Once configured, the neural network needs to be trained on your dataset. The classical and still preferred training algorithm for neural networks is called stochastic gradient descent.

Your goal for this lesson is to become familiar with neural network terminology.

Dig a little deeper into terms like neuron, weights, activation function, learning rate and more.

