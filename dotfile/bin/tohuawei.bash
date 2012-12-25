#!/usr/bin/env bash
# -*- coding:utf-8 -*-
if [ -z "$1" ]
then
    sftp -i /home/wangdian/.ssh/id_dsa_hw  root@huawei:/sdcard
else
    scp  -i /home/wangdian/.ssh/id_dsa_hw  "$1"  root@huawei:/sdcard
fi
