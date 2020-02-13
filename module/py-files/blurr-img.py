import cv2, sys
lines = sys.stdin.readline().replace('\n','')
line_list=lines.split(',')
import os
cwd = os.getcwd()

try:
  image = cv2.imread(cwd+'/'+line_list[0])
  blurred = cv2.GaussianBlur(image, (11, 11), 0)
  cv2.imwrite(cwd+'/'+line_list[2]+'/'+line_list[1]+line_list[3], blurred)
  print(True)
except:
  print(False)