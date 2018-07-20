# Fruit-Flower-Classifier

This repository provides the Jupyter notebook which can be used to train the [Fruit-360](https://kaggle.com/moltean/fruits) kaggle dataset for recognition of 75 fruits and [Flowers Recognition](kaggle.com/alxmamaev/flowers-recognition) kaggle dataset for recognition of 5 flowers.
These notebooks were submitted as kaggle kernel, so you may need to change the code so as to run on your PC or cloud.

----------
## **Dependencies** :
- [keras](https://keras.io/)
- [tensorflow>=1.8](https://www.tensorflow.org/install/)
- [pandas](https://pandas.pydata.org/pandas-docs/stable/install.html)
- [python>=3.5](https://www.python.org/downloads/)
- [jupyter](jupyter.org)

----------
## Technical Details
This repository contains 2 folders and 1 python file.
Folders:
- **Flower-Recognition** : It contains the jupyter notebook for training "Flower Recognition" dataset. It generates the model protobuf file which is used in [Flower Classifier](https://github.com/ghoshsujoy19/FlowerRecogniser) android app.
- **Fruit-Recognition** : It contains the jupyter notebook for training "Fruit-360" dataset. It generates the model protobuf file which is used in [Fruit Classifier](https://github.com/ghoshsujoy19/FlowerRecogniser) android app.

Python File:
- **optimisePBFiles** : It is a python file to optimise the protobuf files, thereby reducing the protobuf file size. You may need to do the optimisation as android gives "Out of Memory" error when file size is too large.(Of course there are other ways also to make it work)

-------
### Training
Run the following command to start jupyter
```sh
$ jupyter notebook
```
and run your required notebook.
Of course there are scope of improvements like:
- Training with more images 
- Using more complex models like inception-v3
- using callbacks like [ReduceLROnPlateau](https://keras.io/callbacks/#reducelronplateau)...
etc.
So feel free to modify it to your own needs.

--------
### Accuracy

**Flower-Recognition**: 
- VGG16_FlowerModel.ipynb : Testing Accuracy = 90%

**Fruit-Recognition**:
- VGG16_model.ipynb : Testing Accuracy = 96.5%
- ResNet50_model.ipynb : Testing Accuracy = 97.2%
- ConvModel.ipynb : Testing Accuracy = 95.4%

License
----

GNU GENERAL PUBLIC LICENSE

