{\rtf1\ansi\ansicpg1252\cocoartf1348\cocoasubrtf170
{\fonttbl\f0\fmodern\fcharset0 CourierNewPSMT;}
{\colortbl;\red255\green255\blue255;}
\margl1440\margr1440\vieww10800\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural

\f0\fs24 \cf0 # aimAtFirst.py\
\
import maya.cmds as cmds\
\
selectionList = cmds.ls( orderedSelection=True )\
\
if len( selectionList ) >= 2:\
    targetName = selectionList[0]\
    selectionList.remove( targetName )\
    for objectName in selectionList:\
        cmds.aimConstraint( targetName, objectName, aimVector=[0,1,0] )\
}