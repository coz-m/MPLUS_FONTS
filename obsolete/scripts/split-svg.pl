#!/usr/bin/perl

use strict;
use File::Basename;
use File::Path;
use threads;
use threads::shared;
use Thread::Semaphore;
use Scalar::Util qw(looks_like_number);

use Codemap;
use SVG;

my $silent = undef;

my $concurrency = 1; # Number of doSplit threads
# If $ARGV[0] is a number, use it as concurrency.
if (looks_like_number($ARGV[0])) {
    $concurrency = shift(@ARGV);
    if ($concurrency < 1) {
        print STDERR "Invalid concurrency: $concurrency\nAborting...\n";
        exit 1;
    }
}

my $semaphore = Thread::Semaphore->new($concurrency);
my $exitflag :shared = 0;

my $jointhrs = threads->new(\&joinThreads);

while (@ARGV) {
    my $orig_svg = shift(@ARGV);
    $semaphore->down;
    threads->new(\&doSplit, $semaphore, $orig_svg);
}

until ($exitflag) {
    my $thrnum = threads->list;
    if ($thrnum < 2) {
        $exitflag = 1;
    }
}
$jointhrs->join;

exit 0;

# Make a thorough join of all threads except main and self.
sub joinThreads {
    until ($exitflag) {
        foreach my $thr (threads->list) {
            my $tid = $thr->tid;
            if ($tid and !threads::equal($thr, threads->self)) {
                $thr->join;
                #print STDERR "  Thread $tid joined.\n" unless defined $silent;
            }
        }
    }
}

# split svgs.
sub doSplit {
    my $semaphore = shift;
    my $orig_svg = shift;

    my $svg = new SVG($orig_svg);
    $svg->setdumpdir("work.d");
    if ($svg->modtime() > $svg->splittime()) {
	$svg->dump();
	print STDERR "  $svg->{filename} : splitted\n" unless defined $silent;
    } else {
	print STDERR "  $svg->{filename} : SKIP\n" unless defined $silent;
    }
    $semaphore->up;
}
