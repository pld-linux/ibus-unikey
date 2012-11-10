Summary:	Vietnamese engine for IBus input platform
Summary(pl.UTF-8):	Silnik wietnamski dla platformy wprowadzania znaków IBus
Name:		ibus-unikey
Version:	0.6.1
Release:	1
License:	GPL v3
Group:		Libraries
Source0:	http://ibus-unikey.googlecode.com/files/%{name}-%{version}.tar.gz
# Source0-md5:	3bae6df0d4609a8c438c246030b9a61e
URL:		http://code.google.com/p/ibus-unikey/
BuildRequires:	GConf2-devel
BuildRequires:	gettext-devel >= 0.17
BuildRequires:	gtk+2-devel >= 2:2.12
BuildRequires:	ibus-devel >= 1.2.99
BuildRequires:	intltool
BuildRequires:	libstdc++-devel
BuildRequires:	pkgconfig
BuildRequires:	xorg-lib-libX11-devel
Requires:	ibus >= 1.2.99
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_libexecdir	%{_libdir}/ibus

%description
A Vietnamese engine for IBus input platform that uses Unikey.

%description -l pl.UTF-8
Silnik wietnamski dla platformy wprowadzania znaków IBus. Wykorzystuje
Unikey.

%prep
%setup -q

%build
%configure \
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README AUTHORS ChangeLog
%attr(755,root,root) %{_libexecdir}/ibus-engine-unikey
%attr(755,root,root) %{_libexecdir}/ibus-setup-unikey
%{_datadir}/%{name}
%{_datadir}/ibus/component/unikey.xml
