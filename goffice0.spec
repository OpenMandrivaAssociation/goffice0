%define name goffice0
%define oname goffice
%define version 0.9.6

%define api 0.10
%define major 9
%define libname %mklibname %oname %{api}_%major
%define develname %mklibname -d %oname %api

Summary: Set of document centric objects and utilities for glib/gtk
Name: %{name}
Version: %{version}
Release: %mkrel 8
Source0: http://ftp.gnome.org/pub/GNOME/sources/goffice/%{oname}-%{version}.tar.xz
License: GPLv2+
Group: System/Libraries
Url: http://www.gnome.org
BuildRequires:	automake
BuildRequires:	intltool
BuildRequires: pkgconfig(gtk+-3.0)
BuildRequires: pkgconfig(libgnomeprint-2.2)
BuildRequires: pkgconfig(libglade-2.0)
BuildRequires: pkgconfig(libgnomeui-2.0)
BuildRequires: pkgconfig(gconf-2.0)
BuildRequires: pkgconfig(libgsf-1)
BuildRequires: pcre pkgconfig(libpcre)
BuildRequires: perl-XML-Parser
BuildRequires: pkgconfig(librsvg-2.0)
Obsoletes: %oname <= 0.4.3

%description
There are common operations for document centric applications that are
conceptually simple, but complex to implement fully.
    - plugins
    - load/save documents
    - undo/redo

%package -n %libname
Summary:  %{summary}
Group: %{group}
Requires: %name >= %version

%description -n %libname
Shared library implementing document centric objects and utilities for glib/gtk

%package -n %develname
Summary:  %{summary}
Group: Development/C
Requires: %libname = %version
Provides: %name-devel = %version-%release
Provides: lib%name-devel = %version-%release
Conflicts: %mklibname -d goffice 0_3
Obsoletes: %mklibname -d goffice 0_4

%description -n %develname
Development files of the Goffice library.

%prep
%setup -q -n %oname-%version

%build
%configure2_5x
%make

%install
%makeinstall_std
%find_lang %oname-%version

%files -f %oname-%version.lang
%doc README NEWS AUTHORS BUGS MAINTAINERS
%dir %_libdir/%oname/

%files -n %libname
%_libdir/libgoffice-%api.so.%{major}*
%_libdir/%oname/%version/

%files -n %develname
%_includedir/libgoffice-%{api}
%_libdir/lib*.so
%_libdir/pkgconfig/*.pc
%_datadir/gtk-doc/html/goffice-%{api}


%changelog
* Sat Nov 08 2008 Funda Wang <fundawang@mandriva.org> 0.4.3-8mdv2009.1
+ Revision: 301129
- rebuild for new xcb

* Thu Jul 24 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.4.3-7mdv2009.0
+ Revision: 246516
- rebuild

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Sun Dec 23 2007 Funda Wang <fundawang@mandriva.org> 0.4.3-5mdv2008.1
+ Revision: 137265
- add missing BR

* Sun Dec 23 2007 Funda Wang <fundawang@mandriva.org> 0.4.3-4mdv2008.1
+ Revision: 137250
- Enable gnome extension

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Oct 22 2007 Götz Waschk <waschk@mandriva.org> 0.4.3-3mdv2008.1
+ Revision: 101085
- new devel name

* Fri Sep 07 2007 Götz Waschk <waschk@mandriva.org> 0.4.3-3mdv2008.0
+ Revision: 81432
- fix deps

* Tue Sep 04 2007 Götz Waschk <waschk@mandriva.org> 0.4.3-2mdv2008.0
+ Revision: 79319
- rename the package
- copy goffice to goffice0

* Tue Sep 04 2007 Götz Waschk <waschk@mandriva.org> 0.4.3-1mdv2008.0
+ Revision: 79228
- new version
- fix build

* Tue Jul 24 2007 Götz Waschk <waschk@mandriva.org> 0.4.2-1mdv2008.0
+ Revision: 54976
- new version

* Wed Jul 11 2007 Götz Waschk <waschk@mandriva.org> 0.4.1-1mdv2008.0
+ Revision: 51223
- new version
- drop merged patch
- add conflict with old devel package for upgrades

* Fri May 04 2007 Götz Waschk <waschk@mandriva.org> 0.4.0-1mdv2008.0
+ Revision: 22231
- new version
- new major

* Sun Apr 22 2007 Götz Waschk <waschk@mandriva.org> 0.3.8-1mdv2008.0
+ Revision: 16891
- new version

