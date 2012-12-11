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


%changelog
* Wed Jan 25 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 5.500.0-4
+ Revision: 768358
- svn commit -m mass rebuild of perl extension against perl 5.14.2

* Sun May 29 2011 Funda Wang <fwang@mandriva.org> 5.500.0-3
+ Revision: 681377
- mass rebuild

* Tue Jul 20 2010 Jérôme Quelin <jquelin@mandriva.org> 5.500.0-2mdv2011.0
+ Revision: 555764
- rebuild for perl 5.12

* Fri Nov 06 2009 Jérôme Quelin <jquelin@mandriva.org> 5.500.0-1mdv2010.1
+ Revision: 461730
- update to 5.5

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 5.4-6mdv2010.0
+ Revision: 430403
- rebuild

* Wed Jul 30 2008 Thierry Vignaud <tv@mandriva.org> 5.4-5mdv2009.0
+ Revision: 256470
- rebuild

* Tue Jan 15 2008 Thierry Vignaud <tv@mandriva.org> 5.4-3mdv2008.1
+ Revision: 152047
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Sat Sep 15 2007 Guillaume Rousse <guillomovitch@mandriva.org> 5.4-2mdv2008.0
+ Revision: 86326
- rebuild


* Wed Sep 13 2006 Oden Eriksson <oeriksson@mandriva.com> 5.4-1mdv2007.0
- rebuild

* Thu Jul 14 2005 Oden Eriksson <oeriksson@mandriva.com> 5.4-1mdk
- initial Mandriva package

