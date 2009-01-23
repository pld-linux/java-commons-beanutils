#
# Conditional build:
%bcond_without	javadoc		# don't build javadoc
#
%include	/usr/lib/rpm/macros.java
Summary:	Jakarta Commons BeanUtils - Bean Introspection Utilities
Summary(pl.UTF-8):	Jakarta Commons BeanUtils - narzędzia do badania JavaBeans
Name:		java-commons-beanutils
Version:	1.7.0
Release:	3
License:	Apache
Group:		Libraries/Java
Source0:	http://www.apache.org/dist/commons/beanutils/source/commons-beanutils-%{version}-src.tar.gz
# Source0-md5:	3fd5cbdf70363b151de5cd538f726e67
Patch0:		jakarta-commons-beanutils-target.patch
URL:		http://commons.apache.org/beanutils/
BuildRequires:	java-commons-collections
BuildRequires:	java-commons-logging
BuildRequires:	jpackage-utils
BuildRequires:	junit
BuildRequires:	rpm-javaprov
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	jre
Suggests:	java-commons-collections
Provides:	jakarta-commons-beanutils
Obsoletes:	jakarta-commons-beanutils
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
%patch0 -p1

%build
required_jars="commons-logging commons-collections"
export CLASSPATH=$(build-classpath $required_jars)
export LC_ALL=en_US # sources are not in ASCII
%ant dist

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_javadir}

# jars
cp -a dist/commons-beanutils-core.jar $RPM_BUILD_ROOT%{_javadir}/commons-beanutils-core-%{version}.jar
ln -s commons-beanutils-core-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/commons-beanutils-core.jar

cp -a dist/commons-beanutils-bean-collections.jar $RPM_BUILD_ROOT%{_javadir}/commons-beanutils-bean-collections-%{version}.jar
ln -s commons-beanutils-bean-collections-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/commons-beanutils-bean-collections.jar

# javadoc
%if %{with javadoc}
install -d $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -a dist/docs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name} # ghost symlink
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%post javadoc
ln -nfs %{name}-%{version} %{_javadocdir}/%{name}

%files
%defattr(644,root,root,755)
%doc *.txt
%{_javadir}/*.jar

%if %{with javadoc}
%files javadoc
%defattr(644,root,root,755)
%{_javadocdir}/%{name}-%{version}
%ghost %{_javadocdir}/%{name}
%endif
