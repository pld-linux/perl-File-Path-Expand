#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	File
%define	pnam	Path-Expand
Summary:	File::Path::Expand - expand filenames
Summary(pl):	File::Path::Expand - rozwijanie nazw plik�w
Name:		perl-File-Path-Expand
Version:	1.01
Release:	1
# same as perl
License:	GPL or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	6f09799e04a24fbb2879e5e18437ebdf
%if %{with tests}
BuildRequires:	perl-Test-Simple
%endif
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
File::Path::Expand expands user directories in filenames. For the
simple case it's no more complex than s{^~/}{$HOME/}, but for other
cases it consults getpwent and does the right thing.

%description -l pl
File::Path::Expand rozwija katalogi u�ytkownika w nazwach plik�w. W
prostym przypadku nie jest to bardziej skomplikowane od
s{^~/}{$HOME/}, ale w innych wykorzystywana jest funkcja getpwent, aby
zrobi� to co trzeba.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_vendorlib}/%{pdir}/*/*.pm
%{_mandir}/man3/*
