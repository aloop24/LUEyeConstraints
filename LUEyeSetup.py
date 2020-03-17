import maya.cmds as cmds

#get list of shots from camera sequencer
shotList=cmds.sequenceManager(lsh=True)
print(shotList)
previousCameras = []
aimConstraintNum = 1
leftConstrainList = []
rightConstrainList = []

for x in shotList:
    #get camera for the current shot
    currentShot = str(x)
    currentCamera = cmds.shot(currentShot, q = True, currentCamera = True)
    if currentCamera.endswith('Shape'):
        currentCamera = currentCamera[:-5]
        
        



    #if not already used, set up locator and parent constraint system for the camera
    if currentCamera not in previousCameras:
        #Now is a previous camera so this doesn't get done twice
        previousCameras.append(currentCamera)
        
        #Put a locator in the same position as the camera and directly parent it in
        cameraPosition = cmds.camera(currentCamera, q = True, position = True)
        locator = cmds.spaceLocator(name = currentCamera + "_locator", position = cameraPosition)
        cmds.parent( locator, currentCamera)
        
        #Create aim constraints between the new locator and the eye controls
        cmds.aimConstraint( locator, "seq005_LUExport:LU:LEye_ctrlgrp")
        cmds.aimConstraint( locator, "seq005_LUExport:LU:REye_ctrlgrp")
        
        #Add the new constraint attributes to the list for each eye control
        leftConstrainList.append(str(currentCamera) + "_locatorW" + str(previousCameras.index(currentCamera)))
        rightConstrainList.append(str(currentCamera) + "_locatorW" + str(previousCameras.index(currentCamera)))
        
        
        
for x in shotList:
    #get camera for the current shot
    currentShot = str(x)
    currentCamera = cmds.shot(currentShot, q = True, currentCamera = True)
    if currentCamera.endswith('Shape'):
        currentCamera = currentCamera[:-5]
    print(currentCamera)
    print(previousCameras)           
    #Identify the Constraint attribute to be given weight and key appropriately    
    lConstrainAttr = str(currentCamera) + "_locatorW" + str(previousCameras.index(currentCamera))
    rConstrainAttr = str(currentCamera) + "_locatorW" + str(previousCameras.index(currentCamera))
    print(lConstrainAttr)
    print(leftConstrainList)
    startFrame = cmds.shot(currentShot, q = True, startTime = True)
    endFrame = cmds.shot(currentShot, q = True, endTime = True)
    cmds.setKeyframe("LEye_ctrlgrp_aimConstraint1", attribute = lConstrainAttr, t=startFrame, value =1)
    cmds.setKeyframe("REye_ctrlgrp_aimConstraint1", attribute = rConstrainAttr, t=startFrame, value =1)
    cmds.setKeyframe("LEye_ctrlgrp_aimConstraint1", attribute = lConstrainAttr, t=endFrame, value =1)
    cmds.setKeyframe("REye_ctrlgrp_aimConstraint1", attribute = rConstrainAttr, t=endFrame, value =1)
    for x in leftConstrainList:
        xstr = str(x)
        if xstr != lConstrainAttr:
            cmds.setKeyframe("LEye_ctrlgrp_aimConstraint1", attribute = xstr, t=startFrame, value =0)
            cmds.setKeyframe("REye_ctrlgrp_aimConstraint1", attribute = xstr, t=startFrame, value =0)
            cmds.setKeyframe("LEye_ctrlgrp_aimConstraint1", attribute = xstr, t=endFrame, value =0)
            cmds.setKeyframe("REye_ctrlgrp_aimConstraint1", attribute = xstr, t=endFrame, value =0)
        
        
