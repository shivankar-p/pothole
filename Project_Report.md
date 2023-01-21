# Project Report
ApexCoders presents its revolutionary solution using Computer Vision which completely automates the process of pothole detection, 3D reconstruction in a single pipeline and also provides the further steps required to aid the situation. It is highly implementable and has high relevance with great future scopes in the fields of technology, city planning and healthcare.

## Abstract
Our solution uses a two fold approach to tackle the given problem.  
1.) Instance segmentation using Mask R-CNN : Our custom pothole classifier is trained using Mask R-CNN architecture, which runs on top of Faster R-CNN for both detection and segmentation purposes. For training, we have aggregated data from 5 different publicly available datasets to encompass diverse and varied road conditions such as cracks (Longitudinal, Lateral, Alligator), bumps, rutting, potholes, etc. Our model is able to identify the region and shape of potholes with an accuracy of 82%. This also outperforms the YOLO (v5 and v7) models.
2.) Generation of 3D spatial data : For 3D reconstruction, we have used Agisoft Metashape - a tool for photogrammetric processing. It is integrated with our general pipeline using a python script which interacts with the tool and automates the process of getting pothole dimensions and severity estimation.

## Photogrammetry (3D Reconstruction) Approach
1.) Alignment - 
  a.) Determine the correct position and orientation of each image in a series of aerial images (video frames) and minimize the reprojection error.
  b.) Search for the feature points on the images and match them across images into tie points (sparse point cloud points)
  c.) Determine the position of the camera for each image and fine-tune camera calibration settings.
2.) Sparse cloud is used for selecting stereo pairs (overlapping image pairs having sufficient number of common valid tie points).
3.) Depth maps are created for such overlapping pairs giving perspective from specific angles.
4.) Depth maps are merged together to form dense point cloud.
5.) Finally a surface in 3D (mesh) or 2.5D is created for modeling purposes and visualization.
