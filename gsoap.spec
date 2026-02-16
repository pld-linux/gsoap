# TODO
# - eliminitate or document skip_post_check_so
Summary:	gSOAP - a development toolkit for Web services
Summary(pl.UTF-8):	gSOAP - zestawem narzędzi programistycznych dla usług WWW
Name:		gsoap
Version:	2.8.140
Release:	1
License:	gSOAP / GPL
Group:		Development/Libraries
Source0:	http://downloads.sourceforge.net/gsoap2/gsoap-2.8/%{name}_%{version}.zip
# Source0-md5:	884b7fe9516036ec9ae64f9c4da332eb
Patch0:		%{name}-libtool.patch
Patch1:		%{name}-xlocale.patch
Patch2:		bison.patch
URL:		http://www.cs.fsu.edu/~engelen/soap.html
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	openssl-devel
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.583
BuildRequires:	sed >= 4.0
BuildRequires:	unzip
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		skip_post_check_so	libgsoap.so.0.0.0 libgsoap\\+\\+.so.0.0.0 libgsoapck.so.0.0.0 libgsoapck\\+\\+.so.0.0.0 libgsoapssl.so.0.0.0 libgsoapssl\\+\\+.so.0.0.0

%description
Conforming to all SOAP 1.1 and 1.2 as well as the WSDL 1.1 standard,
the gSOAP toolkit provides a unique SOAP to C/C++ language binding for
the development of SOAP web services and clients. Relieving the user
from the typical burden of WSDL and SOAP details, the gSOAP compiler
generates efficient XML serializers for native and user defined C and
C++ data types.

%description -l pl.UTF-8
gSOAP udostępnia wieloplatformowe narzędzia programistyczne do
tworzenia serwerów, klientów i partnerów aplikacji usług WWW w C i
C++.

%package devel
Summary:	Devel libraries and headers for linking with gSOAP generated stubs
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
gSOAP libraries, headers and generators for linking with and creating
gSOAP generated stubs

%package static
Summary:	Static %{name} library
Summary(pl.UTF-8):	Statyczna biblioteka %{name}
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static %{name} library.

%description static -l pl.UTF-8
Statyczna biblioteka %{name}.

%prep
%setup -q -n %{name}-2.8
%patch -P0 -p1
#patch -P1 -p1
#patch -P2 -p1

# remove stuff with gsoap license only - not GPL
%{__rm} -r gsoap/extras gsoap/mod_gsoap gsoap/Symbian
%{__sed} -i -e 's!$(top_srcdir)/gsoap/extras/\*!!' gsoap/Makefile.am

%build
%{__libtoolize}
%{__aclocal}
%{__automake}
%{__autoconf}
%configure \
	--enable-ipv6
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README.txt NOTES.txt LICENSE.txt
%attr(755,root,root) %{_bindir}/soapcpp2
%attr(755,root,root) %{_bindir}/wsdl2h
%{_libdir}/libgsoap++.so.*.*.*
%ghost %{_libdir}/libgsoap++.so.0
%{_libdir}/libgsoap.so.*.*.*
%ghost %{_libdir}/libgsoap.so.0
%{_libdir}/libgsoapck++.so.*.*.*
%ghost %{_libdir}/libgsoapck++.so.0
%{_libdir}/libgsoapck.so.*.*.*
%ghost %{_libdir}/libgsoapck.so.0
%{_libdir}/libgsoapssl++.so.*.*.*
%ghost %{_libdir}/libgsoapssl++.so.0
%{_libdir}/libgsoapssl.so.*.*.*
%ghost %{_libdir}/libgsoapssl.so.0

%files devel
%defattr(644,root,root,755)
%doc gsoap/doc/*
%{_libdir}/libgsoap++.la
%{_libdir}/libgsoap++.so
%{_libdir}/libgsoap.la
%{_libdir}/libgsoap.so
%{_libdir}/libgsoapck++.la
%{_libdir}/libgsoapck++.so
%{_libdir}/libgsoapck.la
%{_libdir}/libgsoapck.so
%{_libdir}/libgsoapssl++.la
%{_libdir}/libgsoapssl++.so
%{_libdir}/libgsoapssl.la
%{_libdir}/libgsoapssl.so
%{_includedir}/stdsoap2.h
%{_pkgconfigdir}/gsoapck.pc
%{_pkgconfigdir}/gsoapck++.pc
%{_pkgconfigdir}/gsoap.pc
%{_pkgconfigdir}/gsoap++.pc
%{_pkgconfigdir}/gsoapssl.pc
%{_pkgconfigdir}/gsoapssl++.pc
%{_datadir}/%{name}

%files static
%defattr(644,root,root,755)
%{_libdir}/libgsoap++.a
%{_libdir}/libgsoap.a
%{_libdir}/libgsoapck++.a
%{_libdir}/libgsoapck.a
%{_libdir}/libgsoapssl++.a
%{_libdir}/libgsoapssl.a
