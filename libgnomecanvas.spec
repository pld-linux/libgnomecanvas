Summary:	GnomeCanvas widget
Summary(pl):	Widget GnomeCanvas
Name:		libgnomecanvas
Version:	1.117.0
Release:	1
License:	LGPL
Group:		X11/Libraries
Source0:	ftp://ftp.gnome.org/pub/gnome/pre-gnome2/sources/libgnomecanvas/%{name}-%{version}.tar.bz2
URL:		http://www.gnome.org/
BuildRequires:	gtk+2-devel
BuildRequires:	libart_lgpl-devel
BuildRequires:	libglade2-devel
BuildRequires:	pango-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
The canvas widget allows you to create custom displays using stock
items such as circles, lines, text, and so on. It was originally a
port of the Tk canvas widget but has evolved quite a bit over time.

%description -l pl
Widget canvas pozwala tworzyæ w³asne widoki przy u¿yciu zgromadzonych
rzeczy takich jak ko³a, linie, tekst itp. Oryginalnie by³ to port
widgetu Tk canvas, ale od tamtego czasu nieco wyewoluowa³.

%package devel
Summary:	libgnomecanvas header files
Summary(pl):	Pliki nag³ówkowe libgnomecanvas
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}

%description devel
Development part of libgnomecanvas - header files.

%description devel -l pl
Czê¶æ libgnomecanvas dla programistów - pliki nag³ówkowe.

%package static
Summary:	Static libgnomecanvas library
Summary(pl):	Statyczna biblioteka libgnomecanvas
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Static version of libgnomecanvas library.

%description static -l pl
Statyczna wersja biblioteki libgnomecanvas.

%prep
%setup -q

%build
%configure \
	--enable-gtk-doc=no
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	pkgconfigdir=%{_pkgconfigdir}

gzip -9nf AUTHORS ChangeLog NEWS README

%clean
rm -rf %{buildroot}

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%attr(755,root,root) %{_libdir}/lib*.la
%{_pkgconfigdir}/*.pc
%{_includedir}/libgnomecanvas-2.0

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
