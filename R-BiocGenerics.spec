%global packname BiocGenerics
%global rlibdir %{_libdir}/R/library

Name:             R-%{packname}
Version:          0.6.0 
Release:          1
Summary:          Generic functions for Bioconductor
Group:            Sciences/Mathematics
License:          Artistic-2.0
URL:              http://bioconductor.org/packages/release/bioc/html/BiocGenerics.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/BiocGenerics_0.6.0.tar.gz
BuildArch:        noarch
Requires:         R-methods R-graphics R-stats R-parallel
BuildRequires:    R-methods R-graphics R-stats R-parallel

%description
S4 generic functions needed by many Bioconductor packages

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/unitTests
