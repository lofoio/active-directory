#!/usr/bin/env bash
# -*- coding:utf-8 -*-
sudo scp -i /root/.ssh/id_dsa_hw  "$1"  root@huawei:/sdcard
