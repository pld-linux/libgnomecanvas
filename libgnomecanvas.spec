Summary:	GnomeCanvas widget
Summary(pl):	Widget GnomeCanvas
Name:		libgnomecanvas
Version:	2.8.0
Release:	1
License:	LGPL
Group:		X11/Libraries
Source0:	http://ftp.gnome.org/pub/gnome/sources/%{name}/2.8/%{name}-%{version}.tar.bz2
# Source0-md5:	2bf10396a92777e7b64b6052a8a232f1
URL:		http://www.gnome.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	gnome-common >= 2.8.0
BuildRequires:	gtk+2-devel >= 2:2.4.0
BuildRequires:	gtk-doc >= 1.1
BuildRequires:	libart_lgpl-devel >= 2.3.14
BuildRequires:	libglade2-devel >= 1:2.4.0
BuildRequires:	libtool
BuildRequires:	perl-base >= 5.002
BuildRequires:	pkgconfig
BuildRequires:	rpm-build >= 4.1-10
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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
Requires:	%{name} = %{version}-%{release}
Requires:	gtk+2-devel >= 2:2.4.0
Requires:	gtk-doc-common
Requires:	libart_lgpl-devel >= 2.3.14
Requires:	libglade2-devel >= 1:2.4.0

%description devel
Development part of libgnomecanvas - header files.

%description devel -l pl
Czê¶æ libgnomecanvas dla programistów - pliki nag³ówkowe.

%package static
Summary:	Static libgnomecanvas library
Summary(pl):	Statyczna biblioteka libgnomecanvas
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static version of libgnomecanvas library.

%description static -l pl
Statyczna wersja biblioteki libgnomecanvas.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--enable-gtk-doc \
	--with-html-dir=%{_gtkdocdir}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# no static modules and *.la for glade modules
rm -f $RPM_BUILD_ROOT%{_libdir}/libglade/2.0/*.{la,a}

rm -r $RPM_BUILD_ROOT%{_datadir}/locale/no

%find_lang %{name} --with-gnome --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%attr(755,root,root) %{_libdir}/libglade/2.0/libcanvas.so

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_pkgconfigdir}/*.pc
%{_includedir}/libgnomecanvas-2.0
%{_gtkdocdir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
