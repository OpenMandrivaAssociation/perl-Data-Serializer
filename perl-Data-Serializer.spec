%define upstream_name    Data-Serializer
%define upstream_version 0.59

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    2

Summary:    Generic interface to serializer modules
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Data/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(AutoLoader)
BuildRequires: perl(Data::Dumper)
BuildRequires: perl(Digest::SHA)
BuildRequires: perl(Exporter)
BuildRequires: perl(File::Spec)
BuildRequires: perl(IO::File)
BuildRequires: perl(Test::More)
BuildRequires: perl(Module::Build::Compat)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
This module is intended for folks who release CPAN modules with "t/*.t"
tests. It makes it easy for you to output syntactically correct test-output
while at the same time logging all test activity to a log file. Hopefully,
bug reports which include the contents of this file will be easier for you
to investigate.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor

%{make}

%check
%{make} test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes README
%{_mandir}/man3/*
%perl_vendorlib/*




%changelog
* Wed Jun 22 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.590.0-1mdv2011.0
+ Revision: 686627
- update to new version 0.59

* Sat Apr 23 2011 Funda Wang <fwang@mandriva.org> 0.570.0-2
+ Revision: 656903
- rebuild for updated spec-helper

* Sun Jan 30 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.570.0-1
+ Revision: 634224
- update to new version 0.57

* Tue Jan 04 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.520.0-1mdv2011.0
+ Revision: 628572
- update to new version 0.52

* Fri Dec 31 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0.510.0-1mdv2011.0
+ Revision: 626821
- update to new version 0.51

* Tue Jul 27 2010 Shlomi Fish <shlomif@mandriva.org> 0.490.0-1mdv2011.0
+ Revision: 561148
- import perl-Data-Serializer


* Sat Oct 10 2009 cpan2dist 0.49-1mdv
- initial mdv release, generated with cpan2dist
