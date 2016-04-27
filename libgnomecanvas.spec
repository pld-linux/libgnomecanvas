#
# Conditional build:
%bcond_without	apidocs		# disable gtk-doc

Summary:	GnomeCanvas widget
Summary(pl.UTF-8):	Widget GnomeCanvas
Name:		libgnomecanvas
Version:	2.30.3
Release:	5
License:	LGPL v2+
Group:		X11/Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/libgnomecanvas/2.30/%{name}-%{version}.tar.bz2
# Source0-md5:	ffcbb719c671ff5cd86e59aeba8d0b92
Patch0:		%{name}-am.patch
URL:		http://www.gnome.org/
BuildRequires:	autoconf >= 2.54
BuildRequires:	automake
BuildRequires:	docbook-dtd412-xml
BuildRequires:	gail-devel >= 1.20.0
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel >= 1:2.10.0
BuildRequires:	gnome-common >= 2.20.0
BuildRequires:	gtk+2-devel >= 2:2.12.0
%{?with_apidocs:BuildRequires:	gtk-doc >= 1.8}
BuildRequires:	gtk-doc-automake >= 1.8
BuildRequires:	intltool >= 0.36.2
BuildRequires:	libart_lgpl-devel >= 2.3.19
BuildRequires:	libglade2-devel >= 1:2.6.2
BuildRequires:	libtool
BuildRequires:	pango-devel >= 1:1.0.1
BuildRequires:	perl-base >= 5.002
BuildRequires:	pkgconfig >= 1:0.18
BuildRequires:	rpmbuild(macros) >= 1.197
Requires:	gail >= 1.20.0
Requires:	glib2 >= 1:2.10.0
Requires:	gtk+2 >= 2:2.12.0
Requires:	libart_lgpl >= 2.3.19
Requires:	libglade2 >= 1:2.6.2
Requires:	pango >= 1:1.0.1
# sr@Latn vs. sr@latin
Conflicts:	glibc-misc < 6:2.7
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The canvas widget allows you to create custom displays using stock
items such as circles, lines, text, and so on. It was originally a
port of the Tk canvas widget but has evolved quite a bit over time.

%description -l pl.UTF-8
Widget canvas pozwala tworzyć własne widoki przy użyciu zgromadzonych
rzeczy takich jak koła, linie, tekst itp. Oryginalnie był to port
widgetu Tk canvas, ale od tamtego czasu nieco wyewoluował.

%package devel
Summary:	libgnomecanvas header files
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libgnomecanvas
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	gail-devel >= 1.20.0
Requires:	glib2-devel >= 1:2.10.0
Requires:	gtk+2-devel >= 2:2.12.0
Requires:	libart_lgpl-devel >= 2.3.19
Requires:	libglade2-devel >= 1:2.6.2
Requires:	pango-devel >= 1:1.0.1

%description devel
Development part of libgnomecanvas - header files.

%description devel -l pl.UTF-8
Część libgnomecanvas dla programistów - pliki nagłówkowe.

%package static
Summary:	Static libgnomecanvas library
Summary(pl.UTF-8):	Statyczna biblioteka libgnomecanvas
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static version of libgnomecanvas library.

%description static -l pl.UTF-8
Statyczna wersja biblioteki libgnomecanvas.

%package apidocs
Summary:	libgnomecanvas API documentation
Summary(pl.UTF-8):	Dokumentacja API biblioteki libgnomecanvas
Group:		Documentation
Requires:	gtk-doc-common
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description apidocs
libgnomecanvas API documentation.

%description apidocs -l pl.UTF-8
Dokumentacja API biblioteki libgnomecanvas.

%package examples
Summary:	libgnomecanvas - example programs
Summary(pl.UTF-8):	libgnomecanvas - przykładowe programy
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description examples
libgnomecanvas - example programs.

%description examples -l pl.UTF-8
libgnomecanvas - przykładowe programy.

%prep
%setup -q
%patch0 -p1

%build
%{__gtkdocize}
%{__glib_gettextize}
%{__intltoolize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	%{?with_apidocs:--enable-gtk-doc} \
	--with-html-dir=%{_gtkdocdir} \
	--enable-glade
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

cp demos/*.{c,h,png} $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

# no static modules and *.la for glade modules
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libglade/2.0/*.{la,a} \
	$RPM_BUILD_ROOT%{_libdir}/*.la

%{__mv} $RPM_BUILD_ROOT%{_localedir}/{sr@ije,sr@ijekavian}

%find_lang %{name}-2.0

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{name}-2.0.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/libgnomecanvas-2.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgnomecanvas-2.so.0
%attr(755,root,root) %{_libdir}/libglade/2.0/libcanvas.so

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgnomecanvas-2.so
%{_includedir}/libgnomecanvas-2.0
%{_pkgconfigdir}/libgnomecanvas-2.0.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libgnomecanvas-2.a

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/libgnomecanvas

%files examples
%defattr(644,root,root,755)
%{_examplesdir}/%{name}-%{version}
