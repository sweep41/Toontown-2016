'''tzinfo timezone information for Africa/Tunis.'''
from pytz.tzinfo import DstTzInfo
from pytz.tzinfo import memorized_datetime as d
from pytz.tzinfo import memorized_ttinfo as i

class Tunis(DstTzInfo):
    '''Africa/Tunis timezone definition. See datetime.tzinfo for details'''

    zone = 'Africa/Tunis'

    _utc_transition_times = [
d(1,1,1,0,0,0),
d(1911,3,10,23,50,39),
d(1939,4,15,22,0,0),
d(1939,11,18,22,0,0),
d(1940,2,25,22,0,0),
d(1941,10,5,22,0,0),
d(1942,3,8,23,0,0),
d(1942,11,2,1,0,0),
d(1943,3,29,1,0,0),
d(1943,4,17,0,0,0),
d(1943,4,25,1,0,0),
d(1943,10,4,0,0,0),
d(1944,4,3,1,0,0),
d(1944,10,7,22,0,0),
d(1945,4,2,1,0,0),
d(1945,9,15,22,0,0),
d(1977,4,29,23,0,0),
d(1977,9,23,23,0,0),
d(1978,4,30,23,0,0),
d(1978,9,30,23,0,0),
d(1988,5,31,23,0,0),
d(1988,9,24,23,0,0),
d(1989,3,25,23,0,0),
d(1989,9,23,23,0,0),
d(1990,4,30,23,0,0),
d(1990,9,29,23,0,0),
d(2005,4,30,23,0,0),
d(2005,9,30,0,0,0),
d(2006,3,26,1,0,0),
d(2006,10,29,1,0,0),
d(2007,3,25,1,0,0),
d(2007,10,28,1,0,0),
d(2008,3,30,1,0,0),
d(2008,10,26,1,0,0),
d(2009,3,29,1,0,0),
d(2009,10,25,1,0,0),
d(2010,3,28,1,0,0),
d(2010,10,31,1,0,0),
d(2011,3,27,1,0,0),
d(2011,10,30,1,0,0),
d(2012,3,25,1,0,0),
d(2012,10,28,1,0,0),
d(2013,3,31,1,0,0),
d(2013,10,27,1,0,0),
d(2014,3,30,1,0,0),
d(2014,10,26,1,0,0),
d(2015,3,29,1,0,0),
d(2015,10,25,1,0,0),
d(2016,3,27,1,0,0),
d(2016,10,30,1,0,0),
d(2017,3,26,1,0,0),
d(2017,10,29,1,0,0),
d(2018,3,25,1,0,0),
d(2018,10,28,1,0,0),
d(2019,3,31,1,0,0),
d(2019,10,27,1,0,0),
d(2020,3,29,1,0,0),
d(2020,10,25,1,0,0),
d(2021,3,28,1,0,0),
d(2021,10,31,1,0,0),
d(2022,3,27,1,0,0),
d(2022,10,30,1,0,0),
d(2023,3,26,1,0,0),
d(2023,10,29,1,0,0),
d(2024,3,31,1,0,0),
d(2024,10,27,1,0,0),
d(2025,3,30,1,0,0),
d(2025,10,26,1,0,0),
d(2026,3,29,1,0,0),
d(2026,10,25,1,0,0),
d(2027,3,28,1,0,0),
d(2027,10,31,1,0,0),
d(2028,3,26,1,0,0),
d(2028,10,29,1,0,0),
d(2029,3,25,1,0,0),
d(2029,10,28,1,0,0),
d(2030,3,31,1,0,0),
d(2030,10,27,1,0,0),
d(2031,3,30,1,0,0),
d(2031,10,26,1,0,0),
d(2032,3,28,1,0,0),
d(2032,10,31,1,0,0),
d(2033,3,27,1,0,0),
d(2033,10,30,1,0,0),
d(2034,3,26,1,0,0),
d(2034,10,29,1,0,0),
d(2035,3,25,1,0,0),
d(2035,10,28,1,0,0),
d(2036,3,30,1,0,0),
d(2036,10,26,1,0,0),
d(2037,3,29,1,0,0),
d(2037,10,25,1,0,0),
        ]

    _transition_info = [
i(540,0,'PMT'),
i(3600,0,'CET'),
i(7200,3600,'CEST'),
i(3600,0,'CET'),
i(7200,3600,'CEST'),
i(3600,0,'CET'),
i(7200,3600,'CEST'),
i(3600,0,'CET'),
i(7200,3600,'CEST'),
i(3600,0,'CET'),
i(7200,3600,'CEST'),
i(3600,0,'CET'),
i(7200,3600,'CEST'),
i(3600,0,'CET'),
i(7200,3600,'CEST'),
i(3600,0,'CET'),
i(7200,3600,'CEST'),
i(3600,0,'CET'),
i(7200,3600,'CEST'),
i(3600,0,'CET'),
i(7200,3600,'CEST'),
i(3600,0,'CET'),
i(7200,3600,'CEST'),
i(3600,0,'CET'),
i(7200,3600,'CEST'),
i(3600,0,'CET'),
i(7200,3600,'CEST'),
i(3600,0,'CET'),
i(7200,3600,'CEST'),
i(3600,0,'CET'),
i(7200,3600,'CEST'),
i(3600,0,'CET'),
i(7200,3600,'CEST'),
i(3600,0,'CET'),
i(7200,3600,'CEST'),
i(3600,0,'CET'),
i(7200,3600,'CEST'),
i(3600,0,'CET'),
i(7200,3600,'CEST'),
i(3600,0,'CET'),
i(7200,3600,'CEST'),
i(3600,0,'CET'),
i(7200,3600,'CEST'),
i(3600,0,'CET'),
i(7200,3600,'CEST'),
i(3600,0,'CET'),
i(7200,3600,'CEST'),
i(3600,0,'CET'),
i(7200,3600,'CEST'),
i(3600,0,'CET'),
i(7200,3600,'CEST'),
i(3600,0,'CET'),
i(7200,3600,'CEST'),
i(3600,0,'CET'),
i(7200,3600,'CEST'),
i(3600,0,'CET'),
i(7200,3600,'CEST'),
i(3600,0,'CET'),
i(7200,3600,'CEST'),
i(3600,0,'CET'),
i(7200,3600,'CEST'),
i(3600,0,'CET'),
i(7200,3600,'CEST'),
i(3600,0,'CET'),
i(7200,3600,'CEST'),
i(3600,0,'CET'),
i(7200,3600,'CEST'),
i(3600,0,'CET'),
i(7200,3600,'CEST'),
i(3600,0,'CET'),
i(7200,3600,'CEST'),
i(3600,0,'CET'),
i(7200,3600,'CEST'),
i(3600,0,'CET'),
i(7200,3600,'CEST'),
i(3600,0,'CET'),
i(7200,3600,'CEST'),
i(3600,0,'CET'),
i(7200,3600,'CEST'),
i(3600,0,'CET'),
i(7200,3600,'CEST'),
i(3600,0,'CET'),
i(7200,3600,'CEST'),
i(3600,0,'CET'),
i(7200,3600,'CEST'),
i(3600,0,'CET'),
i(7200,3600,'CEST'),
i(3600,0,'CET'),
i(7200,3600,'CEST'),
i(3600,0,'CET'),
i(7200,3600,'CEST'),
i(3600,0,'CET'),
        ]

Tunis = Tunis()

