%define gtk2_version 1.3.12.90
%define libart_lgpl_version 2.3.7.91
%define libglade2_version 1.99.5.90

Summary:	GnomeCanvas widget
Name:		libgnomecanvas
Version:	1.108.0.90
Release:	1
License:	LGPL
Group:		X11/Libraries
Group(de):	X11/Libraries
Group(es):	X11/Bibliotecas
Group(fr):	X11/Librairies
Group(pl):	X11/Biblioteki
Group(pt_BR):	X11/Bibliotecas
Group(ru):	X11/Библиотеки
Group(uk):	X11/Б╕бл╕отеки
Source0:	ftp://ftp.gnome.org/pub/gnome/pre-gnome2/sources/libgnomecanvas/%{name}-%{version}.tar.bz2
URL:		http://www.gnome.org/
BuildRequires:	gtk2-devel >= %{gtk2_version}
BuildRequires:	libart_lgpl-devel >= %{libart_lgpl_version}
BuildRequires:	libglade2-devel >= %{libglade2_version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
The canvas widget allows you to create custom displays using stock
items such as circles, lines, text, and so on. It was originally a
port of the Tk canvas widget but has evolved quite a bit over time.

%package devel
Summary:	Libraries and headers for libgnomecanvas.
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(ru):	Разработка/Библиотеки
Group(uk):	Розробка/Б╕бл╕отеки
Requires:	%name = %{version}
Conflicts:	gnome-libs-devel < 1.4.1.2
Requires:	gtk2-devel >= %{gtk2_version}
Requires:	libart_lgpl-devel >= %{libart_lgpl_version}
Requires:	libglade2-devel >= %{libglade2_version}

%description devel
The canvas widget allows you to create custom displays using stock
items such as circles, lines, text, and so on. It was originally a
port of the Tk canvas widget but has evolved quite a bit over time.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

gzip -9nf AUTHORS ChangeLog NEWS README

%find_lang %name

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%attr(755,root,root) %{_libdir}/lib*.la
%{_pkgconfigdir}/*
%{_includedir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
