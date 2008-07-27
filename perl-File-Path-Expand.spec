#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	File
%define		pnam	Path-Expand
Summary:	File::Path::Expand - expand filenames
Summary(pl.UTF-8):	File::Path::Expand - rozwijanie nazw plików
Name:		perl-File-Path-Expand
Version:	1.02
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	742aa40a4ffb26d14de01192764bd7ab
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

%description -l pl.UTF-8
File::Path::Expand rozwija katalogi użytkownika w nazwach plików. W
prostym przypadku nie jest to bardziej skomplikowane od
s{^~/}{$HOME/}, ale w innych wykorzystywana jest funkcja getpwent, aby
zrobić to co trzeba.

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
%doc Changes
%{perl_vendorlib}/%{pdir}/*/*.pm
%{_mandir}/man3/*
