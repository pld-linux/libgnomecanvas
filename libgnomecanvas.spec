#
# Conditional build:
%bcond_without	apidocs		# disable gtk-doc
#
Summary:	GnomeCanvas widget
Summary(pl.UTF-8):	Widget GnomeCanvas
Name:		libgnomecanvas
Version:	2.26.0
Release:	2
License:	LGPL v2+
Group:		X11/Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/libgnomecanvas/2.26/%{name}-%{version}.tar.bz2
# Source0-md5:	9bbc635e5ae70e63af071af74ba7e72f
URL:		http://www.gnome.org/
BuildRequires:	autoconf >= 2.54
BuildRequires:	automake
BuildRequires:	gail-devel >= 1.20.0
BuildRequires:	gettext-devel
BuildRequires:	gnome-common >= 2.20.0
BuildRequires:	gtk+2-devel >= 2:2.12.0
%{?with_apidocs:BuildRequires:	gtk-doc >= 1.8}
BuildRequires:	gtk-doc-automake >= 1.3
BuildRequires:	intltool >= 0.36.2
BuildRequires:	libart_lgpl-devel >= 2.3.19
BuildRequires:	libglade2-devel >= 1:2.6.2
BuildRequires:	libtool
BuildRequires:	perl-base >= 5.002
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.197
BuildRequires:	sed >= 4.0
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
Summary(pl.UTF-8):	Pliki nagłówkowe libgnomecanvas
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	gail-devel >= 1.20.0
Requires:	gtk+2-devel >= 2:2.12.0
Requires:	libart_lgpl-devel >= 2.3.19
Requires:	libglade2-devel >= 1:2.6.2

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
Summary(pl.UTF-8):	Dokumentacja API libgnomecanvas
Group:		Documentation
Requires:	gtk-doc-common

%description apidocs
libgnomecanvas API documentation.

%description apidocs -l pl.UTF-8
Dokumentacja API libgnomecanvas.

%package examples
Summary:	libgnomecanvas - example programs
Summary(pl.UTF-8):	libgnomecanvas - przykładowe programy
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description examples
libgnomecanvas - example programs.

%description examples -l pl-UTF-8
libgnomecanvas - przykładowe programy.

%prep
%setup -q

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
	--with-html-dir=%{_gtkdocdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

cp demos/*.{c,h,png} $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

# no static modules and *.la for glade modules
rm -f $RPM_BUILD_ROOT%{_libdir}/libglade/2.0/*.{la,a}

%find_lang %{name} --with-gnome --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/libgnomecanvas-2.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgnomecanvas-2.so.0
%attr(755,root,root) %{_libdir}/libglade/2.0/libcanvas.so

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgnomecanvas-2.so
%{_libdir}/libgnomecanvas-2.la
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
