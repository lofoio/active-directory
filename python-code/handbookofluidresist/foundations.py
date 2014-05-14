#!/usr/bin/env python2
# -*- coding:utf-8 -*-
import math

def qorwoftpm(qw0,p0,t,p,m):
    """工作条件体积流量/流速
    qorwoftpm(qw0,p0,t,p,m)
    Arguments:
    - `qw0`:标准状态体积流量/流速
    - `p0`:标准状态压
    - `t`:工作温度
    - `p`:工作压
    - `m`:水蒸汽含量
    """
    return qw0*p0*t*(1.0+m/0.804)/(273.0*p)

def densoftpm(dens0,p0,t,p,m):
    """工作条件密度

    Arguments:
    - `dens0`:标准状态密度
    - `p0`:标准状态压
    - `t`:工作温度
    - `p`:工作压
    - `m`:水蒸汽含量
    """
    return 273.0*(dens0+m)*p/(t*p0*(1+m/0.804))
