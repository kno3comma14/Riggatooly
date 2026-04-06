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
\x00\x00\x04T\
{\
\x0a    \x22english\x22: \
{\x0a        \x22ui\x22: \
{\x0a            \x22w\
indow_title\x22: \x22R\
iggatooly\x22,\x0a    \
        \x22header\x22\
: \x22PSD to Univer\
sal Rigging Stru\
cture\x22,\x0a        \
    \x22drop_label\x22\
: \x22Drag & Drop .\
psd or .kra(not \
implemente yet) \
file here\x5cnOR\x22,\x0a\
            \x22bro\
wse_btn\x22: \x22Brows\
e Files\x22,\x0a      \
      \x22browse_im\
age_btn\x22: \x22Brows\
e Images Folder\x22\
,\x0a            \x22l\
og_header\x22: \x22Pro\
cess Log:\x22,\x0a    \
        \x22run_btn\
\x22: \x22Generate Uni\
versal Rigging S\
tructure...\x22,\x0a  \
          \x22waiti\
ng_input\x22: \x22Wait\
ing for input...\
\x22,\x0a            \x22\
input_completed\x22\
: \x22Input files l\
oaded. Press Gen\
erate Universal \
Rigging Structur\
e button.\x22,\x0a    \
        \x22change_\
pivote_color_btn\
\x22: \x22Change Pivot\
e Color\x22\x0a       \
 },\x0a        \x22log\
s\x22: {\x0a          \
  \x22start\x22: \x22Star\
ting transformat\
ion...\x22,\x0a       \
     \x22load_succe\
ss\x22: \x22Loaded: {p\
ath}\x22,\x0a         \
   \x22xml_success\x22\
: \x22Success: Univ\
ersal Rigging St\
ructure modified\
.\x22,\x0a            \
\x22error_missing_f\
ile\x22: \x22Error: Co\
uld not find fil\
e {path}\x22\x0a      \
  },\x0a        \x22bu\
ttons\x22: {\x0a      \
      \x22ok\x22: \x22OK\x22\
,\x0a            \x22c\
ancel\x22: \x22Cancel\x22\
,\x0a            \x22y\
es\x22: \x22Yes\x22,\x0a    \
        \x22no\x22: \x22N\
o\x22,\x0a            \
\x22close\x22: \x22Close\x22\
\x0a        }\x0a    }\
\x0a}\x0a\
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
\x00\x00\x01\x9dc\xee\x92\x94\
"

def qInitResources():
    QtCore.qRegisterResourceData(0x03, qt_resource_struct, qt_resource_name, qt_resource_data)

def qCleanupResources():
    QtCore.qUnregisterResourceData(0x03, qt_resource_struct, qt_resource_name, qt_resource_data)

qInitResources()
