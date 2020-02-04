from urllib.robotparser import RobotFileParser

rp1 = RobotFileParser()
rp1.set_url('http://www.jianshu.com/robots.txt')
rp1.read()
print(rp1.can_fetch('*', 'http://www.jianshu.com/p/b67554025d7d'))

rp2 = RobotFileParser()
rp2.set_url('http://www.hdu.edu.cn/robots.txt')
rp2.read()
print(rp2.can_fetch('*', 'http://www.hdu.edu.cn/news/important_26928'))

c=input()
