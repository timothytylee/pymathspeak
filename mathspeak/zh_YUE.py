#-*- encoding: utf-8 -*-
#
#MathSpeak localization for zh_YUE, which currently maps to zh_TW
#
#This file is covered by the GNU General Public License.
#See licence.txt for more details.
#Copyright 2012-2016 World Light Information Limited and Hong Kong Blind Union.


from . import zh_TW


class MathSpeak(zh_TW.MathSpeak):

	locale=u"zh_YUE"

	def __init__(self):
		zh_TW.MathSpeak.__init__(self)

	def _createNode(self):
		return zh_TW.MathSpeakNode()


# vim: set tabstop=4 shiftwidth=4:
