#!/usr/bin/env perl

use EulerMath;
use strict;
use warnings;

my $val = 600851475143;
my @factors = EulerMath::factors($val);

my $largest_prime = -1;
for (@factors) {
  if (EulerMath::is_prime($_) && $_ > $largest_prime) {
    $largest_prime = $_;
  }
}

print "Largest prime factor of $val is $largest_prime\n";
