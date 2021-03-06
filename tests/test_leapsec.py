# mpcformat/tests/test_leapsec.py

# Third-party imports
import novas.compat as novas

# Import the specific package/module/function we are testing
import mpcformat.leapsec as leapsec

def test_leap():
    """example from leap-seconds.list"""
    l = leapsec.LeapSeconds()
    jd9 = novas.julian_date(1972, 6, 30, 23 + (3599. / 3600))
    assert l.getLeapSeconds(jd9) == 10
    jd0 = novas.julian_date(1972, 7, 1, 0)
    assert l.getLeapSeconds(jd0) == 11
