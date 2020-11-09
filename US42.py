from datetime import datetime

def reject_illegal_dates(date: datetime) -> bool:

    month, day, year = date.split('/')
    try:
        if datetime(int(year), int(month), int(day)):
            return True
    except ValueError:
        return False

#def test_reject_illegal_dates(self):
#        """ Test cases for US42 --- Reject Illegal date"""
#       self.assertTrue(us.reject_illegal_dates('2/10/2020'), True)
#       self.assertTrue(us.reject_illegal_dates('6/30/2020'), True)

#       self.assertFalse(us.reject_illegal_dates('2/30/2020'), False)
#       self.assertFalse(us.reject_illegal_dates('6/32/2020'), False)
