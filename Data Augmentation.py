from keras_preprocessing.image import ImageDataGenerator
from itertools import chain

datagen = ImageDataGenerator(
    rescale=1./255.,
    validation_split=0.1,
    width_shift_range=0.2,
    rotation_range=20,
    zoom_range=0.2,
    shear_range=0.2
)

train_generators = []

for i in range(2):
    train_generator = datagen.flow_from_dataframe(
        train,
        directory='./',
        x_col='image_path',
        y_col='mask',
        subset='training',
        class_mode='categorical',
        batch_size=16,
        shuffle=True,
        target_size=(256,256)
    )
    train_generators.append(train_generator)

# Concatenate the generators into a single generator
train_generator = chain.from_iterable(train_generators)
from keras_preprocessing.image import ImageDataGenerator
from itertools import chain

datagen = ImageDataGenerator(
    rescale=1./255.,
    validation_split=0.1,
    width_shift_range=0.2,
    rotation_range=20,
    zoom_range=0.2,
    shear_range=0.2
)

train_generators = []

for i in range(2):
    train_generator = datagen.flow_from_dataframe(
        train,
        directory='./',
        x_col='image_path',
        y_col='mask',
        subset='training',
        class_mode='categorical',
        batch_size=16,
        shuffle=True,
        target_size=(256,256)
    )
    train_generators.append(train_generator)

# Concatenate the generators into a single generator
train_generator = chain.from_iterable(train_generators)

