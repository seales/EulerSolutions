#!/usr/bin/env perl

use EulerMath;

use strict;
use warnings;
use Test::More;

ok(&EulerMath::is_prime(3), "3 is prime");
ok(not(&EulerMath::is_prime(8)), "8 is not prime");

done_testing();
