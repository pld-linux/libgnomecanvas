%define gtk2_version 1.3.12.90
%define libart_lgpl_version 2.3.7.91
%define libglade2_version 1.99.5.90

Summary:	GnomeCanvas widget
Summary(pl):	Widget GnomeCanvas
Name:		libgnomecanvas
Version:	1.109.0
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

%description -l pl
Widget canvas pozwala tworzyФ wЁasne widoki przy u©yciu zgromadzonych
rzeczy takich jak koЁa, linie, tekst itp. Oryginalnie byЁ to port
widgetu Tk canvas, ale od tamtego czasu nieco wyewoluowaЁ.

%package devel
Summary:	libgnomecanvas header files
Summary(pl):	Pliki nagЁСwkowe libgnomecanvas
Group:		X11/Development/Libraries
Group(de):	X11/Entwicklung/Libraries
Group(es):	X11/Desarrollo/Bibliotecas
Group(fr):	X11/Development/Librairies
Group(pl):	X11/Programowanie/Biblioteki
Group(pt_BR):	X11/Desenvolvimento/Bibliotecas
Group(ru):	X11/Разработка/Библиотеки
Group(uk):	X11/Розробка/Б╕бл╕отеки
Requires:	%{name} = %{version}
Conflicts:	gnome-libs-devel < 1.4.1.2
Requires:	gtk2-devel >= %{gtk2_version}
Requires:	libart_lgpl-devel >= %{libart_lgpl_version}
Requires:	libglade2-devel >= %{libglade2_version}

%description devel
Development part of libgnomecanvas - header files.

%description devel -l pl
CzЙ╤Ф libgnomecanvas dla programistСw - pliki nagЁСwkowe.

%package static
Summary:	Static libgnomecanvas library
Summary(pl):	Statyczna biblioteka libgnomecanvas
Group:		X11/Development/Libraries
Group(de):	X11/Entwicklung/Libraries
Group(es):	X11/Desarrollo/Bibliotecas
Group(fr):	X11/Development/Librairies
Group(pl):	X11/Programowanie/Biblioteki
Group(pt_BR):	X11/Desenvolvimento/Bibliotecas
Group(ru):	X11/Разработка/Библиотеки
Group(uk):	X11/Розробка/Б╕бл╕отеки
Requires:	%{name}-devel = %{version}

%description static
Static version of libgnomecanvas library.

%description static -l pl
Statyczna wersja biblioteki libgnomecanvas.

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

%find_lang %{name}

%clean
rm -rf %{buildroot}

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

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
