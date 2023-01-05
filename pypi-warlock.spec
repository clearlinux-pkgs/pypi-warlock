#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-warlock
Version  : 2.0.1
Release  : 2
URL      : https://files.pythonhosted.org/packages/de/cf/ba9ac96d09b797c377e2c12c0eb6b19565f3b2a2efb55932d319e319b622/warlock-2.0.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/de/cf/ba9ac96d09b797c377e2c12c0eb6b19565f3b2a2efb55932d319e319b622/warlock-2.0.1.tar.gz
Summary  : Python object model built on JSON schema and JSON patch.
Group    : Development/Tools
License  : Apache-2.0
Requires: pypi-warlock-license = %{version}-%{release}
Requires: pypi-warlock-python = %{version}-%{release}
Requires: pypi-warlock-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(poetry_core)

%description
# Warlock 🧙‍♀️
**Create self-validating Python objects using JSON schema.**
[![PyPI](https://img.shields.io/pypi/v/warlock.svg)][warlock]
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/warlock.svg)][warlock]
[![PyPI - Downloads](https://img.shields.io/pypi/dw/warlock.svg)][pypistats]

%package license
Summary: license components for the pypi-warlock package.
Group: Default

%description license
license components for the pypi-warlock package.


%package python
Summary: python components for the pypi-warlock package.
Group: Default
Requires: pypi-warlock-python3 = %{version}-%{release}

%description python
python components for the pypi-warlock package.


%package python3
Summary: python3 components for the pypi-warlock package.
Group: Default
Requires: python3-core
Provides: pypi(warlock)
Requires: pypi(jsonpatch)
Requires: pypi(jsonschema)

%description python3
python3 components for the pypi-warlock package.


%prep
%setup -q -n warlock-2.0.1
cd %{_builddir}/warlock-2.0.1
pushd ..
cp -a warlock-2.0.1 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1669574338
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-warlock
cp %{_builddir}/warlock-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/pypi-warlock/2b8b815229aa8a61e483fb4ba0588b8b6c491890 || :
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
pip install --root=%{buildroot}-v3 --no-deps --ignore-installed dist/*.whl
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-warlock/2b8b815229aa8a61e483fb4ba0588b8b6c491890

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
