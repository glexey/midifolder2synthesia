# This simple script walks a given folder and its subfolders, creating XML
# "metadata" description to use with Synthesia software. The metadata
# creates synthesia "group" tree that mimics the directory tree of the
# original folder with files. The description is saved to a file named
# folder.synthesia in the same folder, so that Synthesia picks it up
# automatically.
#
# Written by: Alexey Gaydyukov

import os
import sys
import hashlib
import Tkinter, tkFileDialog

groupindent = 2

def close_group(prevlevel, level, groups):
    while (prevlevel >= level):
        groups += "  " * (prevlevel + groupindent) + '</Group>\n'
        prevlevel -= 1
    return groups

def do_work():
    try:
        dirname = tkFileDialog.askdirectory(parent=root)
        if not dirname: exit(0) # user pressed 'cancel'
        songs = "  <Songs>\n"
        groups = "  <Groups>\n"
        startinglevel = dirname.count(os.sep)
        fout = open(os.path.join(dirname, 'folder.synthesia'), 'w')
        fout.write('<?xml version="1.0" encoding="utf-8"?>\n<SynthesiaMetadata Version="1">\n')
        prevlevel = -1
        unique_ids = set()
        for (path, dirnames, filenames) in os.walk(dirname):
            level = path.count(os.sep) - startinglevel
            groups = close_group(prevlevel, level, groups)
            groupname = os.path.split(path)[1]
            groups += "  " * (level + groupindent) + '<Group Name="%s">\n'%groupname
            prevlevel = level
            for filename in filenames:
                if filename.lower().endswith(".mid") or filename.lower().endswith(".midi"):
                    fullname = os.path.join(path, filename)
                    title = os.path.splitext(filename)[0]
                    md5 = hashlib.md5(open(fullname, 'rb').read()).hexdigest()
                    if md5 in unique_ids: continue # duplicate file, discard second occurence
                    unique_ids.add(md5)
                    songs += '    <Song UniqueId="%s" Title="%s" />\n'%(md5, title)
                    groups += "  " * (level + groupindent + 1) + '<Song UniqueId="%s" />\n'%md5
        groups = close_group(prevlevel, 0, groups)
        groups += "  </Groups>\n"
        songs += "  </Songs>\n"
        fout.write(("%s%s"%(songs, groups)).encode('utf-8'))
        fout.write('</SynthesiaMetadata>\n')
    finally:
        root.destroy()

if __name__=='__main__':
    root = Tkinter.Tk()
    root.after_idle(do_work)
    root.mainloop()
