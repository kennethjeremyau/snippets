#!/usr/bin/env python

import os

current_file = __file__
print('current file: {}'.format(current_file))

current_dir = os.path.dirname(current_file)
print('current dir: {}'.format(current_dir))

abs_path_file = os.path.abspath(current_file)
print('abs path of file: {}'.format(abs_path_file))

abs_path_dir = os.path.dirname(abs_path_file)
print('abs path of dir: {}'.format(abs_path_dir))

relative_path_child = os.path.join(current_dir, 'next')
print('relative path of child dir: {}'.format(relative_path_child))

relative_path_sibling = os.path.join('..', 'sibling')
print('relative path of sibling dir: {}'.format(relative_path_sibling))

abs_path_sibling = os.path.join(os.path.abspath('..'), 'sibling')
print('abs path of sibling dir: {}'.format(abs_path_sibling))
