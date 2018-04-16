#!/bin/bash

src_ip="10.8.0.10"
src_user="root"
src_path="/home/openflow/quan/netfpga/bitfiles/"
dst_path="./"
SCRIPT_PATH="./"
include_path="include-list.txt"

# Functions
# Read src_ip
read_src_ip()
{
	read -p "Enter the SRC IP: " src_ip
}

# Print src_ip
print_src_ip()
{
	echo "src_ip: $src_ip"
}

# Read directory scripts is in.
read_path()
{
	# Absolute path to this script, e.g. /home/user/bin/foo.sh
	SCRIPT=$(readlink -f "$0")
	# Absolute path this script is in, thus /home/user/bin
	SCRIPT_PATH=$(dirname "$SCRIPT")
	echo $SCRIPT_PATH
}

# Rsync
sync_directory()
{
	rsync -avz --include-from "$include_path" --exclude='*' $src_user@$src_ip:$src_path $dst_path
}


echo 'Have a lot of fun!'

# echo 'Command line options'
# Options
while [ "$1" != "" ]; do
	case $1 in
		-c | --custom ) 	# TODO:
					read_src_ip
					;;
		-h | --host )		shift
					src_ip=$1
					;;
		-u | --user )		shift
					src_user=$1
					;;
		-s | --source )		shift
					src_path=$1
					;;
		-d | --destination )	shift
					dst_path=$1
					;;
		-i | --include )	shift
					include_path=$1
					;;
		--help )		# usage
					exit
					;;
		* )			# usage
					exit
	esac
	shift
done


sync_directory


