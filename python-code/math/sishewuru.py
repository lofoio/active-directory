#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Decimal(2.675) is not Decimal("2.675") because the 2.675 read here is exactly '2.67499999999999982236431605997495353221893310546875' but "2.675". Watch for the trap.
from decimal import Decimal
n = Decimal('2.675')
print(round(n, 2),round(2.675,2))
