## Service Desk Ticket Classification with Deep Learning
CleverSupport is a company at the forefront of AI innovation, specializing in the development of AI-driven solutions to enhance customer support services. Their latest endeavor is to engineer a text classification system that can automatically categorize customer complaints.

# Project Overview
CeverSupport is a company at the forefront of AI innovation, specializing in developing AI-driven solutions to enhance customer support services. Their latest endeavor is to engineer a text classification system that can automatically categorize customer complaints. As a data scientist, your role involves creating a sophisticated machine learning model to accurately assign complaints to specific categories, such as mortgage, credit card, money transfers, debt collection, etc.

This project aims to classify service desk tickets into categories using a Convolutional Neural Network (CNN) to streamline customer services.

# Project Structure

The project is organized as follows:

*Data Loading*: Load and prepare the training and testing datasets.
*Model Definition*: Define a CNN classifier with the necessary layers.
*Training*: Train the classifier on the training data.
*Evaluation*: Evaluate the classifier on the test data and calculate performance metrics.

# Model Architecture
The CNN classifier is defined with the following layers:
- An embedding layer to convert words into dense vectors.
- A 1D convolution layer to capture local patterns in the text.
- A linear (fully connected) layer to output the class probabilities.

# Requirements

The following libraries are required to run the project:

- torch
- torch.nn
- torch.utils.data
- torchmetrics
- numpy
- pandas
- json
- nltk
- collections
- sklearn

# Performance Metrics
The model's performance is evaluated using the following metrics:

- Accuracy: Overall accuracy of the model.
- Precision (per class): Precision score for each class.
- Recall (per class): Recall score for each class.

The metrics are printed at the end of the evaluation phase.

# Conclusion

This project demonstrates the use of a CNN for classifying service desk tickets into various categories, helping streamline customer support services. The defined model and its training process can serve as a template for similar text classification tasks.
