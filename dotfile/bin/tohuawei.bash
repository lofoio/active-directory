#!/usr/bin/env bash
# -*- coding:utf-8 -*-
if [ -z "$1" ]
then
#    ssh -p 2222 -i /home/lofoio/.ssh/id_dsa_fhd 192.168.0.101
    sftp -P 2222 -i /home/lofoio/.ssh/id_dsa_fhd 192.168.0.101:/sdcard
else
    scp -P 2222 -i /home/lofoio/.ssh/id_dsa_fhd  "$1"  192.168.0.101:/sdcard
fi
