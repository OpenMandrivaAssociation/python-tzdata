%define module tzdata

Name:		python-tzdata
Version:	2026.1
Release:	1
Summary:	Provider of IANA time zone data
License:	Apache-2.0
Group:		Development/Python
URL:		https://pypi.org/project/tzdata/
Source0:	https://files.pythonhosted.org/packages/source/t/%{module}/%{module}-%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildSystem:	python
BuildArch:	noarch
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(wheel)

%description
Provider of IANA time zone data

%files
%{py_sitedir}/%{module}
%{py_sitedir}/%{module}-%{version}.dist-info
