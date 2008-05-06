# TODO
# - shared libraries?
Summary:	gSOAP - a development toolkit for Web services
Summary(pl.UTF-8):	gSOAP - zestawem narzędzi programistycznych dla usług WWW
Name:		gsoap
Version:	2.7.10
Release:	1
License:	gSOAP / GPL
Group:		Development/Libraries
Source0:	http://dl.sourceforge.net/gsoap2/%{name}_%{version}.tar.gz
# Source0-md5:	31ac50314900d87c43f8f008c8de712f
URL:		http://www.cs.fsu.edu/~engelen/soap.html
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	libstdc++-devel
BuildRequires:	openssl-devel
BuildRequires:	pkgconfig
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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

%prep
%setup -q -n %{name}-2.7

%build
%{__aclocal}
%{__automake}
%{__autoconf}
%configure
%{__make} -j1

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_datadir}/%{name}
install gsoap/stdsoap2.c $RPM_BUILD_ROOT%{_datadir}/%{name}
install gsoap/stdsoap2.cpp $RPM_BUILD_ROOT%{_datadir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE.txt README.txt
%attr(755,root,root) %{_bindir}/soapcpp2
%attr(755,root,root) %{_bindir}/wsdl2h
%{_includedir}/stdsoap2.h
%{_libdir}/libgsoap++.a
%{_libdir}/libgsoap.a
%{_libdir}/libgsoapck++.a
%{_libdir}/libgsoapck.a
%{_libdir}/libgsoapssl++.a
%{_libdir}/libgsoapssl.a
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/stdsoap2.*
%{_pkgconfigdir}/*.pc
