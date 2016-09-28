#!/usr/bin/env perl

use EulerMath;
use strict;
use warnings;

my $largest_palindrome = -1;

for (my $i = 100; $i < 1000; $i++) {
  for (my $j = $i; $j < 1000; $j++) {
    my $product = $i*$j;
    if (&EulerMath::is_palindrome($product . "")
          && $product > $largest_palindrome) {

        $largest_palindrome = $product;
    }
  }
}

print "Largest palindrome from product",
    " of two 3-digit numbers: $largest_palindrome\n";
