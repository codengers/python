'''This is used to back up the files. This program is for only windows.'''
import os
import time
source = ['C:\\Users\\Atika\\Downloads\\pdf\*.pdf']
target_dir = 'C:\\Users\\Atika\\Downloads\\Documents\\automation_backup'

if not os.path.exists(target_dir):
    os.mkdir(target_dir)
today = target_dir + os.sep + time.strftime('%Y%m%d')
now = time.strftime('%H%M%S')
target = today + os.sep + now + '.zip'
if not os.path.exists(today):
    os.mkdir(today)
    print('Successfully created directory : ', today)
zip_command = 'WZZIP -i {0} {1}'.format(target, ' '.join(source))
print('Zip command is : ')
print(zip_command)
print('Running : ')
if os.system(zip_command) == 0:
    print('Successfully backup to :', target)
else:
    print('Backup FAILED!')



