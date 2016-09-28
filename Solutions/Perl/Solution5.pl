#!/usr/bin/env perl

use EulerMath;
use strict;
use warnings;

=Calculations

Multiples of the below-listed numbers can
result in any number between 1 and 20.

20 -> 2 * 2 * 5
19 -> 19
17 -> 17
13 -> 13
11 -> 11
7 -> 7
6 -> 2 * 3
3 -> 3
2 -> 2
=cut

my $product = 2 * 3 * 6 * 7 * 11 * 13 * 17 * 19 * 20;

print "Smallest positive number divisible by all",
    " numbers between 1 and 20: $product\n";
