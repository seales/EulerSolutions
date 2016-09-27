use EulerMath;
use strict;
use warnings;

my $sum = 0;
foreach (1..999) {
  if ($_ % 3 == 0 || $_ % 5 == 0) {
    $sum += $_;
  }
}

print "Sum of all natural numbers divisible by 3 or 5 below 1000: $sum\n";
