# :lemon: Synthetic Lemon Image Generator :lemon:
![Synthetic mouldy lemons](preview.jpg)

This code utilises a Conditional Generative Adversarial Network which has been trained on healthy and unhealthy lemons 

## :lemon: What does this code do? :lemon:
This program loads a trained CGAN and then can generate synthetic images of either healthy or unhealthy classed lemons. We did this for data augmentation purposes.

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

## :lemon: References :lemon:

Trained on the [Lemons quality control dataset](https://github.com/softwaremill/lemon-dataset)

Generator code from [Machine Learning Mastery](https://machinelearningmastery.com/how-to-develop-a-conditional-generative-adversarial-network-from-scratch/)

(Jason Brownlee's code has been edited to support larger RGB images, and the program requires the definition of the class by the user)
