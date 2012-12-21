#!/bin/bash
pacman -Qei | awk '/^Name/ { name=$3 } /^Groups/ { if ( $3 != "base" && $3 != "base-devel" && $3 != "xfce4" && $3 != "xfce4-goodies" && $3 != "xorg" ) { print name } }'
