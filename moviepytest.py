from moviepy.editor import *


clip = VideoFileClip("test.mp4").subclip(10,20)


clip.to_videofile("output.mp4")
print "done"
