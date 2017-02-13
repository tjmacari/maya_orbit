# randomInstances.py

import maya.cmds as cmds
import random

random.seed ( 1234 )

result = cmds.ls( orderedSelection=True ) # create list in order of selection

# str - convert contents to plain text
# ie. result: [u'myCube2', u'playCube2'] - the transform and the orig cube - u: unicode
#print 'result: ' + str(result)
print 'result: %s' % ( result ) #same as above

# DAG - Directed Ayclic Graph (view in Window -> Outliner to see cube object and shape node)
# Duplicate cube by selecting in Outliner, then Edit -> Dup special (the box) then select instance/apply

transformName = result[0] # ie. result = ['myCube1', 'polyCube1'], so grab 'myCube1'

# group cubes neatly together
instanceGroupName = cmds.group( empty=True, name=transformName + '_instance_grp#' )

for i in range ( 0, 50 ):
    
    instanceResult = cmds.instance( transformName, name=transformName + '_instance#' )
    
    # add each instance to our group above
    cmds.parent( instanceResult, instanceGroupName )

    #print 'instanceResult: ' + str( instanceResult)
    
    x = random.uniform( -10, 10 )
    y = random.uniform( 0, 20 )
    z = random.uniform( -10, 10 )

    cmds.move (x, y, z, instanceResult ) # move over 10 units
    
    xRot = random.uniform( 0, 360 )
    yRot = random.uniform( 0, 360 )
    zRot = random.uniform( 0, 360 )
    
    cmds.rotate( xRot, yRot, zRot, instanceResult )
    
    scalingFactor = random.uniform( 0.3, 1.5 )
    
    cmds.scale( scalingFactor, scalingFactor, scalingFactor, instanceResult )
    
cmds.hide( transformName ) # hide orig cube
    
cmds.xform( instanceGroupName, centerPivots=True ) # Center the group pivot

# to make sure all items are facing the center:
# click Windows / selection/preferences / Selection text item, check 'Track Selection Order'

# can create any type of object (sphere, pyramid, etc.) and run this script, still works!
