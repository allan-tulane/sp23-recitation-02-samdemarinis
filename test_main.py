from main import *

def test_simple_work():
  assert simple_work_calc(10, 2, 2) == 56
  assert simple_work_calc(20, 3, 2) == 506.75
  assert simple_work_calc(30, 4, 2) == 1954
  assert simple_work_calc(50, 2, 2) == 364
  assert simple_work_calc(30, 2, 2) == 182
  assert simple_work_calc(75, 4, 2) == 25909

def test_work():
  assert work_calc(10, 2, 2, lambda n: 1) == 31
  assert work_calc(20, 1, 2, lambda n: n*n) == 533.8125
  assert work_calc(30, 3, 2, lambda n: n) == 638.625
  assert work_calc(10, 2, 2, lambda n: n*n) == 203.5
  assert work_calc(60, 2, 2, lambda n: n*n*n) == 287993.6875
  assert work_calc(40, 1, 2, lambda n: n+n) == 158.5