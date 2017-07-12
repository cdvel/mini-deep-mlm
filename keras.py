#### Code samples only, not runnable

# step 1: Define model: Create a sequential and add configured layers

from keras.models import Sequential
model = Sequential()

from keras.layers import Dense, Activation

model.add(Dense(units=64, input_dim=100))
model.add(Activation('relu'))
model.add(Dense(units=10))
model.add(Activation('softmax'))

# step 2: Compile model, specifying loss fx, and optimizers > call compile()

model.compile(loss='categorical_crossentropy', optimizer='sgd', metrics=['accuracy'])

# step 3: Fit your model: Train the model on sample; calling fit()

model.fit(x_tran, y_train, epochs=5, batch_size=32)

#or

model.train_on_batch(x_batch, y_batch)

# evaluate performance

loss_and_metrics = model.evaluate(x_test, y_test, batch_size=128)

# step 4: generate predictions

classes = model.predict(x_test, batch_size=128)


