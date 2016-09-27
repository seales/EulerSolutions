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


1;
