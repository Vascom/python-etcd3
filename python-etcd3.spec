%{?!python3_pkgversion:%global python3_pkgversion 3}

%global srcname etcd3

Name:           python-etcd3
Version:        0.12.0
Release:        1%{?dist}
Summary:        Python client for the etcd API v3
License:        ASL 2.0
URL:            https://github.com/kragniz/python-etcd3
Source0:        https://github.com/kragniz/python-etcd3/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools

%{?python_enable_dependency_generator}

%description
%{summary}, supported under python 2.7, 3.4 and 3.5.


%package -n python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}

%if %{undefined python_enable_dependency_generator} && %{undefined python_disable_dependency_generator}
# Put manual requires here:
Requires:       python%{python3_pkgversion}-foo
%endif

%description -n python%{python3_pkgversion}-%{srcname}
%{summary}, supported under python 2.7, 3.4 and 3.5.


%prep
%autosetup -p1 -n %{name}-%{version}


%build
%py3_build


%install
%py3_install


%files -n  python%{python3_pkgversion}-%{srcname}
%license LICENSE
%doc AUTHORS.rst CONTRIBUTING.rst HISTORY.rst README.rst
# # For noarch packages: sitelib
%{python3_sitelib}/%{srcname}/
%{python3_sitelib}/%{srcname}-%{version}-py%{python3_version}.egg-info/


%changelog
* Mon Jun 28 2021 Vasiliy Glazov <vascom2@gmail.com> - 0.12.0-1
- Initial packaging
