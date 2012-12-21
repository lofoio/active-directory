#!/bin/bash
ip link set wlan0 up \
&& iw dev wlan0 connect -w TP-LINK_2D4E02 key 0:89121ABABA
#dhcpcd wlan0
