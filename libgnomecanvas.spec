%define gtk2_version 1.3.12.90
%define libart_lgpl_version 2.3.7.91
%define libglade2_version 1.99.5.90

Summary: GnomeCanvas widget
Name: libgnomecanvas
Version: 1.108.0.90
Release: 1
URL: http://www.gnome.org/
Source0: %{name}-%{version}.tar.gz
License: LGPL
Group: System Environment/Libraries 
BuildRoot: %{_tmppath}/%{name}-root
Requires: gtk2 >= %{gtk2_version}
BuildRequires: gtk2-devel >= %{gtk2_version}
BuildRequires: libart_lgpl-devel >= %{libart_lgpl_version}
BuildRequires: libglade2-devel >= %{libglade2_version}

%description

The canvas widget allows you to create custom displays using stock items 
such as circles, lines, text, and so on. It was originally a port of the 
Tk canvas widget but has evolved quite a bit over time.

%package devel
Summary: Libraries and headers for libgnomecanvas.
Group: Development/Libraries
Requires:	%name = %{version}
Conflicts:      gnome-libs-devel < 1.4.1.2
Requires: gtk2-devel >= %{gtk2_version}
Requires: libart_lgpl-devel >= %{libart_lgpl_version}
Requires: libglade2-devel >= %{libglade2_version}

%description devel

The canvas widget allows you to create custom displays using stock items 
such as circles, lines, text, and so on. It was originally a port of the 
Tk canvas widget but has evolved quite a bit over time.

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
make install DESTDIR=$RPM_BUILD_ROOT

%find_lang %name

%clean
rm -rf %{buildroot}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(-,root,root)

%doc AUTHORS COPYING ChangeLog NEWS README

%{_libdir}/lib*.so.*

%files devel
%defattr(-,root,root)

%{_libdir}/lib*.a
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*
%{_includedir}/*

%changelog
* Wed Jan  2 2002 Havoc Pennington <hp@redhat.com>
- 1.108.0.90 cvs snap

* Mon Nov 26 2001 Havoc Pennington <hp@redhat.com>
- cvs snap 1.105.0.90, gtk 1.3.11

* Fri Oct 26 2001 Havoc Pennington <hp@redhat.com>
- new cvs snap, rebuild for gtk 1.3.10, 
  add libglade dep, fix libart dep

* Fri Oct  5 2001 Havoc Pennington <hp@redhat.com>
- rebuild cvs snap for new glib/gtk

* Fri Sep 21 2001 Havoc Pennington <hp@redhat.com>
- new cvs snap with upstream changes

* Thu Sep 13 2001 Havoc Pennington <hp@redhat.com>
- Initial build.
