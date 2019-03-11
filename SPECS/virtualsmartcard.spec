%global reponame vsmartcard
%global commit c63cc40c34b44193c4cb8f9a97fb30c9680ebd0f
%global gittag HEAD
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           virtualsmartcard
Version:        3.0
Release:        1.20190117.%shortcommit%{?dist}
Summary:        Virtual SmartCard

License:        GPLv3
URL:            https://github.com/frankmorgner/%{reponame}/tree/master/%{name}
Source0:        https://github.com/frankmorgner/%{reponame}/archive/%{shortcommit}/%{name}-%{shortcommit}.tar.gz
Patch0:         %%{name}-3.0-libprefix.patch

BuildRequires:  pcsc-lite-devel
BuildRequires:  help2man
BuildRequires:  check
BuildRequires:  python3-devel
BuildRequires:  gcc
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool

%description
Virtual Smart Card emulates a smart vard and makes it accessible through PC/SC.

%global debug_package %{nil}

%prep
%setup -q -n %{reponame}-%{commit}/%{name}
%patch0 -p2 -b .libprefix


%build
autoreconf --verbose --force --install --symlink #using --force to prevent issues with libtool and aclocal.m4 being not in sync
autoconf
%configure 
make %{?_smp_mflags}


%install
make DESTDIR=%{buildroot} install
 

%files
%license COPYING
%doc README.md
%_bindir/vicc
%_bindir/vpcd-config
%{python3_sitelib}/%{name}/*
%{_mandir}/man1/vicc.1*
%{_libdir}/pcsc/drivers/serial/libifdvpcd.so
%{_libdir}/pcsc/drivers/serial/libifdvpcd.so.0.8
%config(noreplace) %{_sysconfdir}/reader.conf.d/vpcd



%changelog
* Mon Mar 11 2019 Pierre-Louis Palant <ppalant@redhat.com> 0-1
- Changed Source to get current master branch with python3 support (no release with python3 support yet)

* Wed Mar 06 2019 Pierre-Louis Palant <ppalant@redhat.com> 0.7-2
- Added Jakub Jelen's patch for the prefix problem
- Changed dependency python2 to python3 as python2 is disabled in RHEL8

* Tue Mar 05 2019 Pierre-Louis Palant <ppalant@redhat.com> 0.7-1
- rebuilt


