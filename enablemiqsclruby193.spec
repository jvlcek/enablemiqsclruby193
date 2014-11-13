Name:		enablemiqsclruby193
Version:	0.1
Release:	1%{?dist}
Summary:	Enable Ruby193 for the MiQSCL

Group:		System Environment/Daemons
License:	Unknown
URL:		https://github.com/jvlcek/enablemiqsclruby193.git
Source0:	%{name}-%{version}.tar.gz
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildArch:	noarch
# TODO: requires ruby or scl ruby
# Requires: ruby OR scl

%define staging %{_localstatedir}/lib/enablemiqsclruby193

%description
enablemiqsclruby193 will be used to set the ruby version to 193 for the miqscl RPMs

%build

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{staging}
install -m644 README.md $RPM_BUILD_ROOT%{staging}
install -m755 enablemiqsclruby193 $RPM_BUILD_ROOT%{staging}
install -m755 enablemiqsclruby193.rb $RPM_BUILD_ROOT%{staging}

%clean
rm -rf $RPM_BUILD_ROOT

%post
# TODO: Run this script on installation

%preun
# TODO: Run this script on installation

%files
%defattr(-,root,root,-)
%{staging}/README.md
%{staging}/enablemiqsclruby193
%{staging}/enablemiqsclruby193.rb

%changelog
* Thu Nov 13 2014 Joe VLcek 0.1-1
- Initial release.
