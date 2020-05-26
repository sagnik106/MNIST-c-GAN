[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com)

[![python3](https://img.shields.io/badge/python3-v3.8-blue?style=for-the-badge&logo=python)](https://www.python.org)

# MNIST c-GAN
A conditional Generative Adversarial Network to generate a specific "handwritten"(I know computers do not have hands) digit.

# Dataset
The dataset is the famous [MNIST - Handwritten Digit Classification](http://yann.lecun.com/exdb/mnist/) dataset that comes built-in the [tensorflow.keras.datasets](https://www.tensorflow.org/api_docs/python/tf/keras/datasets/mnist) module.

## Dataset Analysis
![analysis](https://github.com/sagnik106/MNIST-c-GAN/blob/master/resources/data_analysis.png)
![classes](https://github.com/sagnik106/MNIST-c-GAN/blob/master/resources/dataclass.png)

# Requirements
* Numpy 1.18.3
* Matplotlib 3.2.1
* Scikit-learn 0.22.2
* Tensorflow 2.2
* OpenCV 4.2

# Model Architecture
### Generator
![generator](https://github.com/sagnik106/MNIST-c-GAN/blob/master/resources/generator.png)
### Discriminator
![discriminator](https://github.com/sagnik106/MNIST-c-GAN/blob/master/resources/discriminator.png)
### Adversarial
![adversarial](https://github.com/sagnik106/MNIST-c-GAN/blob/master/resources/adversarial.png)

# Model metrics
![metrics](https://github.com/sagnik106/MNIST-c-GAN/blob/master/resources/performance.png)

# Model Output
![output](https://github.com/sagnik106/MNIST-c-GAN/blob/master/resources/output.jpg)

# File Configuration
* [main.ipynb](https://github.com/sagnik106/MNIST-c-GAN/blob/master/main.ipynb) - Jupyter notebook which has the analysis of dataset along with the declaration and training of the model
* [resources/](https://github.com/sagnik106/MNIST-c-GAN/blob/master/resources/) - Github README resources
* [generator.py](https://github.com/sagnik106/MNIST-c-GAN/blob/master/generator.py) - Generates the image with a CLI (Run it you will find out)

# Author
Sagnik Sarkar - [![Github](https://img.shields.io/badge/Github-Sagnik%20Sarkar-green?style=for-the-badge&logo=github)](https://github.com/sagnik106)
[![Linkedin](https://img.shields.io/badge/Linkedin-Sagnik%20Sarkar-blue?style=for-the-badge&logo=linkedin)](https://www.linkedin.com/in/lesagniksarkar/)