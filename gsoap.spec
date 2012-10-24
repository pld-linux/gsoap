# TODO
# - shared libraries?
# - eliminitate or document skip_post_check_so
Summary:	gSOAP - a development toolkit for Web services
Summary(pl.UTF-8):	gSOAP - zestawem narzędzi programistycznych dla usług WWW
Name:		gsoap
Version:	2.8.11
Release:	0.2
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

%prep
%setup -q -n %{name}-2.8
%patch0 -p1

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

install -d $RPM_BUILD_ROOT%{_datadir}/%{name}
cp -p gsoap/stdsoap2.c $RPM_BUILD_ROOT%{_datadir}/%{name}
cp -p gsoap/stdsoap2.cpp $RPM_BUILD_ROOT%{_datadir}/%{name}

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
