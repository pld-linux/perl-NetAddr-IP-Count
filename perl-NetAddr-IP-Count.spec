#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	NetAddr
%define	pnam	IP-Count
Summary:	NetAddr::IP::Count - Count hosts in named subnets
Summary(pl):	NetAddr::IP::Count - liczenie hostów w nazwanych podsieciach
Name:		perl-NetAddr-IP-Count
Version:	2.01
Release:	1
License:	unknown
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	daeebeba0f1983f00faba52bbc076872
URL:		http://search.cpan.org/dist/NetAddr-IP-Count/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-NetAddr-IP
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module implements a symplistic way to match individual IP
Addresses to subnets. It can be used to, among other things, help
analyze HTTPD logs.

%description -l pl
Ten modu³ implementuje uproszczony sposób dopasowywania poszczególnych
adresów IP do podsieci. Mo¿e byæ u¿ywany m.in. do pomocy przy analizie
logów HTTPD.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes sample.pl
%{perl_vendorlib}/NetAddr/IP/*.pm
%{_mandir}/man3/*
