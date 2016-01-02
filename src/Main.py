import argparse
import Browser_Actions
import Get_md5
import VLC_Action
import sys


def get_file_name():
    parser = argparse.ArgumentParser()
    parser.add_argument('filename')
    args = parser.parse_args()
    return args.filename

file_name = get_file_name()
md5 = Get_md5.get_hash(file_name)
sys.stdout.write('Successfully found the Hash of the File\n')
b = Browser_Actions.subtitle(file_name, md5)
b.get_subtitle()
sys.stdout.write('Successfully got the Subtitle\n')
v = VLC_Action.VLC(file_name)
sys.stdout.write('Opening the file in VLC Media Player\n')
