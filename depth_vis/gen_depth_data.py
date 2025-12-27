#!/usr/bin/env python3
# Developed by Xieyuanli Chen and Thomas Läbe
# This file is covered by the LICENSE file in the root of this project.
# Brief: a script to generate depth data

from .utils import range_projection
import os
import numpy as np

def gen_depth_data(scan_path, dst_folder, normalize=False):
  """ Generate projected range data in the shape of (64, 900, 1).
      The input raw data are in the shape of (Num_points, 3).
  """
  # specify the goal folder
  dst_folder = os.path.join(dst_folder, 'depth')
  try:
    os.stat(dst_folder)
    print('generating depth data in: ', dst_folder)
  except:
    print('creating new depth folder: ', dst_folder)
    os.mkdir(dst_folder)


  depths = []
  
  # iterate over all scan files
  # load a point cloud
  current_vertex = np.fromfile(scan_path, dtype=np.float32)
  current_vertex = current_vertex.reshape((-1, 4))

  proj_range, _, _, _ = range_projection(current_vertex)

  # normalize the image
  if normalize:
    proj_range = proj_range / np.max(proj_range)

  # generate the destination path
  dst_path = os.path.join(dst_folder, 'depth')

  # save the semantic image as format of .npy
  np.save(dst_path, proj_range)
  depths.append(proj_range)
  print('finished generating depth data at: ', dst_path)

  return depths
  

if __name__ == '__main__':
  scan_folder = '/folder/of/lidar/scans'
  dst_folder = '/folder/to/store/depth/data'
  
  depth_data = gen_depth_data(scan_folder, dst_folder)
