Name:		python-tzdata
Version:	2025.3
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/t/tzdata/tzdata-%{version}.tar.gz
Summary:	Provider of IANA time zone data
URL:		https://pypi.org/project/tzdata/
License:	Apache-2.0
Group:		Development/Python
BuildRequires:	python
BuildRequires:  python%{pyver}dist(setuptools)
BuildSystem:	python
BuildArch:	noarch

%description
Provider of IANA time zone data

%files
%{py_sitedir}/tzdata
%{py_sitedir}/tzdata-*.*-info
