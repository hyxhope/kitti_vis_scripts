# KITTI Object data transformation and visualization



## Dataset

Download the data (calib, image\_2, label\_2, velodyne) from [Kitti Object Detection Dataset](http://www.cvlibs.net/datasets/kitti/eval_object.php?obj_benchmark=3d) and place it in your data folder at `kitti/object`


The folder structure is as following:
```
kitti
    object
        testing
            calib
               000000.txt
            image_2
               000000.png
            label_2
               000000.txt
            velodyne
               000000.bin
            pred
               000000.txt
        training
            calib
               000000.txt
            image_2
               000000.png
            label_2
               000000.txt
            velodyne
               000000.bin
            pred
               000000.txt
```

## Install locally
- start from a new conda enviornment:
```
(base)$ conda create -n kitti_vis python=3.10
or 环境我打包好了，直接create就行了，如果直接create，就不用install了，直接运行可视化py就行了；
(base)$ conda env create -f environment.yaml
(base)$ conda activate kitti_vis
```
- opencv, pillow, scipy, matplotlib
```
(kitti_vis)$ pip install opencv-python pillow scipy matplotlib
```
- install mayavi from conda-forge, this installs vtk and pyqt5 automatically
```
(kitti_vis)$ conda install mayavi -c conda-forge
```
- vis script
```
(kitti_vis)$ python kitti_object.py --show_lidar_with_depth --img_fov --const_box --vis --show_image_with_boxes --ind 138 --show_lidar_topview_with_boxes --gen_depth --split testing
```

结果会存在imgs文件夹下