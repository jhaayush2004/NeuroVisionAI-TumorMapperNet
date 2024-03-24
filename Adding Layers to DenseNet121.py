head = clf_model.output
head = AveragePooling2D(pool_size=(4,4))(head)
head = Flatten(name='Flatten')(head)
head = Dense(256, activation='relu')(head)
head = Dropout(0.3)(head)
head = Dense(256, activation='relu')(head)
head = Dropout(0.3)(head)
head = Dense(128, activation='relu')(head)
head = Dropout(0.1)(head)
head = Dense(2, activation='softmax')(head)

model = Model(clf_model.input, head)
model.compile(loss = 'categorical_crossentropy', 
              optimizer='adam', 
              metrics= ["accuracy"]
             )
model.summary()
earlystopping = EarlyStopping(monitor='val_loss', 
                              mode='min', 
                              verbose=1, 
                              patience=20
                             )
checkpointer = ModelCheckpoint(filepath="clf-densenet-weights_new2.hdf5", 
                               verbose=1, 
                               save_best_only=True,
                               monitor='val_acc',
                               mode='max'
                              )
reduce_lr = ReduceLROnPlateau(monitor='val_loss',
                              mode='min',
                              verbose=1,
                              patience=10,
                              min_delta=0.0001,
                              factor=0.1
                             )
callbacks = [checkpointer, earlystopping, reduce_lr]
h = model.fit(train_generator, 
              steps_per_epoch=total_images // 16, 
              epochs = 70, 
              validation_data= valid_generator, 
              validation_steps= valid_generator.n // valid_generator.batch_size, 
              callbacks=[checkpointer, earlystopping])
