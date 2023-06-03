#/bin/bash

new_alias="alias serialize='python3 util.py '"

echo $new_alias >> ~/.bashrc
. ~/.bashrc