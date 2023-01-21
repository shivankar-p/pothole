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

def severity_estimator(per_area):
    severity_label = 'HIGH'
    mask_colour = [255, 0, 0]
    depth = -1
    if per_area > 3.2:
        severity_label = 'ROAD SECTION DAMAGED'
        mask_colour = [139,69,19]
        depth = 0
    else:

        if (per_area <= 0.05):
            depth = 40 * per_area

        elif (per_area <= 0.1):
            depth = -40 * per_area + 7
        
        elif per_area <= 0.6:
            depth = -5 * per_area + 7
            
        elif per_area <= 1:
            depth = -5 * per_area + 8
            
        else:
            depth = -1 * per_area + 5
            
        
        if (depth >= 5):
            severity_label = 'HIGH'
            mask_colour = [255, 0, 0]
        elif (depth >= 4):
            severity_label = 'MODERATE'
            mask_colour = [253, 218, 13]
        else:
            severity_label = 'LOW'
            mask_colour = [60, 179, 113]

    return mask_colour, depth, severity_label
