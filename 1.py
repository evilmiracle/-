#!/usr/bin/python
# -*- coding: UTF-8 -*-

from random import randint
# rock = 石头  scissor = 剪刀  paper = 布
def rsp():
	user = int(input('you choice in number:1 rock,2 scissor,3 paper:'))
	comp = randint(1,3)
	if user == 1:
		u = 'rock'
	if user == 2:
		u = 'scissor'
	if user == 3:
		u = 'paper'
	if comp == 1:
		c = 'rock'
	if comp == 2:
		c = 'scissor'
	if comp == 3:
		c = 'paper'
	if comp == user:
		print 'You have %s and the computer have %s too.The same' % (u,c)
	else:
		if user == comp+2 or user ==  comp-1:
			print 'You have %s and the computer have %s.You win!' % (u,c)
		else:
			print 'You have %s and the computer have %s. you lose!' % (u,c)
			return rsp()


rsp()
