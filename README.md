# Pothole Severity Classification via Computer Vision
##### This whole Project was primarly build for the SMARTHATHON hackathon 2023 (January) theme 2 (Pothole Severity Classification via Computer Vision).

## _Instructions to run the code_
### Run this [notebook]().
 <pre>        (or)           </pre>
### Run it locally with the following instructions:
- Clone the repository.
```console
git clone https://github.com/shivankar-p/pothole.git
```
- Go into the repository
```console
cd pothole/src
```
- Linux - Install metashape standalone module wheel File.(For other os find wheel file [here](https://www.agisoft.com/downloads/installer/)
```console
wget https://s3-eu-west-1.amazonaws.com/download.agisoft.com/Metashape-2.0.0-cp35.cp36.cp37.cp38-abi3-linux_x86_64.whl
python3 -m pip install Metashape-2.0.0-cp35.cp36.cp37.cp38-abi3-linux_x86_64.whl
```
- Install other required packages
```console
pip install -r requirements.txt
```
- Inside the models folder(in src) download the model file from this [link](https://drive.google.com/file/d/17IY3CnSz7AaIXwE7Q8RSkAV4_6UPiO6-/view)
- Navigate back to src directory
- For Inference on image run:
```console
python3 mask.py --image <image-path>
```
- For Inference on video run:
```console
python3 mask.py --video <video-path>
```
## Technologies used
- python
- Agiosoft Metashape
- openCV
- tensorflow
- keras
- matplotlib
- numpy

## [Video demo link]()

## [Output video link](https://www.youtube.com/watch?v=9Fv6yXQz52g)

## [Report link](https://github.com/shivankar-p/pothole/blob/main/Project_Report.md)


## Notes
* Do note that the code for Mask R-CNN was obtained from Matterport's [repository](https://github.com/matterport/Mask_RCNN).
* You can find the trained model at [model Google Drive link](https://drive.google.com/file/d/17IY3CnSz7AaIXwE7Q8RSkAV4_6UPiO6-/view)


## References Used
- Public Works Department of Malaysia, 1992. A Guideto Visual Assessment of Flexible Pavement SurfaceConditions, Public Works Department, Malaysia.

## Team
- [Shivankar Pilligundla](https://www.linkedin.com/in/shivankar-pilligundla-a1112a201/)
- [Hardik Khandelwal](https://www.linkedin.com/in/hardik-khandelwal-533599205/)
- [Karanjit Saha](https://www.linkedin.com/in/karanjit-saha-65a02122b/)
- [Netradeepak Chinchwadkar](https://www.linkedin.com/in/netradeepak-chinchwadkar-30728a201/)
- [Abhinav Mahajan](https://www.linkedin.com/in/abhinav-mahajan-727068233/)
- [Srinivas Manda](https://www.linkedin.com/in/srinivas-manda-41a302224/)




