Name:       python3-fuse3
Summary:    Python bindings for the fuse3 library
Version:    2.0.0
Release:    1
License:    LGPLv2+
URL:        https://pypi.org/project/pyfuse3/
Source0:    %{name}-%{version}.tar.bz2
BuildRequires:  pkgconfig(fuse3)
BuildRequires:  python3-devel
BuildRequires:  python3-cython
BuildRequires:  python3-setuptools
Requires:       python3-base
Requires:       python3-trio

%description
%{summary}.

%prep
%setup -q -n %{name}-%{version}/pyfuse3

%build
# Remove MANIFEST.in so that the package is built in release mode.
rm -f MANIFEST.in
python3 ./setup.py build_cython
python3 ./setup.py build

%install
rm -rf %{buildroot}
%py3_install

%files
%defattr(-,root,root,-)
%{python3_sitearch}/pyfuse3.cpython-*.so
%{python3_sitearch}/pyfuse3_asyncio.py
%{python3_sitearch}/_pyfuse3.py
%{python3_sitearch}/pyfuse3-*.egg-info
%{python3_sitearch}/__pycache__/*
