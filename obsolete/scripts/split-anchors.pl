#!/usr/local/bin/perl

# usage: split-anchors.pl WEIGHT module_name > set_bearings

$weight = shift;
@ARGV = grep { -e $_ } map { $_ = "../../../../svg.d/$_/anchors" } @ARGV;
exit 0 if (scalar @ARGV == 0);

%weight_columns = ( 'black' => 0, 'heavy' => 2, 'bold' => 4, 'medium' => 6, 
		    'regular' => 8, 'light' => 10, 'thin' => 12);
$X = $weight_columns{$weight};
$Y = $X+1;

%lookups;
%features;

foreach my $arg (@ARGV) {
	open(ANCHORS, "<$arg") or die "can't open $arg";
	$linenum = 0;
	while (<ANCHORS>) {
		$linenum++;
		next if ( /^#/ or /^\s*$/ );
		die("unexpected line: $arg l$linenum: $_") if ( not /^@(\S+)\s*(.*)$/ );
		if ( $1 eq 'lookup' ) {
			($lookup, $feature) = split(/\s+/,$2,2);
			$lookups{$lookup} = {'m' => {}, 'p' => {}} if ( not defined($lookups{$lookup}) );
			$features{$feature} = {} if ( not defined($features{$feature}) );
		} elsif ( $1 eq 'lookupflag' ) {
			$lookups{$lookup}{'f'} = $2;
		} elsif ( $1 eq 'script' ) {
			my ($script, @langs) = split(/\s+/,$2);
			my $f = $features{$feature};
			$f->{$script} = [] if ( not defined($f->{$script}) );
			push(@{$f->{$script}}, $lookup);
		} elsif ( $1 eq 'markClass' ) {
			my $tag = $2;
			while (<ANCHORS>) {
				last if ($_ =~ /^\@end\s*$/);
				next if (/^#/ or /^\s*$/);
				my ($name, @anchors) = split();
				my ($x, $y) = ($anchors[$X], $anchors[$Y]);
				$lookups{$lookup}{'m'}{$name} = [$x, $y, $tag];
			}
		} elsif ( $1 eq 'pos' ) {
			my ($type, $tag) = split(/\s+/,$2,2);
			while (<ANCHORS>) {
				last if ($_ =~ /^\@end\s*$/);
				next if (/^#/ or /^\s*$/);
				my ($name, @anchors) = split();
				my ($x, $y) = ($anchors[$X], $anchors[$Y]);
				$lookups{$lookup}{'p'}{$name} = [$type, $x, $y, $tag];
			}
		}
	}
	close ANCHORS;
}
foreach my $lookup ( keys %lookups ) {
	print "lookup $lookup {\n";
	my $f = $lookups{$lookup}{'f'};
	print "  lookupflag $f;\n" if (defined $f);
	foreach my $name ( keys %{$lookups{$lookup}{'m'}} ) {
		my ($x, $y, $tag) = (@{$lookups{$lookup}{'m'}{$name}});
		print "  markClass [\\$name ] <anchor $x $y> $tag;\n";
	}
	foreach my $name ( keys %{$lookups{$lookup}{'p'}} ) {
		my ($type, $x, $y, $tag) = (@{$lookups{$lookup}{'p'}{$name}});
		print "  pos $type [\\$name ] <anchor $x $y> mark $tag;\n";
	}
	print "} $lookup;\n";
}
foreach my $feature ( keys %features ) {
	print "feature $feature {\n";
	foreach my $script ( keys %{$features{$feature}} ) {
		print "  script $script;\n";
		print "     language dflt ;\n";
		foreach my $lookup ( @{$features{$feature}{$script}} ) {
			print "      lookup $lookup;\n";
		}
	}
	print "} $feature;\n"
}
