Summary:	Jakarta Commons BeanUtils - Bean Introspection Utilities
Summary(pl.UTF-8):	Jakarta Commons BeanUtils - narzędzia do badania JavaBeans
Name:		jakarta-commons-beanutils
Version:	1.7.0
Release:	1
License:	Apache
Group:		Development/Languages/Java
Source0:	http://archive.apache.org/dist/jakarta/commons/beanutils/source/commons-beanutils-%{version}-src.zip
# Source0-md5:	9d320be7faefd9b260983dbc57f03875
URL:		http://jakarta.apache.org/commons/beanutils/
BuildRequires:	jakarta-commons-collections
BuildRequires:	jakarta-commons-logging
BuildRequires:	jpackage-utils
BuildRequires:	junit
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	jre
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Bean Introspection Utilities component of the Jakarta Commons
subproject offers low-level utility classes that assist in getting and
setting property values on Java classes that follow the naming design
patterns outlined in the JavaBeans Specification, as well as
mechanisms for dynamically defining and accessing bean properties.

%description -l pl.UTF-8
Komponent Bean Instrospection Utilities z podprojektu Jakarta Commons
oferuje niskopoziomowe klasy narzędziowe pomagające w odczytywaniu i
ustawianiu wartości składowych klas Javy zgodnych ze wzorcami
nazewnictwa określonymi w specyfikacji JavaBeans oraz mechanizmy do
dynamicznego definiowania i dostępu do składowych.

%package javadoc
Summary:	Jakarta Commons BeanUtils documentation
Summary(pl.UTF-8):	Dokumentacja do Jakarta Commons BeanUtils
Group:		Documentation
Requires:	jpackage-utils
Obsoletes:	jakarta-commons-beanutils-doc

%description javadoc
Jakarta Commons BeanUtils documentation.

%description javadoc -l pl.UTF-8
Dokumentacja do Jakarta Commons BeanUtils.

%prep
%setup -q -n commons-beanutils-%{version}-src

%build
# sources are not in ASCII
export LC_ALL=en_US
required_jars="commons-logging commons-collections"
export CLASSPATH="`/usr/bin/build-classpath $required_jars`"
%ant dist

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_javadir}

for a in dist/*.jar; do
	jar=${a##*/}
	cp -a dist/$jar $RPM_BUILD_ROOT%{_javadir}/${jar%%.jar}-%{version}.jar
	ln -s ${jar%%.jar}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/$jar
done

# javadoc
install -d $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr dist/docs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%post javadoc
rm -f %{_javadocdir}/%{name}
ln -s %{name}-%{version} %{_javadocdir}/%{name}

%postun javadoc
if [ "$1" = "0" ]; then
	rm -f %{_javadocdir}/%{name}
fi

%files
%defattr(644,root,root,755)
%doc *.txt
%{_javadir}/*.jar

%files javadoc
%defattr(644,root,root,755)
%{_javadocdir}/%{name}-%{version}
