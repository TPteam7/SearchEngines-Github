Image Blocker CNNBy: Trevor Pope and Micheal Callahan1. Problem StatementThis project is a proof-of-concept demonstrating the capability of Convolutional Neural Networks (CNNs) in image classification and filtering. The primary goal is to automatically detect and block unwanted images, using the classification of "dog" images as a practical example. The project explores web scraping for data collection and showcases how a machine learning model can be trained to process and filter visual content in real-time, laying the groundwork for applications in content moderation and personalized user experience.2. MethodologyConvolutional Neural Network (CNN) AlgorithmThe core of this project is a CNN built for binary image classification. The process is as follows:Network Architecture: A CNN is defined with convolutional layers, pooling layers for feature reduction, and fully connected layers for final classification. ReLU and Sigmoid activation functions are used.Input Processing: Images are standardized to 128x128 pixels and pixel values are normalized to a range between 0 and 1.Feature Extraction: Convolutional filters and max-pooling layers work together to extract key visual features (like edges, textures, and shapes) while reducing computational load.Classification: The resulting feature maps are flattened into a 1D vector and processed by dense layers. A final sigmoid activation function outputs a probability score, classifying the image as either "dog" (1) or "not dog" (0).Training: The model is trained using a binary cross-entropy loss function and the Adam optimizer. Early stopping is implemented to prevent overfitting and ensure the model generalizes well to new data.Data & PreprocessingA robust, balanced dataset is crucial for training an effective model.Data Sources: To avoid overfitting and build a comprehensive understanding of visual features, data was aggregated from three sources:90 Animals Dataset (Kaggle): To provide a diverse set of non-dog animal images.Stanford Dogs Dataset (Kaggle): To provide a wide variety of dog breeds, angles, and lighting conditions.Mammals Image Classification Dataset (Kaggle): To add more contextual data for distinguishing dogs from other mammals.Data Balancing: The final dataset was perfectly balanced, containing 19,091 dog images and 19,091 non-dog images.3. Model & PerformanceTransfer LearningTo improve performance and reduce training time, we used transfer learning.Base Model: MobileNetV2, pre-trained on the extensive ImageNet dataset.Strategy: The powerful, pre-trained feature extraction layers of MobileNetV2 were frozen, and new, custom classification layers were added on top to tailor the model for our specific dog vs. not-dog task.Model Architectureimport tensorflow as tf
from tensorflow.keras.layers import Dense, Flatten
from tensorflow.keras.models import Model
from tensorflow.keras.applications import MobileNetV2

# Load pre-trained MobileNetV2 without its top classification layers
base_model = MobileNetV2(weights='imagenet', include_top=False, input_shape=(128, 128, 3))

# Freeze the base model layers
for layer in base_model.layers:
    layer.trainable = False

# Add custom layers for our specific task
x = base_model.output
x = Flatten()(x)
x = Dense(128, activation='relu')(x)
x = Dense(64, activation='relu')(x)
output = Dense(1, activation='sigmoid')(x) # Output layer for binary classification

model = Model(inputs=base_model.input, outputs=output)

# Compile the model
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
EvaluationThe model demonstrated strong performance and rapid convergence, achieving a final test accuracy of 96.86%.MetricValueTest Accuracy96.86%Test Loss0.1041The confusion matrix below illustrates the model's precise predictions on the test set.(Note: Replace with a screenshot of your confusion matrix if available)[[1902, 63],
 [57, 1797]]
4. Future PotentialThis project successfully validates the use of CNNs for automated image filtering. Future enhancements could include:Web Deployment: Resolving challenges with TensorFlow.js to deploy the model in a browser-based application.Expanded Classification: Training the model to recognize and filter a wider range of content categories.Optimization: Implementing techniques like model quantization to improve inference speed and efficiency for real-world use.
