#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define 	module	recordtype
Summary:	Similar to namedtuple, but instances are mutable
Summary(pl.UTF-8):	Dostarcza klasy podobne do namedtuple, ale modifikowalne
Name:		python-%{module}
Version:	1.1
Release:	2
License:	Apache v2.0
Group:		Libraries/Python
Source0:	https://pypi.python.org/packages/source/r/recordtype/%{module}-%{version}.tar.gz
# Source0-md5:	8133256b9c62baa2019ec16db3b14115
URL:		https://bitbucket.org/ericvsmith/recordtype
BuildRequires:	python-distribute
BuildRequires:	rpm-pythonprov
# if py_postclean is used
BuildRequires:	rpmbuild(macros) >= 1.219
#Requires:		python-libs
Requires:	python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
recordtype provides a factory function, named recordtype.recordtype.
It is similar to collections.namedtuple, with the following
differences:
- recordtype instances are mutable.
- recordtype supports per-field default values.
- recordtype supports an optional default value, to be used by all
  fields do not have an explicit default value

%description -l pl.UTF-8
Dostarcza generator klas podobnych do collections.namedtuple których
obiekty są modyfikowalne, z domyślnymi wartoścami.

%prep
%setup -q -n %{module}-%{version}

%build
%py_build

%{?with_tests:%{__python} setup.py test}

%install
rm -rf $RPM_BUILD_ROOT
%py_install

%py_ocomp $RPM_BUILD_ROOT%{py_sitedir}
%py_comp $RPM_BUILD_ROOT%{py_sitedir}
%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{py_sitescriptdir}/*.py[co]
%if "%{py_ver}" > "2.4"
%{py_sitescriptdir}/%{module}-*.egg-info
%endif
