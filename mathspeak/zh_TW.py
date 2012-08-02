#-*- encoding: utf-8 -*-
#
#MathSpeak localization for Traditional Chinese
#
#This file is covered by the GNU General Public License.
#See the file COPYING for more details.
#Copyright 2012 World Light Information Limited and Hong Kong Blind Union.


import _core


_core.VARIANT_DICT.update({
	"bold":        {None:u"粗體"},
	"italic":      {None:u"斜體"},
	"bold-italic": {None:u"粗斜體"},
	"fraktur":     {None:u"哥德體"},
	"bold-fraktur":{None:u"粗哥德體"},
	})


_core.LABEL_DICT.update({
	"number":     {None:u"數值"},
	"row":        {None:u"行"},
	"column":     {None:u"列"},
	"error":      {None:u"錯誤"},
	"capital":    {None:u"大楷"},
	"capword":    {None:u"大楷詞語"},
	"positive":   {None:u"正"},
	"negative":   {None:u"負"},
	"start":      {None:u"開始"},
	"end":        {None:u"結束"},
	"script":     {None:u"標"},
	"scriptclose":{None:u"標"},
	"scriptend":  {None:u"結束標示"},
	"under":      {None:u"底"},
	"over":       {None:u"頂"},
	"above":      {None:u"頂部"},
	"below":      {None:u"底部"},
	"baseline":   {None:u"基線"},
	"super":      {None:u"上"},
	"sub":        {None:u"下"},
	"string":     {None:u"字串"},
	"blank":      {None:u"空白"},
	"layout":     {None:u"佈局"},
	"enlarged":   {None:u"擴大"},
	"matrix":     {None:u"矩陣"},
	"determinant":{None:u"行列式"},
	"binomial":   {None:u"Binomial或矩陣"},
	"choose":     {None:u"選"},
	"absolute":   {None:u"絕對值"},
	"modifying":  {None:u"更改"},
	"each":       {None:u"每個"},
	"with":       {None:u"標示"},
	"by":         {None:u"乘"},
	"point":      {None:u"點"},
	"and":        {None:u"又"},
	"..":         {None:u"兩點"},
	"once":       {None:u"1"},
	"twice":      {None:u"2"},
	"fracnest":   {None:u"嵌套"},
	"fracover":   {None:u"除"},
	"frac":       {None:u"分數"},
	"rootnest":   {None:u"嵌套"},
	"rootindex":  {None:u"方根"},
	"rootstart":  {None:u"開始方根"},
	"rootend":    {None:u"結束方根"},
	"squared":    {None:u"平方"},
	"cubed":      {None:u"立方"},
	"cancel":     {None:u"刪除"},
	"cancelwith": {None:u"改為"},
	"set":        {None:u"集合"},
	})


_core.IDENTIFIER_DICT.update({
	u"\u221e":{None:u"無限"},
	"lim":    {None:u"極限"},
	"ln":     {None:u"自然對數"},
	"log":    {None:u"對數"},
	"sin":    {None:u"正弦"},
	"cos":    {None:u"餘弦"},
	"tan":    {None:u"正切"},
	"cot":    {None:u"餘切"},
	"sec":    {None:u"正割"},
	"csc":    {None:u"餘割"},
	"asin":   {None:u"反正弦"},
	"acos":   {None:u"反餘弦"},
	"atan":   {None:u"反正切"},
	"acot":   {None:u"反餘切"},
	"asec":   {None:u"反正割"},
	"acsc":   {None:u"反餘割"},
	"arcsin": {None:u"反正弦"},
	"arccos": {None:u"反餘弦"},
	"arctan": {None:u"反正切"},
	"arccot": {None:u"反餘切"},
	"arcsec": {None:u"反正割"},
	"arccsc": {None:u"反餘割"},
	})


