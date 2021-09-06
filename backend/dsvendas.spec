Name:           dsvendas
Version:        0.0.1-SNAPSHOT
Release:        1%{?dist}
Summary:        dsvendas

Group:          Development/Libraries
License:        
URL:            
Source0:        #FIXME
BuildArch: noarch

BuildRequires: mvn(org.springframework.boot:spring-boot-starter-test)
BuildRequires: mvn(org.springframework.security:spring-security-test)
BuildRequires: mvn(org.postgresql:postgresql)
BuildRequires: mvn(com.h2database:h2)
BuildRequires: maven-local

%description
projeto desenvolvido na semana spring react 

%package javadoc
Group:          Documentation
Summary:        Javadoc for %{name}

%description javadoc
API documentation for %{name}.


%prep
%setup -q #You may need to update this according to your Source0

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%dir %{_javadir}/%{name}

%files javadoc -f .mfiles-javadoc

%changelog
#FIXME
