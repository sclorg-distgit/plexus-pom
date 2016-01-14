%global pkg_name plexus-pom
%{?scl:%scl_package %{pkg_name}}
%{?maven_find_provides_and_requires}

Name:          %{?scl_prefix}%{pkg_name}
Version:       3.3.1
Release:       5.11%{?dist}
Summary:       Root Plexus Projects POM
License:       ASL 2.0
URL:           https://github.com/sonatype/%{pkg_name}/
Source0:       https://github.com/sonatype/plexus-pom/archive/plexus-%{version}.tar.gz
Source1:       http://www.apache.org/licenses/LICENSE-2.0.txt
BuildArch:     noarch

BuildRequires: %{?scl_prefix_java_common}maven-local
BuildRequires: %{?scl_prefix}spice-parent

%description
The Plexus project provides a full software stack for creating and
executing software projects.  This package provides parent POM for
Plexus packages.

%prep
%setup -q -n plexus-pom-plexus-%{version}
%{?scl:scl enable %{scl} - <<"EOF"}
set -e -x
# require: maven-site-plugin *
%pom_xpath_remove "pom:profile[pom:id='maven-3']"
# * require: org.codehaus.plexus plexus-stylus-skin 1.0
# org.apache.maven.wagon wagon-webdav-jackrabbit 1.0
%pom_remove_plugin org.apache.maven.plugins:maven-site-plugin

%pom_remove_plugin org.codehaus.mojo:findbugs-maven-plugin
%pom_remove_plugin org.codehaus.mojo:taglist-maven-plugin
cp -p %{SOURCE1} LICENSE
%{?scl:EOF}

%build
%{?scl:scl enable %{scl} - <<"EOF"}
set -e -x
%mvn_build
%{?scl:EOF}

%install
%{?scl:scl enable %{scl} - <<"EOF"}
set -e -x
%mvn_install
%{?scl:EOF}

%files -f .mfiles
%dir %{_mavenpomdir}/%{pkg_name}
%doc LICENSE

%changelog
* Thu Jan 15 2015 Michal Srb <msrb@redhat.com> - 3.3.1-5.11
- Fix directory ownership

* Tue Jan 13 2015 Michael Simacek <msimacek@redhat.com> - 3.3.1-5.10
- Mass rebuild 2015-01-13

* Tue Jan 06 2015 Michael Simacek <msimacek@redhat.com> - 3.3.1-5.9
- Mass rebuild 2015-01-06

* Mon May 26 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.3.1-5.8
- Mass rebuild 2014-05-26

* Wed Feb 19 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.3.1-5.7
- Mass rebuild 2014-02-19

* Wed Feb 19 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.3.1-5.6
- Rebuild to get rid of auto-requires on java-devel

* Tue Feb 18 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.3.1-5.5
- Mass rebuild 2014-02-18

* Mon Feb 17 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.3.1-5.4
- Rebuild to fix incorrect auto-requires

* Fri Feb 14 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.3.1-5.3
- SCL-ize requires and build-requires

* Thu Feb 13 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.3.1-5.2
- Rebuild to regenerate auto-requires

* Tue Feb 11 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.3.1-5.1
- First maven30 software collection build

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 3.3.1-5
- Mass rebuild 2013-12-27

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
