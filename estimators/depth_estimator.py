# import sys

# sys.path.insert(1, "3D_reconstruction")

import random

from _3D_reconstruction import coordinates

def get_pothole_depth(frame_no, _2d_coordinates):

    depth = 0

    for coord in _2d_coordinates:
        
        projection = coordinates.get_coordinate(frame_no, coord[0], coord[1])

        if projection is not None:
            depth = min(depth, projection[1])
        #print(depth)
    
    return depth


def get_perimeter(mask, first_row, last_row):
    perimeter_pixels = []
    for i in range(first_row, last_row+1):
            cnt = 0
            p = 0
            q = len(mask[0])-1
            flag1 = 0
            flag2 = 0
            p_temp = -1
            while flag1 == 0 or flag2 == 0:
            
            
                if mask[i][p+cnt] == 1 and flag1 == 0:
                    perimeter_pixels.append([i, p+cnt])
                    flag1 = 1
                    p_temp = p+cnt



                if mask[i][q-cnt] == 1 and flag2 == 0:
                    if q-cnt != p_temp:
                        perimeter_pixels.append([i, q-cnt])
                    flag2 = 1

                cnt += 1
    return perimeter_pixels

def get_ref_depth(perimeter_pixels, frame_no):
    mh = 0
    for i in perimeter_pixels:
        projection = coordinates.get_coordinate(frame_no, i[0], i[1])
        if projection is not None:
            mh = max(mh, projection[1])
    return mh





