%global srcname etcd3

Name:           python-%{srcname}
Version:        0.12.0
Release:        2%{?dist}
Summary:        Python client for the etcd API v3
License:        ASL 2.0
URL:            https://github.com/kragniz/python-etcd3
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  %{py3_dist setuptools}

%global _description %{summary}, supported under python 2.7, 3.4 and 3.5.

%description
%{_description}

%package -n python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python%{python3_pkgversion}-%{srcname}
%{_description}


%prep
%autosetup -p1 -n %{name}-%{version}


%build
%py3_build


%install
%py3_install


%files -n  python%{python3_pkgversion}-%{srcname}
%license LICENSE
%doc AUTHORS.rst CONTRIBUTING.rst HISTORY.rst README.rst
%{python3_sitelib}/%{srcname}/
%{python3_sitelib}/%{srcname}-*.egg-info/


%changelog
* Tue Jun 29 2021 Vasiliy Glazov <vascom2@gmail.com> - 0.12.0-2
- Fix python macro

* Mon Jun 28 2021 Vasiliy Glazov <vascom2@gmail.com> - 0.12.0-1
- Initial packaging
