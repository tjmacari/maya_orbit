{\rtf1\ansi\ansicpg1252\cocoartf1348\cocoasubrtf170
{\fonttbl\f0\fmodern\fcharset0 CourierNewPSMT;}
{\colortbl;\red255\green255\blue255;}
\margl1440\margr1440\vieww10800\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural

\f0\fs24 \cf0 # keyRotation.py\
\
import maya.cmds as cmds\
\
def keyFullRotation ( pObjectName, pStartTime, pEndTime, pTargetAttribute ):\
    cmds.cutKey( pObjectName, time=(pStartTime, pEndTime), attribute=pTargetAttribute )\
    cmds.setKeyframe ( pObjectName, time=pStartTime, attribute=pTargetAttribute, value=0 )\
    cmds.setKeyframe ( pObjectName, time=pEndTime, attribute=pTargetAttribute, value=360 )\
    cmds.selectKey ( pObjectName, time=(pStartTime, pEndTime), attribute=pTargetAttribute, keyframe=True )\
    cmds.keyTangent ( inTangentType='linear', outTangentType='linear' )\
    \
selectionList = cmds.ls( selection=True, type='transform' )\
\
if len( selectionList ) >= 1:\
    \
    startTime = cmds.playbackOptions( query=True, minTime=True )\
    endTime = cmds.playbackOptions( query=True, maxTime=True )\
    \
    for objectName in selectionList:\
        \
        keyFullRotation( objectName, startTime, endTime, 'rotateY' )\
\
else:\
    print 'Please select at least one item'\
}