import Metashape
import cv2
import os
import glob


files = glob.glob('/Images')
for f in files:
    os.remove(f)


doc = Metashape.Document()
doc.save(path = "full_vid.psx")

chunk = doc.addChunk()

vid_path = "../Videos/First_Dataset.mp4"
img_path = "Images/GP1_{filenum}.png"


photos = []

# Opens the Video file
cap= cv2.VideoCapture(vid_path)
i=0
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == False:
        break
    cv2.imwrite('Images/frame'+str(i)+'.jpg',frame)
    photos.append("Images/frame"+str(i)+".jpg")
    i+=1

cap.release()
cv2.destroyAllWindows()


chunk.addPhotos(photos)
for frame in chunk.frames:
    frame.matchPhotos(downscale = 1) # HighestAccuracy

chunk.alignCameras()
chunk.buildDepthMaps(downscale = 2, filter_mode = Metashape.MildFiltering)
chunk.buildPointCloud()

doc.save()
# #chunk.importVideo(vid_path, img_path, frame_step=Metashape.FrameStep.CustomFrameStep,custom_frame_step=15)
# # chunk.matchPhotos(downscale=1, generic_preselection=True, reference_preselection=False)
# # chunk.alignCameras()
# # chunk.buildDepthMaps(downscale=4, filter_mode=Metashape.AggressiveFiltering)
# # chunk.buildModel(source_data = Metashape.DepthMapsData)


# camera = chunk.cameras[34]
# point2D = Metashape.Vector([1104, 803]) # coordinates of the point on the given photo
# sensor = camera.sensor
# calibration = sensor.calibration
# x = chunk.point_cloud.pickPoint(camera.center, camera.transform.mulp(sensor.calibration.unproject(point2D)))
# print(x)
# chunk.addMarker(point = x)
# # print(camera.center)
# # print(sensor.calibration.unproject(point2D))
# # print(camera.transform.mulp(sensor.calibration.unproject(point2D)))
# #chunk.addMarker(point = Metashape.Vector([1, 2, 3]))

# # for m in chunk.markers:
# #     print(m.position)

# doc.save()
