

import tensorflow as tf
import tensorflow_transform as tft
import loan_constant
import importlib

importlib.reload(loan_constant)

NUMERICAL_FEATURES = loan_constant.NUMERICAL_FEATURES
CATEGORICAL_NUMERICAL_FEATURES=loan_constant.CATEGORICAL_NUMERICAL_FEATURES
CATEGORICAL_STRING_FEATURES=loan_constant.CATEGORICAL_STRING_FEATURES
LABEL_KEY=loan_constant.LABEL_KEY
_VOCAB_SIZE = loan_constant.VOCAB_SIZE
_OOV_SIZE = loan_constant.OOV_SIZE
_LABEL_KEY = loan_constant.LABEL_KEY

def t_name(key):
  """
  Rename the feature keys so that they don't clash with the raw keys when
  running the Evaluator component.
  Args:
    key: The original feature key
  Returns:
    key with '_xf' appended
  """
  return key + '_xf'


def _make_one_hot(x, key):
    """Make a one-hot tensor to encode categorical features."""
    integerized = tft.compute_and_apply_vocabulary(x,
                                                   top_k=VOCAB_SIZE,
                                                   num_oov_buckets=OOV_SIZE,
                                                   vocab_filename=key,
                                                   name=key)
    depth = (tft.experimental.get_vocabulary_size_by_name(key) + OOV_SIZE)
    one_hot_encoded = tf.one_hot(integerized,
                                 depth=tf.cast(depth, tf.int32),
                                 on_value=1.0,
                                 off_value=0.0)
    return tf.reshape(one_hot_encoded, [-1, depth])

def _fill_in_missing(x):
    """Replace missing values in a SparseTensor."""
    if not isinstance(x, tf.sparse.SparseTensor):
        return x

    default_value = '' if x.dtype == tf.string else 0
    return tf.squeeze(tf.sparse.to_dense(tf.SparseTensor(x.indices, x.values, [x.dense_shape[0], 1]), default_value), axis=1)

def preprocessing_fn(inputs):
    """tf.transform's callback function for preprocessing inputs."""
    outputs = {}

    # Drop 'Loan_ID' column
    inputs.pop('Loan_ID')

    # Preprocess numerical features
    for key in NUMERICAL_FEATURES:
        outputs[t_name(key)] = tft.scale_to_z_score(_fill_in_missing(inputs[key]), name=key)

    # Preprocess categorical string features
    for key in CATEGORICAL_STRING_FEATURES:
        outputs[t_name(key)] = _make_one_hot(_fill_in_missing(inputs[key]), key)

    # Preprocess categorical numerical features
    for key in CATEGORICAL_NUMERICAL_FEATURES:
        outputs[t_name(key)] = _make_one_hot(tf.strings.strip(tf.strings.as_string(_fill_in_missing(inputs[key]))), key)

    # Process label key
     # Process label key and cast to tf.int64
    outputs[LABEL_KEY] = tf.cast(tf.where(tf.equal(_fill_in_missing(inputs[LABEL_KEY]), 'Y'), 1, 0), tf.int64)

    return outputs



