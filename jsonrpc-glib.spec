#
# Conditional build:
%bcond_without	apidocs		# API documentation
%bcond_without	static_libs	# static library

Summary:	jsonrpc-glib - a library to communicate with JSON-RPC based peers
Summary(pl.UTF-8):	jsonrpc-glib - biblioteka do komunikacji poprzez JSON-RPC
Name:		jsonrpc-glib
Version:	3.38.0
Release:	1
License:	LGPL v2.1+
Group:		Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/jsonrpc-glib/3.38/%{name}-%{version}.tar.xz
# Source0-md5:	16b6027630df63146284deda1125481e
URL:		https://gitlab.gnome.org/GNOME/jsonrpc-glib
BuildRequires:	docbook-dtd412-xml
BuildRequires:	gettext-tools >= 0.18
BuildRequires:	glib2-devel >= 1:2.44.0
BuildRequires:	gobject-introspection-devel >= 0.9.5
%{?with_apidocs:BuildRequires:	gtk-doc >= 1.20}
BuildRequires:	json-glib-devel
BuildRequires:	meson >= 0.49.2
BuildRequires:	ninja >= 1.5
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRequires:	vala
Requires:	glib2 >= 1:2.44.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Jsonrpc-GLib is a library to communicate with JSON-RPC based peers in
either a synchronous or asynchronous fashion.

%description -l pl.UTF-8
Jsonrpc-GLib to biblioteka do komunikacji z partnerami JSON-RPC w
trybie synchronicznym lub asynchronicznym.

%package devel
Summary:	Header files for the jsonrpc-glib library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki jsonrpc-glib
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	glib2-devel >= 1:2.44.0
Requires:	json-glib-devel

%description devel
Header files for the jsonrpc-glib library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki jsonrpc-glib.

%package static
Summary:	Static jsonrpc-glib library
Summary(pl.UTF-8):	Statyczna biblioteka jsonrpc-glib
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static jsonrpc-glib library.

%description static -l pl.UTF-8
Statyczna biblioteka jsonrpc-glib.

%package apidocs
Summary:	jsonrpc-glib API documentation
Summary(pl.UTF-8):	Dokumentacja API jsonrpc-glib
Group:		Documentation
Requires:	gtk-doc-common
BuildArch:	noarch

%description apidocs
jsonrpc-glib API documentation.

%description apidocs -l pl.UTF-8
Dokumentacja API jsonrpc-glib.

%package -n vala-jsonrpc-glib
Summary:	jsonrpc-glib API for Vala language
Summary(pl.UTF-8):	API jsonrpc-glib dla języka Vala
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	vala >= 2:0.18.0
BuildArch:	noarch

%description -n vala-jsonrpc-glib
jsonrpc-glib API for Vala language.

%description -n vala-jsonrpc-glib -l pl.UTF-8
API jsonrpc-glib dla języka Vala.

%prep
%setup -q

%build
%meson build \
	%{!?with_static_libs:--default-library=shared} \
	%{?with_apidocs:-Denable_gtk_doc=true}

%ninja_build -C build

%install
rm -rf $RPM_BUILD_ROOT

%ninja_install -C build

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README.md
%attr(755,root,root) %{_libdir}/libjsonrpc-glib-1.0.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libjsonrpc-glib-1.0.so.1
%{_libdir}/girepository-1.0/Jsonrpc-1.0.typelib

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libjsonrpc-glib-1.0.so
%{_datadir}/gir-1.0/Jsonrpc-1.0.gir
%{_includedir}/jsonrpc-glib-1.0
%{_pkgconfigdir}/jsonrpc-glib-1.0.pc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libjsonrpc-glib-1.0.a
%endif

%if %{with apidocs}
%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/jsonrpc-glib
%endif

%files -n vala-jsonrpc-glib
%defattr(644,root,root,755)
%{_datadir}/vala/vapi/jsonrpc-glib-1.0.deps
%{_datadir}/vala/vapi/jsonrpc-glib-1.0.vapi
