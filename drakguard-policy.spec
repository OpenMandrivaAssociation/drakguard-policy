%define	oldname	drakguard
Summary:	Parental control tool
Name:		drakguard-policy
Version:	0.7.7
Release:	%mkrel 11
Source0:	%{oldname}-%{version}.tar.lzma
Patch0:		drakguard_netpolice.patch
Source1:	UpdateBL
Source2:	OriginalUpdateBL
Source3:	bigblacklist.tar.gz
Source4:	badwords.zip
Source5:	new.zip
Source6:	extrem.zip
License:	GPL
Group:		System/Configuration/Other
Url:		http://www.mandriva.com/
Requires:	drakxtools >= 10.22
Requires:	drakx-net >= 0.41
BuildRequires:	perl-MDK-Common-devel gettext
Requires:	dansguardian
Obsoletes:	drakguard
BuildRoot:	%_tmppath/%name-%version-buildroot
BuildArch:	noarch

%description
This tool allows to configure parental control. It can block access to
web sites and restrict connection during a specified timeframe.

%description -l ru
Этот инструмент позволяет настраивать родительский контролью Он может блокировать
доступ к веб сайтам (используя также DNS NetPolice) и ограничивать соединение в
заданное время, а также запуск программ. 

Чтобы убрать фильтры NetPolice удалите из файла /etc/squid/squid.conf строку dns_nameservers 81.176.72.82 81.176.72.83

%prep
tar -xf %{SOURCE0}
cd %{oldname}-%{version}
%patch0 -p0

%build
cd %{oldname}-%{version}
%make

%install
rm -rf %{buildroot}
cd %{oldname}-%{version}
%makeinstall_std 
%find_lang %{oldname}

%clean
rm -rf %{buildroot}

%files -f %oldname-%version/%{oldname}.lang
%defattr(-,root,root)
%doc %{oldname}-%{version}/NEWS
%{_sbindir}/%{oldname}
%{_sbindir}/*
/usr/lib/libDrakX/icons/*
