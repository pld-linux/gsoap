Summary:	gSOAP is a development toolkit for Web services
Summary(pl):	gSOAP jest zestawem narzêdzi dla Web services
Name:		gsoap
Version:	2.7
Release:	3
License:	gSOAP public license
Group:		Development/Libraries
Source0:	http://dl.sourceforge.net/gsoap2/%{name}-%{version}.tar.gz
# Source0-md5:	c48eb15227892f94d00934bce63ef504
URL:		http://www.cs.fsu.edu/~engelen/soap.html
BuildRequires:	automake
BuildRequires:	bison
BuildRequires:	libstdc++
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
gSOAP provides a cross-platform development toolkit for developing
server, client, and peer Web service applications in C and C++.

%description -l pl
gSOAP udostêpnia wieloplatformowe narzêdzia programistyczne do
tworzenia serwerów, klientów i partnerów aplikacji Web service w C i
C++.

%prep
%setup -q

%build
cp -f /usr/share/automake/config.sub .
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc soapcpp2/COPYING.txt soapcpp2/README.txt soapcpp2/*.html
%attr(755,root,root) %{_bindir}/*
%{_includedir}/*
%{_libdir}/*.a
%{_pkgconfigdir}/*.pc
