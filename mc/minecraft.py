#!/usr/bin/python3
import shutil
import os
import time
import sys
import datetime


import argparse
parser = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawTextHelpFormatter)
parser.add_argument('cmd',
                    help="""Command to the minecraft server""", type=str, choices={"start", "stop", "status", "backup", "destroy", "check"})
parser.add_argument('--verbose',
                    help="""Print stuff when cmd=status (default = False)""", action='store_true')
args = parser.parse_args()

command = args.cmd

# Location of the Minecraft server installation.
minecraft_dir = '/path/to/mc/server'
worlds_dir = ['world', 'world_nether', 'world_the_end']


# Backup directory
backup_dir = '/path/to/mc/backup'
os.makedirs(backup_dir, exist_ok=True)

def server_command(cmd):
    os.system('screen -S minecraft -X stuff "{}\015"'.format(cmd))

def start():
    if not status():
        os.chdir(minecraft_dir)
        os.system('screen -dmS "minecraft" java -Xmx1024M -Xms1024M -jar server.jar nogui')
        print("START")
    else:
        print("ALREADY START")

def stop():
    if status():
        server_command('stop')
        print("STOP")
    else:
        print("ALREADY STOP")

def status():
    output = os.popen('screen -ls').read()
    if '.minecraft'  in output:
        if args.verbose: print("RUN")
        return True
    else:
        if args.verbose: print("NOT RUN")
        return False

def backup():
    if status():
        server_command('save-off')
        server_command('save-all')

    time.sleep(1)
    current_time = datetime.datetime.now()
    time_string = current_time.isoformat().replace(':', '.')
    time_string = str(time_string)[:19]
    print("COPYTREE")
    save_dir = f'{backup_dir}/{time_string}'
    os.mkdir(save_dir)
    for world in worlds_dir:
        shutil.copytree(f'{minecraft_dir}/{world}',f'{save_dir}/{world}')
    
    if status():
        server_command('save-on')
    print("OK")

def destroy():
    print('RMTREE')
    
    if status():
        print("CANT")
        quit()
        
    for world in worlds_dir:
        shutil.rmtree(f'{minecraft_dir}/{world}')
    print("OK")
    

def main():
    current_time = datetime.datetime.now()
    time_str = str(current_time)[5:16]
    if command == 'start':
        print(time_str)
        start()
    elif command == 'stop':
        print(time_str)
        stop()
    elif command == 'backup':
        print(time_str)
        backup()
    elif command == 'status':
        if args.verbose: print(time_str)
        status()
    elif command == 'destroy':
        print(time_str)
        destroy()
    elif command == 'check':
        if not status():
            print(time_str)
            backup()
            destroy()
            start()


if __name__ == "__main__":
    main()
