#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mvn-maven-invoker
Version  : 3.0.1
Release  : 2
URL      : https://repo1.maven.org/maven2/org/apache/maven/shared/maven-invoker/3.0.1/maven-invoker-3.0.1.jar
Source0  : https://repo1.maven.org/maven2/org/apache/maven/shared/maven-invoker/3.0.1/maven-invoker-3.0.1.jar
Source1  : https://repo1.maven.org/maven2/org/apache/maven/shared/maven-invoker/3.0.0/maven-invoker-3.0.0.jar
Source2  : https://repo1.maven.org/maven2/org/apache/maven/shared/maven-invoker/3.0.0/maven-invoker-3.0.0.pom
Source3  : https://repo1.maven.org/maven2/org/apache/maven/shared/maven-invoker/3.0.1/maven-invoker-3.0.1.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: mvn-maven-invoker-data = %{version}-%{release}

%description
No detailed description available

%package data
Summary: data components for the mvn-maven-invoker package.
Group: Data

%description data
data components for the mvn-maven-invoker package.


%prep

%build

%install
mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/shared/maven-invoker/3.0.1
cp %{SOURCE0} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/shared/maven-invoker/3.0.1/maven-invoker-3.0.1.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/shared/maven-invoker/3.0.0
cp %{SOURCE1} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/shared/maven-invoker/3.0.0/maven-invoker-3.0.0.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/shared/maven-invoker/3.0.0
cp %{SOURCE2} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/shared/maven-invoker/3.0.0/maven-invoker-3.0.0.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/shared/maven-invoker/3.0.1
cp %{SOURCE3} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/shared/maven-invoker/3.0.1/maven-invoker-3.0.1.pom


%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/.m2/repository/org/apache/maven/shared/maven-invoker/3.0.0/maven-invoker-3.0.0.jar
/usr/share/java/.m2/repository/org/apache/maven/shared/maven-invoker/3.0.0/maven-invoker-3.0.0.pom
/usr/share/java/.m2/repository/org/apache/maven/shared/maven-invoker/3.0.1/maven-invoker-3.0.1.jar
/usr/share/java/.m2/repository/org/apache/maven/shared/maven-invoker/3.0.1/maven-invoker-3.0.1.pom
