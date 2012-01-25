%define upstream_name    Data-Locations
%define upstream_version 5.5

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:	4

Summary:	Data-Locations module for perl 
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Data/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
This module allows for "magic" insertion points in your data.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make
make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc CHANGES.txt CREDITS.txt GNU_GPL.txt INSTALL.txt README.txt
%{perl_vendorlib}/*/Data/Locations.pm
%{perl_vendorlib}/*/auto/Data/Locations
%{_mandir}/*/*
