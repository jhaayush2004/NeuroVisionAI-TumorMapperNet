from tensorflow.keras.applications import DenseNet121
clf_model = DenseNet121(weights='imagenet', include_top=False, input_tensor=Input(shape=(256,256,3)))
clf_model.summary()
# before this i tried with trainable layer but the accuracy was less as compared
for layer in clf_model.layers:
    layers.trainable = False
