# This file is MACHINE GENERATED! Do not edit.
# Generated by: tensorflow/python/tools/api/generator/create_python_api.py script.
"""Utilities for text input preprocessing.

"""

from __future__ import print_function as _print_function

import sys as _sys

from tensorflow.python.keras.preprocessing.text import Tokenizer
from tensorflow.python.keras.preprocessing.text import hashing_trick
from tensorflow.python.keras.preprocessing.text import one_hot
from tensorflow.python.keras.preprocessing.text import text_to_word_sequence

del _print_function

from tensorflow.python.util import module_wrapper as _module_wrapper

if not isinstance(_sys.modules[__name__], _module_wrapper.TFModuleWrapper):
  _sys.modules[__name__] = _module_wrapper.TFModuleWrapper(
      _sys.modules[__name__], "keras.preprocessing.text", public_apis=None, deprecation=True,
      has_lite=False)
