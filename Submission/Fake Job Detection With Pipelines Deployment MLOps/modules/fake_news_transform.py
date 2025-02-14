"""Module for preprocessing and transforming fake news data."""

import tensorflow as tf

LABEL_KEY = "is_fake"
FEATURE_KEY = "text"

def transformed_name(key):
    """Renaming transformed features."""
    return key + "_xf"

def preprocessing_fn(inputs):
    """
    Preprocess input features into transformed features.
    
    Args:
        inputs: map from feature keys to raw features.
    
    Returns:
        outputs: map from feature keys to transformed features.    
    """
    
    print("Input keys:", inputs.keys())  # Debugging, tampilkan keys
    
    outputs = {}
    
    # Transform features
    outputs[transformed_name(FEATURE_KEY)] = tf.strings.lower(inputs[FEATURE_KEY])
    outputs[transformed_name(LABEL_KEY)] = tf.cast(inputs[LABEL_KEY], tf.int64)
    
    return outputs
