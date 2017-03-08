import os
from subprocess import call
import time

try:
    os.popen("mkdir C:\\dEkota")
    os.popen("attrib +h C:\\dEkota")
    print('Directory made!')
except:
    print('existing directory!')

def open_file(text_file):
    urls = open(text_file, "r")
    urls = urls.readlines()
    urls = [x.replace('\n','') for x in urls]
    urls = [x.replace('','') for x in urls]
    threshold = urls[0]
    threshold = float(threshold.split(' = ')[1])
    urls = urls[1:]
    return urls, threshold

try:
    urls, threshold = open_file("random.cfg")
    print('Setting threshold to', threshold)
    print('Urls and threshold loaded')
except:
    urls = [
            'https://giphy.com/gifs/2qh13B8iEyQmI',
            'https://giphy.com/gifs/thegifys-cats-gifys-5xaOcLM0A365irVKtUY',
            'https://giphy.com/gifs/cbbtv-scott-aukerman-7XOjMcwzfAHbW',
            'https://giphy.com/gifs/back-to-the-future-marty-mcfly-great-scott-5y8sRBYSWWb16',
            'https://giphy.com/gifs/seann-william-scott-stifler-american-wedding-iV1UVvuKg1Z3q',
            'https://giphy.com/gifs/parks-and-recreation-ben-wyatt-parksedit-enai2FLiWILkI',
            'https://giphy.com/gifs/dance-tyler-scott-l2YLmNqwix1N6',
            'https://giphy.com/gifs/rapper-jenner-pedophile-5mOYqrxPF5aW4',
            'https://giphy.com/gifs/funny-website-spicy-XIhzqUpi2slTq',
            'https://giphy.com/gifs/comedy-bang-cbb-eleventh-day-of-oscar-KVUhxQAqrAV3i',
            'https://giphy.com/gifs/teen-wolf-cast-gif-3VxQRRy82PNYI',
            'https://giphy.com/gifs/office-steve-carell-vbBj4gxOeY6c0',
            'https://giphy.com/gifs/beyonce-confidence-empower-xvx1WT7Sc6cEg',
            'https://giphy.com/gifs/la-neogaf-nostra-MoaWzlFAovnsk',
            'https://giphy.com/gifs/superfruit-mitch-grassi-sup3rfruit-ACIUyRP62zDbO',
            'https://giphy.com/gifs/funny-lol-what-FRRK3vMJ4no52',
            'https://giphy.com/gifs/whats-happening-rerun-fred-berry-vCQYVaqJmIjV6',
            'https://giphy.com/gifs/deal-with-it-i-dont-care-sbCdjSJEGghGM',
            'https://giphy.com/gifs/david-hasselhoff-the-hoff-dont-hassle-dF2w3l5gudW3C',
            'https://giphy.com/gifs/bachelorinparadise-bachelor-in-paradise-l0MYCLi5PQKMAjYg8',
            'https://giphy.com/gifs/decisions-CLq8NvXTdik0g',
            'https://giphy.com/gifs/u8G4WMEV2Y2Zi',
            'http://imgur.com/gallery/zQo6Eds',
            'https://giphy.com/gifs/reaction-tIKI2r0n8Btzq',
            'https://giphy.com/gifs/weird-what-the-fuck-jesus-christ-GlYqthjGTYGfC',
            'https://giphy.com/gifs/aatOCetGqsUTe',
            'http://i.imgur.com/nI8tvRj.gif',
            'http://i.imgur.com/hn82Em4.mp4',
            'http://i.imgur.com/XIb1vQ4.mp4',
            'http://i.imgur.com/lDBzN9K.mp4',
            'https://giphy.com/gifs/like-doing-ramp-CjA3bsrJTI3Ac',
            'https://giphy.com/gifs/baby-internet-vintage-14kqI3Y4urS3rG',
            'https://giphy.com/gifs/baby-scary-crying-HJTBvT7cTQqFq',
            'http://imgur.com/gallery/nDtyPnZ',
            'https://www.youtube.com/watch?v=gJLIiF15wjQ']
    threshold = 0.70
    print('Using built in defaults')


def create_run(urls, threshold):
    amount = str(len(urls)*(1/threshold))
    amount = int(float(amount))
    start = '''@echo off & setLocal EnableDelayedExpansion'''
    rand_amount = 'set /a RAND=%RANDOM% %%{}'.format(amount)
    exit = '''exit'''
    sentences = ''
    for i in range(len(urls)):
        if 'youtube' in urls[i]:
            sentence = "IF !RAND! == %s (start chrome %s)" % (i, urls[i])
            vbs = 'IF !RAND! == %s (vol.vbs)' % (i)
            space = '''
'''
            sentences = sentences+sentence+space+vbs+space
        else:
            sentence = "IF !RAND! == %s (start chrome %s)" % (i, urls[i])
            space = '''
'''
            sentences = sentences+sentence+space
    run = start+space+rand_amount+space+sentences+exit
    print('Run created!')
    return run


def save_run(run):
    run_location = os.path.join("c:\\", "dEkota", "run.bat")
    with open(run_location, "w") as text_file:
        text_file.write(run)
    print('Run saved')

run = create_run(urls, threshold)
time.sleep(1)
save_run(run)

def create_volumne():
    volumne = '''set WshShell = CreateObject("WScript.Shell")
WshShell.Run "%SystemRoot%\System32\SndVol.exe"
WScript.Sleep 1000
WshShell.AppActivate "Volume Mixer"
WshShell.SendKeys "{PGDN}" ' Turn the volume up by 20. If muted it will unmute it.
WshShell.SendKeys "{PGDN}" ' Turn the volume up by 20. If muted it will unmute it.
WshShell.SendKeys "{PGDN}" ' Turn the volume up by 20. If muted it will unmute it.
WshShell.SendKeys "{PGDN}" ' Turn the volume up by 20. If muted it will unmute it.
WshShell.SendKeys "{PGDN}" ' Turn the volume up by 20. If muted it will unmute it.
WshShell.SendKeys "{PGDN}" ' Turn the volume up by 20. If muted it will unmute it.
WshShell.SendKeys "{PGUP}" ' Turn the volume up by 20. If muted it will unmute it.
WshShell.SendKeys "{PGUP}" ' Turn the volume up by 20. If muted it will unmute it.
WshShell.SendKeys "{PGUP}" ' Turn the volume up by 20. If muted it will unmute it.
WshShell.SendKeys "{PGUP}" ' Turn the volume up by 20. If muted it will unmute it.
WshShell.SendKeys "%{F4}"  ' Alt+F4'''
    print('Volume made')
    return volumne

def save_volumne(volumne):
    vol_location = os.path.join("c:\\", "dEkota","vol.vbs")
    with open(vol_location, "w") as text_file:
        text_file.write(volumne)
    print('Volume saved')

volumne = create_volumne()
save_volumne(volumne)

def create_task():
    run_location = os.path.join("c:\\", "dEkota","run.bat")
    task = '''SchTasks /Create /tn "takemycup" /tr "{}" /sc HOURLY'''.format(run_location)
    call(task)
    print('Task created!')

create_task()
