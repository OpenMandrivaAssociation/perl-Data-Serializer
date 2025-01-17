%define upstream_name    Data-Serializer
%define upstream_version 0.60

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    2

Summary:    Generic interface to serializer modules
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        https://search.cpan.org/dist/%{upstream_name}
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

%make

%check
%make test

%install
%makeinstall_std

%clean

%files
%doc Changes README
%{_mandir}/man3/*
%{perl_vendorlib}/*
