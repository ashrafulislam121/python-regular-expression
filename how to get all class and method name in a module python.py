# -*- coding: utf-8 -*-
"""
Created on Sat Apr  1 00:11:14 2023

@author: Ashraful Islam
"""

import inspect
import re

# Get all class names
class_names = [cls for name, cls in inspect.getmembers(re) if inspect.isclass(cls)]

# Get all method names from each class
method_names = []
for cls in class_names:
    methods = inspect.getmembers(cls, predicate=inspect.ismethod)
    method_names += [name for name, method in methods]

print(class_names)
print(method_names)