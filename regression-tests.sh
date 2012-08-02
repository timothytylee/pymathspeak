#!/bin/sh
#
cd `dirname $0`/mathml
for n in 01 02 03 04 05 06 07 08 09 10 11 12 13 14 15; do
    ../test-mathspeak "MathSpeak Chapter $n.xml" |diff - "ch$n.out.ref"
done
for n in simplePres; do
    ../test-mathspeak "W3C MathML 3 Test - $n.mml" |diff - "$n.out.ref"
done
