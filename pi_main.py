import cv2
import pygame.mixer
from camera import camera
from block import block
from button import button
import audigo
import sender

def has_object(blocks):
  for b in blocks:
    if b.width is 2:
      return True
  return False

audigo.play('info-girl1-datawoyomikondeimasu1.mp3')

btn = button(24)
opt = block.option(0.9)
cam = camera((opt.camera_width, opt.camera_height))

audigo.play('info-girl1-kidoushimashita1.mp3')

try:
  while True:
    btn.wait_for_push()
    img = cam.get()
    if img is None or img.shape[0] is 0:
      print('failed to open image')
      quit()
    img = img[0:img.shape[0], img.shape[1]/3:img.shape[1]*2/3]
    try:
      blocks = block.calc(img, opt)
      # block.show_blocks(img, blocks)
      if has_object(blocks):
        audigo.play('info-girl1-start1.mp3')
        sender.post(blocks)
      else:
        audigo.play('info-girl1-bubu1.mp3')
    except cv2.error as e:
      print(e)
except KeyboardInterrupt:
  cam.close()
  btn.close()
  pygame.mixer.quit()