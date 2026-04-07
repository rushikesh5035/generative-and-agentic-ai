# Collection in python 

# import arrow

# brewing_time = arrow.utcnow()
# brewing_time.to('Asia/Kolkata').format('YYYY-MM-DD HH:mm:ss')
# print(brewing_time)

from collections import namedtuple
chaiprofile = namedtuple('ChaiProfile', ['name', 'milk', 'sugar', 'brewing_time'])

print(chaiprofile)