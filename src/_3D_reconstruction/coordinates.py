import Metashape

doc = Metashape.Document()
doc.open("_3D_reconstruction/full_vid.psx", ignore_lock = True)
#doc.open("2sec_vid.psx", ignore_lock = True)
chunk = doc.chunks[0]
# #chunk.importVideo(vid_path, img_path, frame_step=Metashape.FrameStep.CustomFrameStep,custom_frame_step=15)
# # chunk.matchPhotos(downscale=1, generic_preselection=True, reference_preselection=False)
# # chunk.alignCameras()
# # chunk.buildDepthMaps(downscale=4, filter_mode=Metashape.AggressiveFiltering)
# # chunk.buildModel(source_data = Metashape.DepthMapsData)


def get_coordinate(frame_no, pixel_x, pixel_y):

    # print("called get_coordinate")
    # print(frame_no, pixel_x, pixel_y)
    

    camera = chunk.cameras[frame_no]

    #print(frame_no, camera.transform)

    if camera.transform is None:
        for i in range(3500):
            print(chunk.cameras[i].transform)
    # while camera.transform is None:
    #     print("none block: "+str(frame_no))
    #     frame_no -= 1
    #     camera = chunk.cameras[frame_no]
    #     print(camera.transform)
    #     if frame_no == 0:
    #         break
    # print("camera", camera, frame_no)
    # print("transform", camera.transform, frame_no)
    point2D = Metashape.Vector([pixel_x, pixel_y]) # coordinates of the point on the given photo
    sensor = camera.sensor
    calibration = sensor.calibration
    coordinate = chunk.point_cloud.pickPoint(camera.center, camera.transform.mulp(sensor.calibration.unproject(point2D)))

    return (coordinate)
    #chunk.addMarker(point = x)


#print(get_coordinate(40, 436, 722))


# doc.save()