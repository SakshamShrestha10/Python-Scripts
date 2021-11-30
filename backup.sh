#!/bin/bash

#tar -cvf /root/python/backup.tar /root/python

#Go to the backup folder location
#cd /root/python

#Show the size of the folder
#du -sh


file=/root/python/"backup_`date +%d`_`date +%m`_`date +%Y`.tar";
dest=/root/python
tar -cvf $file $dest


cd $dest
ls
du -sh

