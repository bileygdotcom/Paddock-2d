#!/usr/bin/env python

import level as l

segments = []
sprites  = []
name     = "02-02"

segments += l.add_straight(200, 0)
segments += l.add_corner(70, 110, 70, 8, l.last_y(segments),100)
segments += l.add_straight(100, l.last_y(segments))
segments += l.add_corner(140, 220, 140, 4, l.last_y(segments),50)
segments += l.add_corner(35, 55, 35, -12, l.last_y(segments),80)
segments += l.add_corner(35, 55, 35, -12, l.last_y(segments),50)
segments += l.add_corner(70, 110, 70, -4, l.last_y(segments),30)
segments += l.add_straight(200, l.last_y(segments))
segments += l.add_corner(70, 110, 70, -4, l.last_y(segments),20)
segments += l.add_straight(100, l.last_y(segments))
segments += l.add_corner(35, 55, 35, -8, l.last_y(segments))
segments += l.add_straight(200, l.last_y(segments))
segments += l.add_corner(35, 55, 35, -8, l.last_y(segments),40)
segments += l.add_corner(35, 55, 35, 12, l.last_y(segments))
segments += l.add_straight(200, l.last_y(segments))
segments += l.add_corner(70, 110, 70, -8, l.last_y(segments),80)
segments += l.add_straight(200, l.last_y(segments))
segments += l.add_corner(35, 55, 35, -12, l.last_y(segments),50)
segments += l.add_straight(400, l.last_y(segments))
segments += l.add_corner(70, 110, 70, -8, l.last_y(segments),0)

#segments += l.add_corner(30, 85, 40, 5, 0, 20)
#segments += l.add_hill(25, 25, 25, 0, l.last_y(segments))

l.write("/home/bileyg/SocieteTurbo_2d/SwervinMervin-changed/swervin_mervin/levels/tracks/{0}.csv".format(name), segments)
