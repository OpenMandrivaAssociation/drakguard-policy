Summary:	Parental control tool
Name:		drakguard-policy
Version:	0.7.7
Release:	%mkrel 11
#Source0:  %name-%version.tar.lzma

Source0:	drakguard_netpolice.patch
Source1:	UpdateBL
Source2:	OriginalUpdateBL
Source3:	bigblacklist.tar.gz
Source4:	badwords.zip
Source5:	new.zip
Source6:	extrem.zip

License:	GPL
Group:		System/Configuration/Other
Url:		http://www.mandriva.com/
BuildRequires:	drakguard, dansguardian
Requires:	drakxtools >= 10.22
Requires:	drakx-net >= 0.41
Requires:	drakguard, dansguardian
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

#%setup -q
#%patch0 -p0

%build
#%make

%install
#rm -rf %{buildroot}
#%makeinstall_std
#%find_lang %name

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
#%doc NEWS
#%{_sbindir}/%{name}
#%{_sbindir}/*
#/usr/lib/libDrakX/icons/*


