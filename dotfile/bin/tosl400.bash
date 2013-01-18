#!/usr/bin/env bash
# -*- coding:utf-8 -*-
if [ -z "$1" ]
then
    sftp -i /home/wangdian/.ssh/id_ecdsa_wdsl400 192.168.1.100
else
    scp  -i /home/wangdian/.ssh/id_ecdsa_wdsl400  "$1"  192.168.1.100
fi
