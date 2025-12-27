#!/usr/bin/env python3
import sys, os
import matplotlib.pyplot as plt
import depth_vis.gen_depth_data as gen_depth
import depth_vis.gen_normal_data as gen_normal
import depth_vis.gen_intensity_data as gen_intensity


def show_images(depth_data, normal_data, intensity_data):
    """ This function is used to visualize different types of data
        generated from the LiDAR scan, including depth, normal, intensity and semantics.
    """
    fig, axs = plt.subplots(3, figsize=(6, 4))
    axs[0].set_title('range_data')
    axs[0].imshow(depth_data)
    axs[0].set_axis_off()

    axs[1].set_title('normal_data')
    axs[1].imshow(normal_data)
    axs[1].set_axis_off()

    axs[2].set_title('intensity_data')
    # truncate the intensity to better visualize
    intensity_data[intensity_data < 0] = 0
    axs[2].imshow(intensity_data, cmap='gray')
    axs[2].set_axis_off()

    plt.suptitle('Preprocessed data from the LiDAR scan')
    plt.show()


def gen_data(scan_path, dst_folder=None, visualize=True):
    """ This function is used to generate different types of data
        from the LiDAR scan, including depth, normal, intensity and semantics.
    """
    range_data = gen_depth.gen_depth_data(scan_path, dst_folder)[0]
    normal_data = gen_normal.gen_normal_data(scan_path, dst_folder)[0]
    intensity_data = gen_intensity.gen_intensity_data(scan_path, dst_folder)[0]

    if visualize:
        show_images(range_data, normal_data, intensity_data)


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description="KIITI Depth Visualization")
    parser.add_argument(
        "--split",
        type=str,
        default="training",
        help="use training split or testing split (default: training)",
    )
    parser.add_argument(
        "-i",
        "--ind",
        type=int,
        default=0,
        metavar="N",
        help="input  (default: data/object)",
    )
    args = parser.parse_args()
    # set the related parameters
    scan_path = os.path.join('./data/object', args.split, 'velodyne', "%06d.bin" % (args.ind))
    dst_folder = './imgs'

    # start the demo1 to generate different types of data from LiDAR scan
    gen_data(scan_path,  dst_folder)