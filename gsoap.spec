# TODO
# - eliminitate or document skip_post_check_so
Summary:	gSOAP - a development toolkit for Web services
Summary(pl.UTF-8):	gSOAP - zestawem narzędzi programistycznych dla usług WWW
Name:		gsoap
Version:	2.8.11
Release:	1
License:	gSOAP / GPL
Group:		Development/Libraries
Source0:	http://downloads.sourceforge.net/gsoap2/%{name}_%{version}.zip
# Source0-md5:	ea2d7ee876d274a188b8fbb365702eec
Patch0:		%{name}-libtool.patch
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
%patch0 -p1

# remove stuff with gsoap license only - not GPL
%{__rm} -r gsoap/extras gsoap/mod_gsoap gsoap/Symbian
%{__sed} -i -e 's!$(srcdir)/extras/\*!!' gsoap/Makefile.am

%build
%{__libtoolize}
%{__aclocal}
%{__automake}
%{__autoconf}
%configure
# -j1 as dependencies are not declared properly
%{__make} -j1

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

%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/import
%{_datadir}/%{name}/import/c14n.h
%{_datadir}/%{name}/import/dom.h
%{_datadir}/%{name}/import/ds2.h
%{_datadir}/%{name}/import/ds.h
%{_datadir}/%{name}/import/README.txt
%{_datadir}/%{name}/import/soap12.h
%{_datadir}/%{name}/import/stldeque.h
%{_datadir}/%{name}/import/stl.h
%{_datadir}/%{name}/import/stllist.h
%{_datadir}/%{name}/import/stlset.h
%{_datadir}/%{name}/import/stlvector.h
%{_datadir}/%{name}/import/wsa3.h
%{_datadir}/%{name}/import/wsa4.h
%{_datadir}/%{name}/import/wsa5.h
%{_datadir}/%{name}/import/wsa.h
%{_datadir}/%{name}/import/WS-example.c
%{_datadir}/%{name}/import/WS-example.h
%{_datadir}/%{name}/import/WS-Header.h
%{_datadir}/%{name}/import/wsp.h
%{_datadir}/%{name}/import/wsrp.h
%{_datadir}/%{name}/import/wsse2.h
%{_datadir}/%{name}/import/wsse.h
%{_datadir}/%{name}/import/wsu.h
%{_datadir}/%{name}/import/xlink.h
%{_datadir}/%{name}/import/xmime4.h
%{_datadir}/%{name}/import/xmime5.h
%{_datadir}/%{name}/import/xmime.h
%{_datadir}/%{name}/import/xml.h
%{_datadir}/%{name}/import/xmlmime5.h
%{_datadir}/%{name}/import/xmlmime.h
%{_datadir}/%{name}/import/xop.h
%dir %{_datadir}/%{name}/WS
%{_datadir}/%{name}/WS/README.txt
%{_datadir}/%{name}/WS/WS-Addressing.xsd
%{_datadir}/%{name}/WS/WS-Addressing03.xsd
%{_datadir}/%{name}/WS/WS-Addressing04.xsd
%{_datadir}/%{name}/WS/WS-Addressing05.xsd
%{_datadir}/%{name}/WS/WS-Discovery.wsdl
%{_datadir}/%{name}/WS/WS-Enumeration.wsdl
%{_datadir}/%{name}/WS/WS-Policy.xsd
%{_datadir}/%{name}/WS/WS-Routing.xsd
%{_datadir}/%{name}/WS/WS-typemap.dat
%{_datadir}/%{name}/WS/discovery.xsd
%{_datadir}/%{name}/WS/ds.xsd
%{_datadir}/%{name}/WS/enumeration.xsd
%{_datadir}/%{name}/WS/typemap.dat
%{_datadir}/%{name}/WS/wsse.xsd
%{_datadir}/%{name}/WS/wsu.xsd
%dir %{_datadir}/%{name}/custom
%{_datadir}/%{name}/custom/README.txt
%{_datadir}/%{name}/custom/long_double.c
%{_datadir}/%{name}/custom/long_double.h
%{_datadir}/%{name}/custom/struct_timeval.c
%{_datadir}/%{name}/custom/struct_timeval.h
%{_datadir}/%{name}/custom/struct_tm.c
%{_datadir}/%{name}/custom/struct_tm.h
%dir %{_datadir}/%{name}/plugin
%{_datadir}/%{name}/plugin/README.txt
%{_datadir}/%{name}/plugin/cacerts.c
%{_datadir}/%{name}/plugin/cacerts.h
%{_datadir}/%{name}/plugin/httpda.c
%{_datadir}/%{name}/plugin/httpda.h
%{_datadir}/%{name}/plugin/httpdatest.c
%{_datadir}/%{name}/plugin/httpdatest.h
%{_datadir}/%{name}/plugin/httpform.c
%{_datadir}/%{name}/plugin/httpform.h
%{_datadir}/%{name}/plugin/httpget.c
%{_datadir}/%{name}/plugin/httpget.h
%{_datadir}/%{name}/plugin/httpgettest.c
%{_datadir}/%{name}/plugin/httpgettest.h
%{_datadir}/%{name}/plugin/httpmd5.c
%{_datadir}/%{name}/plugin/httpmd5.h
%{_datadir}/%{name}/plugin/httpmd5test.c
%{_datadir}/%{name}/plugin/httpmd5test.h
%{_datadir}/%{name}/plugin/httppost.c
%{_datadir}/%{name}/plugin/httppost.h
%{_datadir}/%{name}/plugin/logging.c
%{_datadir}/%{name}/plugin/logging.h
%{_datadir}/%{name}/plugin/md5evp.c
%{_datadir}/%{name}/plugin/md5evp.h
%{_datadir}/%{name}/plugin/plugin.c
%{_datadir}/%{name}/plugin/plugin.h
%{_datadir}/%{name}/plugin/smdevp.c
%{_datadir}/%{name}/plugin/smdevp.h
%{_datadir}/%{name}/plugin/threads.c
%{_datadir}/%{name}/plugin/threads.h
%{_datadir}/%{name}/plugin/wsaapi.c
%{_datadir}/%{name}/plugin/wsaapi.h
%{_datadir}/%{name}/plugin/wsse2api.c
%{_datadir}/%{name}/plugin/wsse2api.h
%{_datadir}/%{name}/plugin/wsseapi.c
%{_datadir}/%{name}/plugin/wsseapi.h
# Additions in 2.7.12-1
%{_datadir}/%{name}/WS/WS-ReliableMessaging.wsdl
%{_datadir}/%{name}/WS/WS-ReliableMessaging.xsd
%{_datadir}/%{name}/WS/reference-1.1.xsd
%{_datadir}/%{name}/WS/ws-reliability-1.1.xsd
%{_datadir}/%{name}/import/ref.h
%{_datadir}/%{name}/import/wsrm.h
%{_datadir}/%{name}/import/wsrm4.h
%{_datadir}/%{name}/import/wsrx.h
# Additions in 2.7.13-1
%{_datadir}/%{name}/import/stdstring.h
%{_datadir}/%{name}/import/xsd.h
%{_datadir}/%{name}/plugin/wsseapi.cpp
# Additions in 2.7.16-1
%{_datadir}/%{name}/custom/duration.c
%{_datadir}/%{name}/custom/duration.h
%{_datadir}/%{name}/plugin/httpposttest.c
%{_datadir}/%{name}/plugin/httpposttest.h
%{_datadir}/%{name}/plugin/wsrmapi.c
%{_datadir}/%{name}/plugin/wsrmapi.h
# Additions in 2.7.17-1
%{_datadir}/%{name}/WS/WS-Policy12.xsd
%{_datadir}/%{name}/WS/WS-SecurityPolicy.xsd
%{_datadir}/%{name}/import/wsse11.h
# Additions in 2.8.3-1
%{_datadir}/%{name}/WS/xenc.xsd
%{_datadir}/%{name}/import/xenc.h
%{_datadir}/%{name}/plugin/mecevp.c
%{_datadir}/%{name}/plugin/mecevp.h
# Additions in 2.8.4-1
%{_datadir}/%{name}/import/wsdd.h
%{_datadir}/%{name}/import/wsdx.h
%{_datadir}/%{name}/plugin/wsddapi.c
%{_datadir}/%{name}/plugin/wsddapi.h
# Additions in 2.8.7-1
%{_datadir}/%{name}/import/wsdd10.h

# Additions in 2.8.9-1
%{_datadir}/gsoap/WS/WS-SecureConversation.xsd
%{_datadir}/gsoap/WS/WS-Trust.wsdl
%{_datadir}/gsoap/WS/WS-Trust.xsd
%{_datadir}/gsoap/import/ser.h
%{_datadir}/gsoap/import/wsc.h
%{_datadir}/gsoap/import/wsrm5.h
%{_datadir}/gsoap/import/wsrx5.h
%{_datadir}/gsoap/import/wst.h
%{_datadir}/gsoap/import/wstx.h

%files static
%defattr(644,root,root,755)
%{_libdir}/libgsoap++.a
%{_libdir}/libgsoap.a
%{_libdir}/libgsoapck++.a
%{_libdir}/libgsoapck.a
%{_libdir}/libgsoapssl++.a
%{_libdir}/libgsoapssl.a
