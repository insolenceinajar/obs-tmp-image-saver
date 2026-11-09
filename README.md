# obs-tmp-image-saver
Workaround for OBS to directly drag image files on stream without saving them to disk first.

A quick note on how to get it working:
- locate your OBS scripts folder trough "Tools > Scripts"
- while you're at it, make sure to have some version of python installed and OBS is aware of it in the "python settings" tab
- save ".py" to OBS' script folder (can be located through the "Tools > Scripts" window)
- make an empty folder where the temporary images can be stored, can be called anything, for instance "tmp"
- one line of the script needs to be adjusted depending on where you saved the new folder: look for the line that says "expPath" and copy in the path to your "tmp" file accordingly (the "/" at the end is imprortant)
- all done!

One small caveat: the "temporary" images will pile up after a while, so there's a "Empty tmp folder" next to the script when you load it in "Tools > Scripts".
The scripts detects png, jpg, bmp and gif. If you need any other image file formats, you'd need to add those accordingly around line 25-28 in the script (I never had to, but just in case).
