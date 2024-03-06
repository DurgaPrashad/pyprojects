import numpy as np
import matplotlib.pyplot as plt
from keras.layers import Input, Conv2D, MaxPooling2D, UpSampling2D
from keras.models import Model
from keras.datasets import mnist

# Load and preprocess the dataset
(X_train, ), (, _) = mnist.load_data()
X_train = X_train.astype('float32') / 255.
X_train = np.reshape(X_train, (len(X_train), 28, 28, 1))

# Create occluded images for training (remove a portion of pixels)
occlusion_factor = 0.5  # Fraction of pixels to be removed
X_occluded = X_train * (np.random.random(X_train.shape) > occlusion_factor)

# Define autoencoder model
def build_autoencoder():
    input_img = Input(shape=(28, 28, 1))

    # Encoder
    x = Conv2D(32, (3, 3), activation='relu', padding='same')(input_img)
    x = MaxPooling2D((2, 2), padding='same')(x)
    x = Conv2D(32, (3, 3), activation='relu', padding='same')(x)
    encoded = MaxPooling2D((2, 2), padding='same')(x)

    # Decoder
    x = Conv2D(32, (3, 3), activation='relu', padding='same')(encoded)
    x = UpSampling2D((2, 2))(x)
    x = Conv2D(32, (3, 3), activation='relu', padding='same')(x)
    x = UpSampling2D((2, 2))(x)
    decoded = Conv2D(1, (3, 3), activation='sigmoid', padding='same')(x)

    return Model(input_img, decoded)

# Build and compile the autoencoder model
autoencoder = build_autoencoder()
autoencoder.compile(optimizer='adam', loss='binary_crossentropy')

# Train the autoencoder with occluded images
autoencoder.fit(X_occluded, X_train, epochs=50, batch_size=128, shuffle=True, validation_split=0.2)

# Function to visualize original, occluded, and reconstructed images
def visualize_results(original, occluded, reconstructed):
    plt.figure(figsize=(10, 3))

    for i in range(5):
        # Original image
        plt.subplot(3, 5, i + 1)
        plt.imshow(original[i].reshape(28, 28), cmap='gray')
        plt.axis('off')
        plt.title('Original')

        # Occluded image
        plt.subplot(3, 5, 5 + i + 1)
        plt.imshow(occluded[i].reshape(28, 28), cmap='gray')
        plt.axis('off')
        plt.title('Occluded')

        # Reconstructed image
        plt.subplot(3, 5, 10 + i + 1)
        plt.imshow(reconstructed[i].reshape(28, 28), cmap='gray')
        plt.axis('off')
        plt.title('Reconstructed')

    plt.tight_layout()
    plt.show()

# Generate reconstructed images
reconstructed_images = autoencoder.predict(X_occluded)

# Visualize the results
visualize_results(X_train, X_occluded, reconstructed_images)