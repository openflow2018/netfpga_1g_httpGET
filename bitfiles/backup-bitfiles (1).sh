#!/bin/bash

# Absolute path to this script, e.g. /home/user/bin/foo.sh
SCRIPT=$(readlink -f "$0")
# Absolute path this script is in, thus /home/user/bin
SCRIPT_PATH=$(dirname "$SCRIPT")
# echo $SCRIPT_PATH

rsync_script_path=$(readlink -f "$SCRIPT_PATH/../utils/rsync_scripts.sh")

include_file="include-list.txt"
include_path="$SCRIPT_PATH/$include_file"

# 
src_netfpga="/home/openflow/quan/netfpga"

dst_path="$SCRIPT_PATH/"
src_path="$src_netfpga/bitfiles/"

src_ip="10.8.0.10"

echo "dst_path: $dst_path"
echo "src_path: $src_path"
echo "include_path: $include_path"

# echo 'Command line options'
# Options
while [ "$1" != "" ]; do
	case $1 in
		-h | --host )		shift
					src_ip=$1
					;;
		--help )		usage
					exit
					;;
		* )			usage
					exit
	esac
	shift
done

/bin/bash "$rsync_script_path" -h $src_ip -d $dst_path -s $src_path -i $include_path


