midifolder2synthesia
====================

A script to create Synthesia groupt tree from directory tree in a filesystem

This simple script walks a given folder and its subfolders, creating XML "metadata" description to use with Synthesia software. The metadata creates synthesia "group" tree that mimics the directory tree of the original folder with files. The description is saved to a file named folder.synthesia in the same folder, so that Synthesia picks it up automatically.

USAGE
=====

If you have python installed, simply run midifolder2synthesia.py and in the dialog select the top level folder that you wish to convert to Synthesia "groups". Top-level directory will become a top level group, subdirectories will become sub-groups, and so on. On a Windows without python installation, user can run midifolder2synthesia.exe executable instead.

NOTES
=====

Windows executable was created with pyinstaller using the following command:

   pyinstaller midifolder2synthesia.py -F -w --distpath .
