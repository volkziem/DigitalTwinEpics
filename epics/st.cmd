#!../../bin/linux-x86_64/dtwin

#- SPDX-FileCopyrightText: 2003 Argonne National Laboratory
#-
#- SPDX-License-Identifier: EPICS

#- You may have to change dtwin to something else
#- everywhere it appears in this file

< envPaths

epicsEnvSet(STREAM_PROTOCOL_PATH,"../../dtwinApp/Db")

cd "${TOP}"

## Register all support components
dbLoadDatabase "dbd/dtwin.dbd"
dtwin_registerRecordDeviceDriver pdbbase

drvAsynIPPortConfigure("SOCKET1","127.0.0.1:8000",0,0,0)

dbLoadRecords("dtwinApp/Db/wienfilter.db","PORT='SOCKET1',USER='DT'")
dbLoadRecords("dtwinApp/Db/magnets.db","PORT='SOCKET1',USER='DT'")
dbLoadRecords("dtwinApp/Db/bpm.db","PORT='SOCKET1',USER='DT'")
#dbLoadRecords("dtwinApp/Db/bpm2.db","PORT='SOCKET1',USER='DT'")
dbLoadRecords("dtwinApp/Db/misc.db","PORT='SOCKET1',USER='DT'")

cd "${TOP}/iocBoot/${IOC}"
iocInit
