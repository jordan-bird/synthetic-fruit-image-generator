# :lemon: Synthetic Lemon Image Generator :lemon:
![Synthetic mouldy lemons](preview.jpg)

This code utilises a Conditional Generative Adversarial Network which has been trained on healthy and unhealthy lemons 

## :lemon: What does this code do? :lemon:
This program loads a trained CGAN and then can generate synthetic images of either healthy or unhealthy classed lemons. We did this for data augmentation purposes.

## :lemon: Requirements :lemon:
* NumPy
* Keras

I used NumPy v1.19.3 and Keras v2.4.3 with TensorFlow 2.4.0 backend, but most versions should work

## :lemon: How do I use this? :lemon:
Simply run either:
```
python generate_lemons.py --type=healthy
```
or:
```
python generate_lemons.py --type=healthy
```

Then, 1000 jpg files will be generated of lemons that are either healthy or unhealthy

## :lemon: Training info :lemon:
The CGAN was trained on 256x256px images for 2000 epochs on an RTX 2080Ti which took around 17 hours. More info is available in the paper below

## :lemon: References :lemon:

This model was developed for the following research paper: *I'll add a link soon when the preprint is uploaded*

Trained on the [Lemons quality control dataset](https://github.com/softwaremill/lemon-dataset)

Generator code from [Machine Learning Mastery](https://machinelearningmastery.com/how-to-develop-a-conditional-generative-adversarial-network-from-scratch/)

(Jason Brownlee's code has been edited to support larger RGB images, and the program requires the definition of the class by the user)
