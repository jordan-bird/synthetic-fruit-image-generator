from numpy.random import randn
from numpy.random import randint
from keras.models import load_model
from matplotlib import pyplot
import time
import argparse

desc = "Generate synthetic healthy and unhealthy lemon images."
parser = argparse.ArgumentParser(description=desc)

parser.add_argument('--type',
                    type=str,
                    help='"healthy" or "unhealthy"',
                    required=True)
					
args = parser.parse_args()

classToGen = args.type.lower()


# generate points in latent space as input for the generator
def generate_latent_points(latent_dim, n_samples, class_to_gen, n_classes=2):
	x_input = randn(latent_dim * n_samples)
	z_input = x_input.reshape(n_samples, latent_dim)
	# generate labels
	if class_to_gen==1:
		labels = randint(1, n_classes, n_samples)
	if class_to_gen==0:
		labels = randint(0, 1, n_samples)
	return [z_input, labels]

def save_plot(examples, n):
	for i in range(n * n):
		pyplot.subplot(n, n, 1 + i)
		pyplot.axis('off')
		pyplot.imshow(examples[i])
		#filename = "synthetic_images/0/" + str(time.time()) + ".jpg"
		filename = str(time.time()) + ".jpg"
		pyplot.imsave(filename, examples[i])
		
	#pyplot.show()

def generate():
	model = load_model('lemons_generator_2000.h5')

	for x in range(0,10):
		latent_points, labels = generate_latent_points(100, 100, classToGen)
		X  = model.predict([latent_points, labels])
		X = (X + 1) / 2.0
		save_plot(X, 10)

if classToGen == "healthy":
	classToGen = 1
	print("Generating healthy lemons...")
	generate()
	print("Done!")
elif classToGen == "unhealthy":
	classToGen = 0
	print("Generating bad lemons...")
	generate()
	print("Done!")
else: 
	print('Error: define --type as "healthy" or "unhealthy"')