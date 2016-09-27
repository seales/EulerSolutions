#!/usr/bin/env perl

package EulerMath;
use strict;
use warnings;

sub first_n_fibonacci_values {
  my $n = $_[0];
  my $f1 = 0;
  my $f2 = 1;

  my @fibonacci_sequence;

  while ($n > 0) {
    $f2 = $f1 + $f2;
    $f1 = $f2 - $f1;
    $n -= 1;

    push(@fibonacci_sequence, $f2);
  }

  @fibonacci_sequence;
}

sub fibonacci_values_less_than_or_equal_to_n {
  my $n = $_[0];
  my $f1 = 0;
  my $f2 = 1;

  my @fibonacci_sequence;

  while ($f2 <= $n) {
    $f2 = $f1 + $f2;
    $f1 = $f2 - $f1;

    push(@fibonacci_sequence, $f2);
  }

  @fibonacci_sequence;
}

sub nth_fibonacci {
  my $n = $_[0];
  my $f1 = 0;
  my $f2 = 1;

  while ($n > 0) {
    $f2 = $f1 + $f2;
    $f1 = $f2 - $f1;
    $n -= 1;
  }

  $f2;
}

sub is_even {
  $_[0] % 2 == 0;
}

sub is_odd {
  not(is_even($_[0]));
}

sub is_prime {
  my $val = $_[0];

  if ($val <= 1) {
    return 0; # a prime, by def, must be greater than one
  }

  my $div = int(sqrt($val));  # initialize with largest possible divisor

  while ($div > 1) {

    if ($val % $div == 0) {
      return 0;  # val has divisor
    }

    $div -= 1;
  }

  1;  # value has no divisor
}

sub factors {
  my $val = $_[0];

  my $div = int(sqrt($val));  # initialize with largest possible divisor
  my %factors;

  while ($div > 0) {

    if ($val % $div == 0) {
      my $factor1 = $div;
      my $factor2 = $val / $div;

      if (not(exists($factors{$factor1}))) {
        $factors{$factor1} = 1;
      }

      if (not(exists($factors{$factor2}))) {
        $factors{$factor2} = 1;
      }
    }

    $div -= 1;
  }

  sort {$a <=> $b} (keys %factors);
}

1;
