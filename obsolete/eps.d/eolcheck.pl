#!/usr/bin/perl
# vim:set ts=8 sts=2 sw=2 tw=0:
#
# Last Change:	25-Jan-2004.
# Maintainer:	MURAOKA Taro <koron@tka.att.ne.jp>

use strict;

for (@ARGV) {
    my $should_be_converted = 0;
    open IN, $_ or next;
    binmode IN;
    # Check end-of-line which not in UNIX format.
    while (1) {
	my $data;
	my $len = read IN, $data, 4096;
	if (not defined $len) {
	    $should_be_converted = 0;
	    last;
	} elsif ($len == 0) {
	    last;
	} elsif ($data =~ /\r/) {
	    $should_be_converted = 1;
	    last;
	}
    }
    if ($should_be_converted) {
	# Convert EOL to UNIX format.
	seek IN, 0, 0;
	local $/ = "";
	my $all_data = <IN>;
	close IN;
	my @lines = split /\r\n?/, $all_data;
	open OUT, ">$_" or next;
	print STDOUT "Converting $_ ...\n";
	binmode OUT;
	for (@lines) {
	    print OUT $_, "\n";
	}
	close OUT;
    } else {
	close IN;
    }
}
