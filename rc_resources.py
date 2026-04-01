# Resource object code (Python 3)
# Created by: object code
# Created by: The Resource Compiler for Qt version 6.11.0
# WARNING! All changes made in this file will be lost!

from PySide6 import QtCore

qt_resource_data = b"\
\x00\x00\x02L\
/\
* Styling the dr\
op area specific\
ally by its obje\
ct name */\x0a#Drop\
Frame {\x0a    bord\
er: 2px dashed #\
555;\x0a    border-\
radius: 10px;\x0a  \
  background-col\
or: #222;\x0a}\x0a\x0a#Dr\
opFrame:hover {\x0a\
    border-color\
: #00adb5;\x0a    b\
ackground-color:\
 #2a2a2a;\x0a}\x0a\x0a/* \
You can also sty\
le all buttons h\
ere */\x0aQPushButt\
on {\x0a    backgro\
und-color: #333;\
\x0a    color: whit\
e;\x0a    padding: \
5px;\x0a    border-\
radius: 4px;\x0a}\x0a\x0a\
QPushButton#RunB\
utton {\x0a    back\
ground-color: #0\
0adb5;\x0a    font-\
weight: bold;\x0a}\x0a\
\x0aQPushButton#Run\
Button:disabled \
{\x0a    background\
-color: #444; \x0a \
   color: #888; \
           \x0a    \
border: 1px soli\
d #555; \x0a}\x0a\
\x00\x00\x02@\
{\
\x0a    \x22ui\x22: {\x0a   \
     \x22window_tit\
le\x22: \x22Riggatooly\
\x22,\x0a        \x22head\
er\x22: \x22PSD to Tah\
oma2D Pipeline\x22,\
\x0a        \x22drop_l\
abel\x22: \x22Drag & D\
rop .tnz or .jso\
n here\x5cnOR\x22,\x0a   \
     \x22browse_btn\
\x22: \x22Browse Files\
\x22,\x0a        \x22log_\
header\x22: \x22Proces\
s Log:\x22,\x0a       \
 \x22run_btn\x22: \x22Inj\
ect Offsets & Pa\
rent Pegs\x22,\x0a    \
    \x22waiting_inp\
ut\x22: \x22Waiting fo\
r input...\x22\x0a    \
},\x0a    \x22logs\x22: {\
\x0a        \x22start\x22\
: \x22Starting tran\
sformation...\x22,\x0a\
        \x22load_su\
ccess\x22: \x22Loaded:\
 {path}\x22,\x0a      \
  \x22xml_success\x22:\
 \x22Success: XML s\
tructure modifie\
d.\x22,\x0a        \x22er\
ror_missing_file\
\x22: \x22Error: Could\
 not find file {\
path}\x22\x0a    }\x0a}\x0a\
"

qt_resource_name = b"\
\x00\x04\
\x00\x06\xa8\xa1\
\x00d\
\x00a\x00t\x00a\
\x00\x09\
\x00(\xad#\
\x00s\
\x00t\x00y\x00l\x00e\x00.\x00q\x00s\x00s\
\x00\x0c\
\x012:\xde\
\x00s\
\x00t\x00r\x00i\x00n\x00g\x00s\x00.\x00j\x00s\x00o\x00n\
"

qt_resource_struct = b"\
\x00\x00\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x01\
\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x00\x00\x02\x00\x00\x00\x02\x00\x00\x00\x02\
\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x0e\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\
\x00\x00\x01\x9dJ\x0d\xac|\
\x00\x00\x00&\x00\x00\x00\x00\x00\x01\x00\x00\x02P\
\x00\x00\x01\x9dC\xd4\x1b\xa3\
"

def qInitResources():
    QtCore.qRegisterResourceData(0x03, qt_resource_struct, qt_resource_name, qt_resource_data)

def qCleanupResources():
    QtCore.qUnregisterResourceData(0x03, qt_resource_struct, qt_resource_name, qt_resource_data)

qInitResources()
