Summary:	A utility for displaying and/or setting hard disk parameters
Name:		hdparm
Version:	8.5
Release:	%mkrel 2
License:	BSD
Group:		System/Kernel and hardware
URL:		http://sourceforge.net/projects/hdparm/
Source0:	http://nchc.dl.sourceforge.net/sourceforge/hdparm/%name-%version.tar.gz
Source1:	hdparm-sysconfig
Patch0:		hdparm-no_strip.diff
Buildroot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Hdparm is a useful system utility for setting (E)IDE hard drive parameters. For
example, hdparm can be used to tweak hard drive performance and to spin down
hard drives for power conservation.

%prep

%setup -q
%patch0 -p0

%build
%serverbuild
perl -pi -e "s/-O2/$CFLAGS/" Makefile
make clean
%make

%install
rm -fr %{buildroot}

install -m0755 hdparm -D %{buildroot}/sbin/hdparm
install -m0644 hdparm.8 -D %{buildroot}%{_mandir}/man8/hdparm.8
install -m0644 %{SOURCE1} -D %{buildroot}%{_sysconfdir}/sysconfig/harddisks

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc hdparm.lsm Changelog README.acoustic
%config(noreplace) %{_sysconfdir}/sysconfig/harddisks
/sbin/hdparm
%{_mandir}/man8/hdparm.8*
