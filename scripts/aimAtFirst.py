# aimAtFirst.py

import maya.cmds as cmds

selectionList = cmds.ls( orderedSelection=True )

if len( selectionList ) >= 2:
    targetName = selectionList[0]
    selectionList.remove( targetName )
    for objectName in selectionList:
        cmds.aimConstraint( targetName, objectName, aimVector=[0,1,0] )