# $Id$

# Authority: dries
# Upstream: Dave Rolsky <autarch$urth,org>

%define real_name Net-SSH-Perl
%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)
%define perl_archlib %(eval "`perl -V:archlib`"; echo $archlib)
%define perl_privlib %(eval "`perl -V:privlib`"; echo $privlib)

Summary: Perl client interface to SSH
Name: perl-Net-SSH-Perl
Version: 1.27
Release: 1
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Net-SSH-Perl/

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: http://search.cpan.org/CPAN/authors/id/D/DR/DROLSKY/Net-SSH-Perl-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl, perl-Math-Pari

%description
Net::SSH::Perl contains implementations of
both the SSH1 and SSH2 protocols.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" destdir=%{buildroot}
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README Changes
%doc %{_mandir}/man3/*
#%{perl_vendorlib}/NAMEDIR.pm
#%{perl_vendorlib}/NAMEDIR/*
#%exclude %{perl_archlib}/perllocal.pod
#%exclude %{perl_vendorarch}/auto/*/*/.packlist

# perl_vendorlib: /usr/lib/perl5/vendor_perl/5.8.0
# perl_vendorarch: /usr/lib/perl5/vendor_perl/5.8.0/i386-linux-thread-multi
# perl_archlib: /usr/lib/perl5/5.8.0/i386-linux-thread-multi
# perl_privlib: /usr/lib/perl5/5.8.0

%changelog
* Fri Mar  4 2005 Dries Verachtert <dries@ulyssis.org> - 1.27-1
- Updated to release 1.27.

* Mon Dec 06 2004 Dries Verachtert <dries@ulyssis.org> - 1.24-1
- Initial package.
