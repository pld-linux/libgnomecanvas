Summary:	GnomeCanvas widget
Summary(pl):	Widget GnomeCanvas
Name:		libgnomecanvas
Version:	2.0.1
Release:	1
License:	LGPL
Group:		X11/Libraries
Source0:	ftp://ftp.gnome.org/pub/gnome/pre-gnome2/sources/libgnomecanvas/%{name}-%{version}.tar.bz2
URL:		http://www.gnome.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	libart_lgpl-devel >= 2.3.8
BuildRequires:	libglade2-devel >= 2.0.0
BuildRequires:	libtool
BuildRequires:	gnome-common
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man
%define		_gtkdocdir	/usr/share/doc/gtk-doc/html

%description
The canvas widget allows you to create custom displays using stock
items such as circles, lines, text, and so on. It was originally a
port of the Tk canvas widget but has evolved quite a bit over time.

%description -l pl
Widget canvas pozwala tworzy� w�asne widoki przy u�yciu zgromadzonych
rzeczy takich jak ko�a, linie, tekst itp. Oryginalnie by� to port
widgetu Tk canvas, ale od tamtego czasu nieco wyewoluowa�.

%package devel
Summary:	libgnomecanvas header files
Summary(pl):	Pliki nag��wkowe libgnomecanvas
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}

%description devel
Development part of libgnomecanvas - header files.

%description devel -l pl
Cz�� libgnomecanvas dla programist�w - pliki nag��wkowe.

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
rm -f missing
libtoolize --copy --force
aclocal -I %{_aclocaldir}/gnome2-macros
%{__autoconf}
%{__automake}
%configure \
	--enable-gtk-doc \
	--with-html-path=%{_gtkdocdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	HTML_DIR=%{_gtkdocdir} \
	pkgconfigdir=%{_pkgconfigdir}

%find_lang %{name} --with-gnome --all-name

%clean
rm -rf %{buildroot}

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%attr(755,root,root) %{_libdir}/libglade/2.0/libcanvas.??

%files devel
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/lib*.so
%attr(755,root,root) %{_libdir}/lib*.la
%{_pkgconfigdir}/*.pc
%{_includedir}/libgnomecanvas-2.0
%{_gtkdocdir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
