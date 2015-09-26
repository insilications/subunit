Name     : subunit
Version  : 1.1.0
Release  : 23
URL      : https://launchpad.net/subunit/trunk/1.1.0/+download/subunit-1.1.0.tar.gz
Source0  : https://launchpad.net/subunit/trunk/1.1.0/+download/subunit-1.1.0.tar.gz
Summary  : Subunit test protocol library.
Group    : Development/Tools
License  : Apache-2.0 MIT
Requires: subunit-bin
Requires: subunit-python
Requires: subunit-lib
BuildRequires : extras
BuildRequires : iso8601
BuildRequires : pbr
BuildRequires : pip
BuildRequires : pkgconfig(check)
BuildRequires : pkgconfig(cppunit)
BuildRequires : python-dev
BuildRequires : python3
BuildRequires : python3-dev
BuildRequires : setuptools
BuildRequires : testrepository
BuildRequires : testresources
BuildRequires : testscenarios
BuildRequires : testtools
BuildRequires : traceback2

%description
subunit: A streaming protocol for test results
Licensed under either the Apache License, Version 2.0 or the BSD 3-clause
license at the users choice. A copy of both licenses are available in the
project source as Apache-2.0 and BSD. You may not use this file except in
compliance with one of these two licences.

%package bin
Summary: bin components for the subunit package.
Group: Binaries

%description bin
bin components for the subunit package.


%package dev
Summary: dev components for the subunit package.
Group: Development
Requires: subunit-lib
Requires: subunit-bin
Provides: subunit-devel

%description dev
dev components for the subunit package.


%package lib
Summary: lib components for the subunit package.
Group: Libraries

%description lib
lib components for the subunit package.


%package python
Summary: python components for the subunit package.
Group: Default
Provides: python-subunit
Provides: python-subunit-python

%description python
python components for the subunit package.


%prep
%setup -q -n subunit-1.1.0

%build
%configure --disable-static
make V=1  %{?_smp_mflags}


%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
make check || :

%install
rm -rf %{buildroot}
%make_install
PYTHON_VERSION=3.4 
PYTHON=/usr/bin/python3
export PYTHON_VERSION
export PYTHON
%configure --disable-static
make V=1  %{?_smp_mflags}
%make_install

%files
%defattr(-,root,root,-)
/usr/lib/perl5/site_perl/5.22.0/Subunit.pm
/usr/lib/perl5/site_perl/5.22.0/Subunit/Diff.pm
/usr/lib/perl5/site_perl/5.22.0/x86_64-linux/auto/Subunit/.packlist

%files bin
%defattr(-,root,root,-)
/usr/bin/subunit-1to2
/usr/bin/subunit-2to1
/usr/bin/subunit-diff
/usr/bin/subunit-filter
/usr/bin/subunit-ls
/usr/bin/subunit-notify
/usr/bin/subunit-output
/usr/bin/subunit-stats
/usr/bin/subunit-tags
/usr/bin/subunit2csv
/usr/bin/subunit2gtk
/usr/bin/subunit2junitxml
/usr/bin/subunit2pyunit
/usr/bin/tap2subunit

%files dev
%defattr(-,root,root,-)
/usr/include/subunit/SubunitTestProgressListener.h
/usr/include/subunit/child.h
/usr/lib64/*.so
/usr/lib64/pkgconfig/*.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/*.so.*

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
