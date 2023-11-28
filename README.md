# Pothole Severity Classification via Computer Vision
The Project was build for the SMARTATHON Challenge 2023 theme 2 (Pothole Severity Classification via Computer Vision).

## Instructions to run the code
### Run this [notebook](https://colab.research.google.com/drive/153bOqpGplhfOoz8-_T6x5dmdYNLEN5_l?usp=sharing).
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

## [Demo video link](https://www.youtube.com/watch?v=AVYgmbHnvBQ)

## [Output video link](https://www.youtube.com/watch?v=9Fv6yXQz52g)

## Output Screenshots
<img width="1728" alt="3" src="https://user-images.githubusercontent.com/77498897/213882123-7f482699-c2c1-4504-b099-7ff8c6a82148.png">
<img width="1728" alt="1" src="https://user-images.githubusercontent.com/77498897/213882126-17d42982-7f3c-4a50-a3dc-2dafd7abf287.png">
<img src="https://user-images.githubusercontent.com/77498897/213882194-c3789999-0370-4f9c-81da-136626186169.jpg">
<img src="https://user-images.githubusercontent.com/77498897/213882195-53395cdd-ce91-468b-a5b5-24fec70ea8e4.jpg">
<img src="https://user-images.githubusercontent.com/77498897/213882196-274a52bb-3a2d-4699-a53e-f338135ab235.jpg">


## Team
- [Shivankar Pilligundla](https://www.linkedin.com/in/shivankar-pilligundla-a1112a201/)
- [Hardik Khandelwal](https://www.linkedin.com/in/hardik-khandelwal-533599205/)
- [Karanjit Saha](https://www.linkedin.com/in/karanjit-saha-65a02122b/)
- [Netradeepak Chinchwadkar](https://www.linkedin.com/in/netradeepak-chinchwadkar-30728a201/)
- [Abhinav Mahajan](https://www.linkedin.com/in/abhinav-mahajan-727068233/)
- [Srinivas Manda](https://www.linkedin.com/in/srinivasa-bhargava-manda)




