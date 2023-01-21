# Project Report
ApexCoders presents its revolutionary solution using Computer Vision which completely automates the process of pothole detection, 3D reconstruction in a single pipeline and also provides the further steps required to aid the situation. Our solution has high practical significance and has high relevance with great future scopes in the fields of technology, city planning and healthcare.

## Abstract
Our solution uses a two fold approach to tackle the given problem.  
1. Instance segmentation using Mask R-CNN : Our custom pothole classifier is trained using Mask R-CNN architecture, which runs on top of Faster R-CNN for both detection and segmentation purposes. For training, we have aggregated data from 5 different publicly available datasets to encompass diverse and varied road conditions such as cracks (Longitudinal, Lateral, Alligator), bumps, rutting, potholes, etc. Our model is able to identify the region and shape of potholes with an accuracy of 82%. This also outperforms the YOLO (v5 and v7) models.  
2. Generation of 3D spatial data : For 3D reconstruction, we have used Agisoft Metashape - a tool for photogrammetric processing. It is integrated with our general pipeline using a python script which interacts with the tool and automates the process of getting pothole dimensions and severity estimation.  

## Photogrammetry (3D Reconstruction) Approach
![Untitled Diagram drawio (2) drawio (1) (1)](https://user-images.githubusercontent.com/77499650/213863827-41cba4b6-4099-42be-bce7-f433db6b4209.png)  
1. Alignment -  
    - Determine the correct position and orientation of each image in a series of aerial images (video frames) and minimize the reprojection error.  
    - Search for the feature points on the images and match them across images into tie points (sparse point cloud points)  
    - Determine the position of the camera for each image and fine-tune camera calibration settings.  
2. Sparse cloud is used for selecting stereo pairs (overlapping image pairs having sufficient number of common valid tie points).  
3. Depth maps are created for such overlapping pairs giving perspective from specific angles.   
4. Depth maps are merged together to form dense point cloud.  
5. Finally a surface in 3D (mesh) or 2.5D is created for modeling purposes and visualization.  
![Screenshot 2023-01-21 at 2 17 47 PM](https://user-images.githubusercontent.com/77499650/213862742-656bb652-b56f-40f3-a431-7e39c05a81ce.png)  

## General Workflow
 ![Untitled Diagram drawio (2) drawio (1)](https://user-images.githubusercontent.com/77499650/213863844-e92af244-ea6f-4f9a-82b6-fffd110bf84c.png)  
1. A sequence of motion pictures/frames or a video is given as a input to our Classifier which parallelly performs the following operations -   
    - A dense point cloud is created by breaking the video at critical points. The process is further optimized by appropriately selecting just the sufficient number of frames required.  
    - The input is passed to our ML model which detects and masks the potholes, cracks and other damaged regions on the road.  
2. For each output frame from our ML Model, the segmented pixels of each identified pothole in the frame are used to set markers in the dense point cloud that can track the corresponding pothole in the video and thus gives the overall 3D coordinates of the pixels of that pothole across all the frames. This helps in -  
    - Validating each pothole detected by the ML model by checking its elevation, depth, etc.  
    - Calculating the average depth, perimeter and surface area of each valid pothole using the 3D coordinates from the reconstructed point cloud. These will be normalized to the centimeter scale, which shall be used to calculate pothole severity.  
3. It is possible that the road surface itself has different elevation at different points. Keeping that in mind, the depth of each pothole is calculated with respect to the elevation of the road bounding it, rather than using a base elevation for the entire 3D mesh.  
4. After getting all the physical properties of each pothole in a frame, the below metric is used to calculate its severity/magnitude[1]. Potholes with different levels of severity are masked accordingly. Specific road segments with a large number of potholes of high severity are also marked in the final output video.  
![Screenshot 2023-01-19 at 2 21 14 PM](https://user-images.githubusercontent.com/77499650/213862773-f4b4c0c3-3299-4f5b-a5bc-da2b98cdfbca.png)  

## Cost and Performance Efficiency
- In order to speed up the process of computation, we sample the pixels by using the Markov Chain Monte-Carlo technique which leverages the frequency distribution of pixels so as to reduce the number of pixels we need to process.   
- On the prototype level, We are able to process 3 - 4 frames per second on a standard RTX 3060 for no cost. The processing speed can be increased exponentially by using industry standard hardware.  

## Relevance and City Planning
- Our solution is capable of being deployed on edge (NVIDIA Jetson Nano or a more advanced Jetson TX2) and thus can mark the damaged areas on the spot through any IoT devices feeding in camera footage. Furthermore, no other input is required such as laser calibrated surface profiling or ultrasonic sensor data, thereby cutting down the cost of hardware and time spent for doing labor as our entire solution relies on automation. Therefore, our solution is a great alternative for Mobile Lidar related technologies and requires almost no human intervention as even the camera orientation/calibration is determined during the reconstruction process.  
- Furthermore, our solution proposes the following scheme to categorize potholes based on the response times they need for repair/reconstruction. This helps in establishing the most urgent and problematic potholes and road areas. The scheme takes into account the severity as well as the importance of the road estimated by the frequency of its use in a qualitative manner.    
![Screenshot 2023-01-20 at 12 11 48 AM](https://user-images.githubusercontent.com/77499650/213862785-e27e000e-5a22-4122-873f-a72dae5703a3.png)&nbsp;&nbsp;&nbsp;  
Emergency: 2 hour response (Road Collapse)  
Category 1: Repair within 5 days  
Category 2: Repair is required within four calendar months  

## Future Scope
1. Our solution can be easily scaled up to run on thermal and satellite imagery as well which are quite often used in city planning.  
2. It can be integrated with navigation applications (such as Google apps, Waze etc.) to alert the users and can be used for optimal path selection thereby increasing the apps reliability and help in accident prevention.  

## REFERENCES
[1] Public Works Department of Malaysia, 1992. A Guide to Visual Assessment of Flexible Pavement SurfaceConditions, Public Works Department, Malaysia.
