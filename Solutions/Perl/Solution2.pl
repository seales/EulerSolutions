use EulerMath;
use strict;
use warnings;

my $upper_bound = 4000000; # four million

my $sum_of_evens = 0;
foreach (&EulerMath::fibonacci_values_less_than_or_equal_to_n($upper_bound)) {
  if (&EulerMath::is_even($_)) {
    print "After $_, sum of evens: $sum_of_evens\n";
    $sum_of_evens += $_;
  }
}

print "Sum of even fibonacci numbers below 4million: $sum_of_evens\n";
