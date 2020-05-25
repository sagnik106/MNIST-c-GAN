[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com)

[![python3](https://img.shields.io/badge/python-v3.8-blue)](https://www.python.org)

# MNIST c-GAN
A conditional Generative Adversarial Network to generate a specific "handwritten"(I know computers do not have hands) digit.

# Dataset
The dataset is the famous [MNIST - Handwritten Digit Classification]() dataset that comes built-in the [tensorflow.keras.datasets]() module.

## Dataset Analysis
![analysis](https://github.com/sagnik106/MNIST-c-GAN/blob/master/resources/data_analysis.png)
![classes](https://github.com/sagnik106/MNIST-c-GAN/blob/master/resources/dataclass.png)

# Requirements
* Numpy 1.18.3
* Matplotlib 3.2.1
* Scikit-learn 0.22.2
* Tensorflow 2.2

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