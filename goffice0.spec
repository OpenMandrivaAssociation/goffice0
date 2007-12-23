%define name goffice0
%define oname goffice
%define version 0.4.3

%define api 0
%define major 4
%define libname %mklibname %oname %{api}_%major
%define develname %mklibname -d %oname %api

Summary: Set of document centric objects and utilities for glib/gtk
Name: %{name}
Version: %{version}
Release: %mkrel 5
Source0: http://ftp.gnome.org/pub/GNOME/sources/goffice/%{oname}-%{version}.tar.bz2
License: GPLv2+
Group: System/Libraries
Url: http://www.gnome.org
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	automake
BuildRequires:	intltool
BuildRequires: gtk+2-devel
BuildRequires: libgnomeprint-devel >= 2.8.2
BuildRequires: libgsf-devel >= 1:1.13.3
BuildRequires: libglade2.0-devel
BuildRequires: libgnomeui2-devel
BuildRequires: libGConf2-devel
BuildRequires: libgsf-devel
BuildRequires: pcre libpcre-devel
BuildRequires: gtk-doc
BuildRequires: perl-XML-Parser
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
%configure2_5x --enable-gtk-doc --with-gnome
%make

%install
rm -rf $RPM_BUILD_ROOT %name-%version.lang
%makeinstall_std
%find_lang %oname-%version
find %buildroot -name \*.la|xargs chmod 644

%clean
rm -rf $RPM_BUILD_ROOT

%post -n %libname -p /sbin/ldconfig
%postun -n %libname -p /sbin/ldconfig

%files -f %oname-%version.lang
%defattr(-,root,root)
%doc README NEWS AUTHORS BUGS MAINTAINERS
%_datadir/%oname
%_datadir/pixmaps/%oname
%dir %_libdir/%oname/

%files -n %libname
%defattr(-,root,root)
%_libdir/libgoffice-%api.so.%{major}*
%_libdir/%oname/%version/

%files -n %develname
%defattr(-,root,root)
%_includedir/libgoffice-0.4/
%_libdir/lib*.so
%attr(644,root,root) %_libdir/lib*a
%_libdir/pkgconfig/*.pc
%_datadir/gtk-doc/html/goffice/
