if [ ! -p /dev/shm/mfifo ]
then
echo "Creating mfifo ..... "
su -c "mkfifo -m 666 /dev/shm/mfifo" && echo "mfifo done" || exit
fi
if [ ! -p /dev/shm/ififo ]
then
echo "Creating ififo ..... "
su -c "mkfifo -m a=rw /dev/shm/ififo" && echo "ififo done" || exit
fi
echo "Playing $1 ..... "
mplayer -ao alsa -loop 0 $1 -msglevel all=4 -input file=/dev/shm/mfifo \
| while read a
do [ "${a//ANS/}" != "$a" ] && echo $a>/dev/shm/ififo 
done
