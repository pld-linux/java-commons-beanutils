Summary:	Jakarta Commons Beanutils
Name:		jakarta-commons-beanutils
Version:	1.6.1
Release:	1
License:	Apache
Group:		Development/Languages/Java
Source0:	http://sunsite.icm.edu.pl/pub/www/apache/dist/jakarta/commons/beanutils/binaries/commons-beanutils-%{version}.tar.gz
URL:		http://jakarta.apache.org/
Requires:	jre
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_javalibdir	/usr/share/java

%description
Jakarta Commons Beanutils.

%package doc
Summary:	Jakarta Commons Beanutils
Group:		Development/Languages/Java

%description doc
Jakarta Commons Beanutils.

%prep
%setup -q -n commons-beanutils-%{version}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_javalibdir}
install *.jar $RPM_BUILD_ROOT%{_javalibdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.txt
%{_javalibdir}/*.jar

%files doc
%defattr(644,root,root,755)
%doc docs
