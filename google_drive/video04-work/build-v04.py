from pathlib import Path
from PIL import Image,ImageOps
import imageio_ffmpeg,subprocess
p=Path('google_drive/video04-work');d=p/'frames';d.mkdir(exist_ok=True)
blocks=[56.97,53.52,69.16,65.48,60.08,38.55]
plan=[
 ['n07','n08','n01','n08','n07','n09'],
 ['n09','n10','n10','n11','n06','n15'],
 ['n15','n06','n16','n11','n18','n15'],
 ['n12','n02','n03','n13','n14','n14','n04'],
 ['n04','n17','n05','n16','n18','n08'],
 ['n19','n20','n08','n19'],
]
i=0;dur=[]
for shots,block in zip(plan,blocks):
    sec=block/len(shots)
    for n in shots:
        im=ImageOps.fit(Image.open(p/f'{n}.png').convert('RGB'),(1280,720),method=Image.Resampling.LANCZOS)
        im.save(d/f'{i:02}.jpg',quality=95);dur.append(sec);i+=1
f=p/'v4.ffconcat'
f.write_text('ffconcat version 1.0\n'+''.join(f"file 'frames/{k:02}.jpg'\nduration {s:.4f}\n" for k,s in enumerate(dur))+f"file 'frames/{i-1:02}.jpg'\n")
ff=imageio_ffmpeg.get_ffmpeg_exe();out='google_drive/video-04-draft-v1.mp4'
subprocess.run([ff,'-y','-v','error','-f','concat','-safe','0','-i',str(f),'-i','google_drive/video-04-narration.mp3',
 '-filter_complex','[0:v]fps=24,format=yuv420p[v]','-map','[v]','-map','1:a','-t','343.76',
 '-c:v','libx264','-preset','veryfast','-crf','20','-pix_fmt','yuv420p','-c:a','aac','-movflags','+faststart',out],check=True)
subprocess.run([ff,'-v','error','-i',out,'-f','null','-'],check=True)
print('shots',i,'|',subprocess.run([ff,'-i',out],capture_output=True,text=True).stderr.split('Duration: ')[1][:11])
