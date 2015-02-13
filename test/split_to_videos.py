import wave
import sys,os
from textgrid import TextGrid

from moviepy.editor import *

if len(sys.argv)<3:
    sys.exit()

grid = os.path.abspath(sys.argv[1])
grid = TextGrid.fromFile(grid)
videofile = VideoFileClip(sys.argv[2])

#wavPath=os.path.abspath(sys.argv[2])

print grid
grid=grid[len(grid)-1]
counter=0
print grid
print "files loaded"
for interval in grid: 
    intervalStr=str(interval)
    start,end,mark=intervalStr[intervalStr.find("(")+1:intervalStr.find(")")].split(',')
    print start,end,mark
    start=float(start)
    end=float(end)
    mark=mark.split()[0]
    if mark!='sil':
        if mark == 'sp':
            mark = 'SILENTSPACE'
        print "extracting :%s" %mark
        #win= wave.open(wavPath, 'rb')
        clip = videofile.subclip(start,end)
        clip.to_videofile('segments/segment%03d_%s.mp4'%(counter,mark))
        #t0,t1=start,end
        #t0, t1= 1.0, 2.0 # cut audio between one and two seconds
        #s0, s1= int(t0*win.getframerate()), int(t1*win.getframerate())

        #win.readframes(s0) # discard
        #frames= win.readframes(s1-s0)
        #wout = wave.open('segment%03d_%s.wav'%(counter,mark), 'wb')
        #wout.setparams(win.getparams())
        #wout.writeframes(frames)
        #wout.close()
        counter+=1
        #win.close()
    else:
        print mark
print "finnished"

