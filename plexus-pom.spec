%{?scl:%scl_package plexus-pom}
%{!?scl:%global pkg_name %{name}}

Name:          %{?scl_prefix}plexus-pom
Version:       3.3.3
Release:       4.1%{?dist}
Summary:       Root Plexus Projects POM
Group:         Development/Libraries
License:       ASL 2.0
URL:           https://github.com/codehaus-plexus/plexus-pom
Source0:       https://github.com/codehaus-plexus/plexus-pom/archive/plexus-%{version}.tar.gz
Source1:       http://www.apache.org/licenses/LICENSE-2.0.txt
BuildArch:     noarch

BuildRequires: %{?scl_prefix}maven-local
BuildRequires: %{?scl_prefix}forge-parent

%description
The Plexus project provides a full software stack for creating and
executing software projects.  This package provides parent POM for
Plexus packages.

%prep
%setup -q -n plexus-pom-plexus-%{version}
# require: maven-site-plugin *
%pom_xpath_remove "pom:profile[pom:id='maven-3']"
# * require: org.codehaus.plexus plexus-stylus-skin 1.0
# org.apache.maven.wagon wagon-webdav-jackrabbit 1.0
%pom_remove_plugin org.apache.maven.plugins:maven-site-plugin

%pom_remove_plugin org.codehaus.mojo:findbugs-maven-plugin
%pom_remove_plugin org.codehaus.mojo:taglist-maven-plugin
cp -p %{SOURCE1} LICENSE

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%license LICENSE

%changelog
* Wed Jun 21 2017 Java Maintainers <java-maint@redhat.com> - 3.3.3-4.1
- Automated package import and SCL-ization

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Apr 14 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.3.3-1
- Update to upstream version 3.3.3

* Wed Apr  1 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.3.1-10
- Update upstream URL

* Wed Feb 11 2015 gil cattaneo <puntogil@libero.it> 3.3.1-9
- introduce license macro

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.3.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 28 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.3.1-7
- Rebuild to regenerate Maven auto-requires

* Wed May 28 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.3.1-6
- Rebuild to regenerate provides

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.3.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Apr 12 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.3.1-4
- Build with xmvn

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 3.3.1-2
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Sat Dec 08 2012 gil cattaneo <puntogil@libero.it> 3.3.1-1
- Update to 3.3.1

* Wed Nov 21 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.0.1-3
- Install LICENSE file
- Resolves: rhbz#878825

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Feb 08 2012 gil cattaneo <puntogil@libero.it> 3.0.1-1
- initial rpm
