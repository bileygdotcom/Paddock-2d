#!/usr/bin/env python

import level as l

segments = []
sprites  = []
name     = "02-01"

segments += l.add_straight(525, 0)
segments += l.add_corner(140, 220, 140, -4, l.last_y(segments))
segments += l.add_straight(315, l.last_y(segments))
segments += l.add_corner(70, 110, 70, 8, l.last_y(segments))
segments += l.add_corner(70, 110, 70, 8, l.last_y(segments))
segments += l.add_corner(70, 110, 70, 8, l.last_y(segments))
#segments += l.add_hill(50, 50, 50, 5, l.last_y(segments))
segments += l.add_straight(360, l.last_y(segments))
#segments += l.add_hill(50, 50, 50, -5, l.last_y(segments))
segments += l.add_straight(800, l.last_y(segments))
segments += l.add_corner(70, 110, 70, -8, l.last_y(segments))
segments += l.add_corner(140, 220, 140, -4, l.last_y(segments),0)

#segments += l.add_corner(30, 85, 40, 5, 0, 20)
#segments += l.add_hill(25, 25, 25, 0, l.last_y(segments))

l.write("/home/bileyg/SocieteTurbo_2d/SwervinMervin-changed/swervin_mervin/levels/tracks/{0}.csv".format(name), segments)
