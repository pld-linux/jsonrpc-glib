Summary:	jsonrpc-glib - a library providing serialization and deserialization support for the JSON format
Summary(pl.UTF-8):	jsonrpc-glib - biblioteka zapewniająca serializację i deserializację dla formatu JSON
Name:		jsonrpc-glib
Version:	3.26.1
Release:	0.2
License:	LGPL v2.1+
Group:		Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/jsonrpc-glib/3.26/%{name}-%{version}.tar.xz
# Source0-md5:	e40e4485223ee021ee069b54aced28da
BuildRequires:	docbook-dtd412-xml
BuildRequires:	gettext-tools >= 0.18
BuildRequires:	glib2-devel >= 1:2.44.0
BuildRequires:	gobject-introspection-devel >= 0.9.5
BuildRequires:	gtk-doc >= 1.20
BuildRequires:	meson >= 0.40.1
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.726
BuildRequires:	vala
Requires:	glib2 >= 1:2.44.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
jsonrpc-glib is a library providing serialization and deserialization
support for the JavaScript Object Notation (JSON) format described by
RFC 4627.

%description -l pl.UTF-8
jsonrpc-glib to biblioteka zapewniająca obsługę serializacji i
deserializacji dla formatu JSON (JavaScript Object Notation) opisanego
w RFC 4627.

%package devel
Summary:	Header files for the jsonrpc-glib library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki jsonrpc-glib
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	glib2-devel >= 1:2.44.0

%description devel
Header files for the jsonrpc-glib library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki jsonrpc-glib.

%package apidocs
Summary:	jsonrpc-glib API documentation
Summary(pl.UTF-8):	Dokumentacja API jsonrpc-glib
Group:		Documentation
Requires:	gtk-doc-common
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

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
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description -n vala-jsonrpc-glib
jsonrpc-glib API for Vala language.

%description -n vala-jsonrpc-glib -l pl.UTF-8
API jsonrpc-glib dla języka Vala.

%prep
%setup -q

%build
%meson build \
	-Dintrospection=true \
	-Denable_gtk_doc=true

%meson_build -C build

%install
rm -rf $RPM_BUILD_ROOT

%meson_install -C build

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc NEWS README.md
%attr(755,root,root) %{_libdir}/libjsonrpc_glib-1.0.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libjsonrpc_glib-1.0.so.0
%{_libdir}/girepository-1.0/Jsonrpc-1.0.typelib

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libjsonrpc_glib-1.0.so
%{_datadir}/gir-1.0/Jsonrpc-1.0.gir
%{_includedir}/jsonrpc-glib-1.0
%{_pkgconfigdir}/jsonrpc-glib-1.0.pc

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/jsonrpc-glib

%files -n vala-jsonrpc-glib
%defattr(644,root,root,755)
%{_datadir}/vala/vapi/jsonrpc-glib-1.0.deps
%{_datadir}/vala/vapi/jsonrpc-glib-1.0.vapi