_core.OPERATOR_DICT.update({
	"=":      {None:u"等於"},
	",":      {None:u"逗號"},
	".":      {None:u"句號"},
	":":      {None:u"冒號"},
	";":      {None:u"分號"},
	"+":      {None:u"加"},
	"-":      {None:u"減"},
	"#":      {None:u"井號"},
	"$":      {None:u"錢號"},
	"<":      {None:u"細於"},
	">":      {None:u"大於"},
	"~":      {None:u"波浪線"},
	"^":      {None:u"hat"},
	"_":      {None:u"low-line"},
	"|":      {None:u"垂直線"},
	"{":      {None:u"左大括號"},
	"}":      {None:u"右大括號"},
	"[":      {None:u"左方括號"},
	"]":      {None:u"右方括號"},
	"(":      {None:u"左括號"},
	")":      {None:u"右括號"},
	u"\u00af":{None:u"伸展線"},
	u"\u00b1":{None:u"加或減"},
	u"\u00b7":{None:u"點"},
	u'\u00d7':{None:u"乘"},
	u"\u00f7":{None:u"除"},
	u"\u02d9":{None:u"點"},
	u"\u2016":{None:u"雙重垂直線"},
	u"\u2018":{None:u"開單括號"},
	u"\u2019":{None:u"關單括號"},
	u"\u201c":{None:u"開雙括號"},
	u"\u201d":{None:u"關雙括號"},
	u"\u2026":{None:u"省略號"},
	u"\u2032":{None:u"prime"},
	u"\u2033":{None:u"雙重 prime"},
	u"\u2034":{None:u"三重 prime"},
	u"\u2038":{None:u"caret"},
	u"\u2061":{None:u""},
	u"\u2062":{None:u"乘"},
	u"\u2063":{None:u"逗號"},
	u"\u2107":{None:u"歐拉常數"},
	u"\u210e":{None:u"普朗克常數"},
	u"\u210f":{None:u"約化普朗克常數"},
	u"\u2135":{None:u"alef 無限"},
	u"\u2190":{None:u"左箭頭"},
	u"\u2191":{None:u"上箭頭"},
	u"\u2192":{None:u"右箭頭"},
	u"\u2193":{None:u"下箭頭"},
	u"\u2207":{None:u"倒三角算子"},
	u"\u2208":{None:u"元素"},
	u"\u2209":{None:u"非元素"},
	u"\u220a":{None:u"元素"},
	u"\u220b":{None:u"contains-member"},
	u"\u220c":{None:u"does-not-contain-member"},
	u"\u220d":{None:u"contains-member"},
	u"\u220e":{None:u"end-of-proof"},
	u"\u220f":{None:u"求積"},
	u"\u2210":{None:u"上積"},
	u"\u2211":{None:u"求和"},
	u"\u2212":{None:u"減"},
	u"\u2213":{None:u"減或加"},
	u"\u2214":{None:u"點加"},
	u"\u2215":{None:u"除"},
	u"\u2216":{None:u"減子集"},
	u"\u2217":{None:u"星號"},
	u"\u2218":{None:u"環形"},
	u"\u2219":{None:u"項目符號"},
	u"\u221a":{None:u"平方根"},
	u"\u221b":{None:u"立方根"},
	u"\u221c":{None:u"四次方根"},
	u"\u221d":{None:u"成正比"},
	u"\u221f":{None:u"直角"},
	u"\u2220":{None:u"角"},
	u"\u2221":{None:u"測量角"},
	u"\u2222":{None:u"球面角"},
	u"\u2223":{None:u"分隔"},
	u"\u2224":{None:u"不分隔"},
	u"\u2225":{None:u"平行"},
	u"\u2226":{None:u"非平行"},
	u"\u2227":{None:u"邏輯和"},
	u"\u2228":{None:u"邏輯或"},
	u"\u2229":{None:u"焦集"},
	u"\u222a":{None:u"聯集"},
	u"\u222b":{None:u"積分"},
	u"\u222c":{None:u"雙重積分"},
	u"\u222d":{None:u"三重積分"},
	u"\u222e":{None:u"線積分"},
	u"\u222f":{None:u"雙重線積分"},
	u"\u2230":{None:u"volume-integral"},
	u"\u2231":{None:u"順時針積分"},
	u"\u2232":{None:u"順時針線積分"},
	u"\u2233":{None:u"逆時針線積分"},
	u"\u2234":{None:u"所以"},
	u"\u2235":{None:u"因為"},
	u"\u2236":{None:u"比"},
	u"\u2237":{None:u"比例"},
	u"\u2238":{None:u"點減"},
	u"\u2239":{None:u"excess"},
	u"\u223a":{None:u"幾何成正比"},
	u"\u223b":{None:u"homothetic-to"},
	u"\u223c":{None:u"波浪號"},
	u"\u2243":{None:u"漸近相等"},
	u"\u2244":{None:u"非漸近相等"},
	u"\u2245":{None:u"大約等於"},
	u"\u2246":{None:u"大約但不等於"},
	u"\u2247":{None:u"非大約亦非等於"},
	u"\u2248":{None:u"幾乎等於"},
	u"\u2249":{None:u"不幾乎等於"},
	u"\u224a":{None:u"幾乎等於或等於"},
	u"\u224c":{None:u"全部等於"},
	u"\u224d":{None:u"相等"},
	u"\u224e":{None:u"幾何相等"},
	u"\u224f":{None:u"相差"},
	u"\u2250":{None:u"趨向極限"},
	u"\u2251":{None:u"幾何等於"},
	u"\u2252":{None:u"大約等於或是影像"},
	u"\u2253":{None:u"是影像或大約等於"},
	u"\u2254":{None:u"冒號等於"},
	u"\u2255":{None:u"等於冒號"},
	u"\u2260":{None:u"不等於"},
	u"\u2264":{None:u"小於或等於"},
	u"\u2265":{None:u"大於或等於"},
	u"\u22ee":{None:u"垂直省略號"},
	u"\u22ef":{None:u"省略號"},
	u"\u22f0":{None:u"右上斜省略號"},
	u"\u22f1":{None:u"右下斜省略號"},
	u"\u2308":{None:u"左上捨入"},
	u"\u2309":{None:u"右上捨入"},
	u"\u230a":{None:u"左下捨入"},
	u"\u230b":{None:u"右下捨入"},
	u"\u2a2f":{None:u"叉"},
	})


class MathSpeakNode(_core.MathSpeakNode):

	def __init__(self):
		_core.MathSpeakNode.__init__(self)

	def _ordinalAbbrev(self,idx):
		return u"第 "+str(idx)

	def _mergeNumericFraction(self):
		if not self[0]._isNumber():  return
		if not self[1]._isNumber():  return
		self.text=" ".join((self[1].text,u"分",self[0].text))


class MathSpeak(_core.MathSpeak):

	locale="zh_TW"

	def __init__(self):
		_core.MathSpeak.__init__(self)

	def _createNode(self):
		return MathSpeakNode()


# vim: set tabstop=4 shiftwidth=4:
