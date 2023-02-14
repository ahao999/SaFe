import os,time,sys

print('开始录制信号,请等待8秒…………')
os.system('hackrf_transfer -r lab.raw -f 434015700 -g 16 -l 32 -a 1 -s 8000000 -b 400000')

time.sleep(8)
print('开始重放信号：')
os.system('hackrf_transfer -t lab.raw -f 434015700 -x 47 -a 1 -s 8000000 -b 4000000')


