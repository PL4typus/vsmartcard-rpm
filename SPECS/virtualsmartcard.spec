Name:           virtualsmartcard
Version:        0.7
Release:        1%{?dist}
Summary:        Virtual SmartCard

License:        GPLv3
URL:            https://github.com/frankmorgner/vsmartcard/tree/master/%{name}
Source0:        https://github.com/frankmorgner/vsmartcard/releases/download/%{name}-%{version}/%{name}-%{version}.tar.gz
Patch0:         %{name}-0.7-libprefix.patch

BuildRequires:  pcsc-lite-devel
BuildRequires:  help2man
BuildRequires:  check
BuildRequires:  python2-devel
BuildRequires:  gcc
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool

%description
Virtual Smart Card emulates a smart vard and makes it accessible through PC/SC.

%global  debug_package %{nil}

%prep
%setup -q
%patch0 -p1 -b .libprefix


%build
autoreconf --verbose --force --install --symlink #using --force to prevent issues with libtool and aclocal.m4 being not in sync
autoconf
%configure 
make %{?_smp_mflags}


%install
make DESTDIR=%{buildroot} install
 

%files
%license COPYING
%doc README
%_bindir/vicc
%_bindir/vpcd-config
%{python2_sitelib}/%{name}/*
%{_mandir}/man1/vicc.1*
%{_libdir}/pcsc/drivers/serial/libifdvpcd.so
%{_libdir}/pcsc/drivers/serial/libifdvpcd.so.0.7
%config(noreplace) %{_sysconfdir}/reader.conf.d/vpcd



%changelog
* Wed Mar 06 2019 Pierre-Louis Palant <ppalant@redhat.com> 0.7-1
- Added Jakub Jelen's patch for the prefix problem

* Tue Mar 05 2019 Pierre-Louis Palant <ppalant@redhat.com> 0.7-1
- rebuilt


