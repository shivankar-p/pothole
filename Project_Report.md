# Project Report
ApexCoders presents its revolutionary solution using Computer Vision which completely automates the process of pothole detection, 3D reconstruction in a single pipeline and also provides the further steps required to aid the situation. It is highly implementable and has high relevance with great future scopes in the fields of technology, city planning and healthcare.

## Abstract
Our solution uses a two fold approach to tackle the given problem.
1.) Instance segmentation using Mask R-CNN : Our custom pothole classifier is trained using Mask R-CNN architecture, which runs on top of Faster R-CNN for both detection and segmentation purposes. For training, we have aggregated data from 5 different publicly available datasets to encompass diverse and varied road conditions such as cracks (Longitudinal, Lateral, Alligator), bumps, rutting, potholes, etc. Our model is able to identify the region and shape of potholes with an accuracy of 82%. This also outperforms the YOLO (v5 and v7) models.

2.) Generation of 3D spatial data : For 3D reconstruction, we have used Agisoft Metashape - a tool for photogrammetric processing. It is integrated with our general pipeline using a python script which interacts with the tool and automates the process of getting pothole dimensions and severity estimation.
