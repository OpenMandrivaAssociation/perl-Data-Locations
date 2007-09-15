%define real_name Data-Locations

Summary:	Data-Locations module for perl 
Name:		perl-%{real_name}
Version:	5.4
Release:	%mkrel 2
License:	GPL or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{real_name}
Source0:	%{real_name}-%{version}.tar.bz2
BuildRequires:	perl-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
This module allows for "magic" insertion points in your data.

%prep
%setup -q -n %{real_name}-%{version}

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


