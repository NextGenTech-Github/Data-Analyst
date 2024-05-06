# pip install speedtest

import speedtest

d_speed = speedtest.Speedtest()

print('Download speed: ' + f'{d_speed.download()/8000000:.2f}mb')

print('Upload speed: ' + f'{d_speed.upload()/8000000:.2f}mb')


