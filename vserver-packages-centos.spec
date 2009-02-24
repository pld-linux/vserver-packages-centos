
%define _source_payload	w4.gzdio
%define _binary_payload	w9.gzdio

Summary:	A package providing fake packages for VServer Centos guest system
Summary(pl.UTF-8):	Pakiet udostępniający fałszywe pakiety dla systemu gościnnego VServera
Name:		vserver-packages-centos
Version:	1.0
Release:	1
License:	GPL
Group:		Base
BuildArch:	noarch
Provides:	/sbin/nash
Provides:	dev = 3.3-3
Provides:	kernel = 2.6.9-78.EL
Provides:	kudzu = 1.1.95.23
Provides:	lvm2 = 2.02.37
Provides:	mingetty = 1.07
Provides:	mkinitrd = 4.2.1.13
Provides:	module-init-tools = 3.1
Provides:	udev = 034-2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A package providing a fake packages to allow removal of useless
packages inside VPS. Dedicated for CentosOS.

%description -l pl.UTF-8
Pakiet dostarczający fałszywe pakiety CentoOS, aby umożliwić usunięcie
bezużytecznych pakietów z VPS-a. 

%prep

%install
rm -rf $RPM_BUILD_ROOT

%post
echo 'Now you can:'
echo 'rpm -e dbus dbus-glib device-mapper hal hotplug hwdata kernel kudzu lvm2 MAKEDEV mingetty mkinitrd udev usbutils'

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
