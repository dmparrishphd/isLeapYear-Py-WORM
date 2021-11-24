def isLeapYear (year):
    assert isinstance(year, int)
    return \
        True  if not year % 400 else \
        False if not year % 100 else \
        True  if not year %   4 else \
        False
  
