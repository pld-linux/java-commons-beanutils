Summary:	Jakarta Commons BeanUtils - Bean Introspection Utilities
Summary(pl):	Jakarta Commons BeanUtils - narzędzia do badania JavaBeans
Name:		jakarta-commons-beanutils
Version:	1.6.1
Release:	1
License:	Apache
Group:		Development/Languages/Java
Source0:	http://sunsite.icm.edu.pl/pub/www/apache/dist/jakarta/commons/beanutils/binaries/commons-beanutils-%{version}.tar.gz
# Source0-md5:	846d578ab2e703c5ab179ed56270550e
URL:		http://jakarta.apache.org/
Requires:	jre
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_javalibdir	/usr/share/java

%description
The Bean Introspection Utilities component of the Jakarta Commons
subproject offers low-level utility classes that assist in getting and
setting property values on Java classes that follow the naming design
patterns outlined in the JavaBeans Specification, as well as
mechanisms for dynamically defining and accessing bean properties.

%description -l pl
Komponent Bean Instrospection Utilities z podprojektu Jakarta Commons
oferuje niskopoziomowe klasy narzędziowe pomagające w odczytywaniu i
ustawianiu wartości składowych klas Javy zgodnych ze wzorcami
nazewnictwa określonymi w specyfikacji JavaBeans oraz mechanizmy do
dynamicznego definiowania i dostępu do składowych.

%package doc
Summary:	Jakarta Commons BeanUtils documentation
Summary(pl):	Dokumentacja do Jakarta Commons BeanUtils
Group:		Development/Languages/Java

%description doc
Jakarta Commons BeanUtils documentation.

%description doc -l pl
Dokumentacja do Jakarta Commons BeanUtils.

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
