# vim:set ts=8 sts=4 sw=4 tw=0:
#
# Last Change: 20-Apr-2004.
# Maintainer:  MURAOKA Taro <koron@tka.att.ne.jp>

package UCSTable;

my $DIR = "ucstable.d";

sub new
{
    my $class = shift;
    my $encode_name = shift;
    my $this = bless {
	name => $encode_name,
	table => {},
    }, $class;
    $this->_load("$DIR/$encode_name.TXT");
    $this->_load("$DIR/$encode_name.WIN.TXT");
    return $this;
}

sub _load
{
    my $this = shift;
    my $filename = shift;
    return 0 if not -f $filename;
    open IN, $filename;
    binmode IN;
    while (<IN>) {
	chomp;
	s/\s*#.*$//;
	next if m/^$/;
	if (m/^0x([[:xdigit:]]+)\s+0x([[:xdigit:]]+)/) {
	    #print "  $1->$2\n";
	    $this->{table}->{hex($1)} = hex($2);
	}
    }
    close IN;
    return 1;
}

sub get
{
    my $this = shift;
    my $from = hex(shift);
    if (exists $this->{table}->{$from}) {
	return $this->{table}->{$from};
    } else {
	return undef;
    }
}

1;
