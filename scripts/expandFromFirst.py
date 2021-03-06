# expandFromFirst.py

import maya.cmds as cmds

selectionList = cmds.ls( orderedSelection=True, type='transform' )

if len( selectionList ) >= 2:

    targetName = selectionList[0]

    selectionList.remove ( targetName )

    #create empty group where we will store all our locators
    locatorGroupName = cmds.group( empty=True, name='expansion_locator_grp#' )

    maxExpansion = 100

    newAttributeName = 'expansion'

    if not cmds.objExists( '%s.%s' % ( targetName, newAttributeName ) ):

        cmds.select( targetName )

        cmds.addAttr( longName=newAttributeName, shortName='exp', attributeType='double', min=0, max=maxExpansion, defaultValue=maxExpansion, keyable=True )

    #iterate over each object in selection list
    for objectName in selectionList:

        # get first object's coords
        coords = cmds.getAttr( '%s.translate' % ( objectName ) )[0]

        # set to objects coords
        locatorName = cmds.spaceLocator( position=coords, name='%s_loc#' % ( objectName ) )[0]

        # center-pivot object
        cmds.xform( locatorName, centerPivots=True )

        # group new locator under designated group
        cmds.parent( locatorName, locatorGroupName )

        # constrain object between target and locator
        pointConstraintName = cmds.pointConstraint( [ targetName, locatorName ], objectName, name='%s_pointConstraint#' % ( objectName ) )[0]

        # ie. string=pSphere1W0=100-pSphere1.expansion
        cmds.expression( alwaysEvaluate=True, name='%s_attractWeight' % ( objectName ), object=pointConstraintName, string='%sW0=%s-%s.%s' % ( targetName, maxExpansion, targetName, newAttributeName ) )

        # (1) source attribute, (2) destination
        cmds.connectAttr( '%s.%s' % ( targetName, newAttributeName ), '%s.%sW1' % ( pointConstraintName, locatorName ) )

    # center locator pivot
    cmds.xform( locatorGroupName, centerPivots=True )

else:
    print 'Please select 2 or more items'