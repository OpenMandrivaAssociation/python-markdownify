Name:		python-markdownify
Version:	1.2.0
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/m/markdownify/markdownify-%{version}.tar.gz
Summary:	Convert HTML to Markdown
URL:		https://github.com/matthewwithanm/python-markdownify
License:	MIT
Group:		Development/Python
BuildRequires:	python

Requires:  python3dist(beautifulsoup4)
Requires:  python3dist(six)

BuildSystem:	python
BuildArch:	noarch

%description
Convert HTML to Markdown

%files
%{_bindir}/markdownify
%{python_sitelib}/markdownify-%{version}.dist-info/
%{python_sitelib}/markdownify/
