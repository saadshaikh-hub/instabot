from instapy import Instapy

session =InstaPy(username="username", password="password")
session. login()

#following section

session.set_do_follow=False, percentage-90, times=1)

#Comment section

session.set_do_coment(True, percentage-90) session.set_comments([u'nice one @{}!'])
 
#like section

session.like_by_tags(['freelancing', 'needwebsite', 'workfromhome'] ,amount=100)

sension.set_dont_like(("naked", "nafw", "sex")

session.end()
