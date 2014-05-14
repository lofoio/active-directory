#!/usr/bin/env python2
# -*- coding:utf-8 -*-
class pipe_2(object):
    """双通管
    """

    def __init__(self, in_p):
        """

        Arguments:
        - `in_p`:进口压力
        - `out_p`:出口压力
        """
        self._in_p = in_p
        self._out_p = in_p


class valve(object):
    """活门
    """

    def __init__(self,in_p,out_p,threshold):
        """

        Arguments:
        - `in_p`:入口压
        - `out_p`:出口压
        - `threshold`:阈值
        """
        self._in_p = in_p
        self._out_p = out_p
        self._threshold = threshold

        if self._threshold < self._in_p-self._out_p:
            self._out_p=self._in_p-self._threshold

class hm_1(object):
    """HM-1
    """

    def __init__(self, in_p,out_p,p1,p2):
        """

        Arguments:
        - `in_p`:
        - `out_p`:
        - `p1`:
        - `p2`:
        """
        self._in_p = in_p
        self._out_p = out_p
        self._p1 = p1
        self._p2 = p2
