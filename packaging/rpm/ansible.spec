%define name ansible

%if 0%{?rhel} == 5
%define __python /usr/bin/python26
%endif

Name:      %{name}
Version:   1.5
Release:   1%{?dist}
Url:       http://www.ansible.com
Summary:   SSH-based application deployment, configuration management, and IT orchestration platform
License:   GPLv3
Group:     Development/Libraries
Source:    http://releases.ansible.com/ansible/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}

BuildArch: noarch

# RHEL <=5
%if 0%{?rhel} && 0%{?rhel} <= 5
BuildRequires: python26-devel
Requires: python26-PyYAML
Requires: python26-paramiko
Requires: python26-jinja2
Requires: python26-keyczar
Requires: python26-httplib2
%endif

# RHEL > 5
%if 0%{?rhel} && 0%{?rhel} > 5
BuildRequires: python2-devel
Requires: PyYAML
Requires: python-paramiko
Requires: python-jinja2
Requires: python-keyczar
Requires: python-httplib2
%endif

# FEDORA > 17
%if 0%{?fedora} >= 18
BuildRequires: python-devel
Requires: PyYAML
Requires: python-paramiko
Requires: python-jinja2
Requires: python-keyczar
Requires: python-httplib2
%endif

# SuSE/openSuSE
%if 0%{?suse_version} 
BuildRequires: python-devel
BuildRequires: python-setuptools
Requires: python-paramiko
Requires: python-jinja2
Requires: python-keyczar
Requires: python-yaml
Requires: python-httplib2
%endif

Requires: sshpass

%description

Ansible is a radically simple model-driven configuration management,
multi-node deployment, and orchestration engine. Ansible works
over SSH and does not require any software or daemons to be installed
on remote nodes. Extension modules can be written in any language and
are transferred to managed machines automatically.

%prep
%setup -q

%build
%{__python} setup.py build

%install
%{__python} setup.py install -O1 --prefix=%{_prefix} --root=%{buildroot}
mkdir -p %{buildroot}/etc/ansible/
cp examples/hosts %{buildroot}/etc/ansible/
cp examples/ansible.cfg %{buildroot}/etc/ansible/
mkdir -p %{buildroot}/%{_mandir}/man1/
cp -v docs/man/man1/*.1 %{buildroot}/%{_mandir}/man1/
mkdir -p %{buildroot}/%{_datadir}/ansible
cp -rv library/* %{buildroot}/%{_datadir}/ansible/

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{python_sitelib}/ansible*
%{_bindir}/ansible*
%dir %{_datadir}/ansible
%dir %{_datadir}/ansible/*
%{_datadir}/ansible/*/*
%config(noreplace) %{_sysconfdir}/ansible
%doc README.md PKG-INFO COPYING
%doc %{_mandir}/man1/ansible*
%doc examples/playbooks


%changelog

* Fri Feb 28 2014 Michael DeHaan <michael@ansible.com> - 1.5-0
- Release 1.5.0

* Wed Feb 12 2014 Michael DeHaan <michael.dehaan@gmail.com> - 1.4.5
* Release 1.4.5

* Mon Jan 06 2014 Michael DeHaan <michael.dehaan@gmail.com> - 1.4.4
* Release 1.4.4

* Fri Dec 20 2013 Michael DeHaan <michael.dehaan@gmail.com> - 1.4.3
* Release 1.4.3

* Wed Dec 18 2013 Michael DeHaan <michael.dehaan@gmail.com> - 1.4.2
* Release 1.4.2

* Wed Nov 27 2013 Michael DeHaan <michael.dehaan@gmail.com> - 1.4-1
* Release 1.4.1

* Thu Nov 21 2013 Michael DeHaan <michael.dehaan@gmail.com> - 1.4-0
* Release 1.4.0

* Fri Sep 13 2013 Michael DeHaan <michael.dehaan@gmail.com> - 1.3-0
* Release 1.3.0

* Thu Jul 05 2013 Michael DeHaan <michael.dehaan@gmail.com> - 1.2-2
* Release 1.2.2

* Thu Jul 04 2013 Michael DeHaan <michael.dehaan@gmail.com> - 1.2-1
* Release 1.2.1

* Mon Jun 10 2013 Michael DeHaan <michael.dehaan@gmail.com> - 1.2-0
* Release 1.2

* Tue Apr 2 2013 Michael DeHaan <michael.dehaan@gmail.com> - 1.1-0
* Release 1.1

* Fri Feb 1 2013 Michael DeHaan <michael.dehaan@gmail.com> - 1.0-0
- Release 1.0

* Fri Nov 30 2012 Michael DeHaan <michael.dehaan@gmail.com> - 0.9-0
- Release 0.9

* Fri Oct 19 2012 Michael DeHaan <michael.dehaan@gmail.com> - 0.8-0
- Release of 0.8

* Thu Aug 6 2012 Michael DeHaan <michael.dehaan@gmail.com> - 0.7-0
- Release of 0.7

* Mon Aug 6 2012 Michael DeHaan <michael.dehaan@gmail.com> - 0.6-0
- Release of 0.6

* Wed Jul 4 2012 Michael DeHaan <michael.dehaan@gmail.com> - 0.5-0
- Release of 0.5

* Wed May 23 2012 Michael DeHaan <michael.dehaan@gmail.com> - 0.4-0
- Release of 0.4

* Mon Apr 23 2012 Michael DeHaan <michael.dehaan@gmail.com> - 0.3-1
- Release of 0.3

* Tue Apr  3 2012 John Eckersberg <jeckersb@redhat.com> - 0.0.2-1
- Release of 0.0.2

* Sat Mar 10 2012  <tbielawa@redhat.com> - 0.0.1-1
- Release of 0.0.1
