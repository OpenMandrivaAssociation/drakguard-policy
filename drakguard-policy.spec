%define		original_name	drakguard
Summary:	Parental control tool with NetPolice DNS enable
Name:		drakguard-policy
Version:	0.7.7
Release:	%mkrel 6
License:	GPL
Group:		System/Configuration/Other
Url:		http://www.mandriva.com/
Requires:	drakguard
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot
BuildArch:	noarch

%description
This tool allows to configure parental control. It can block access to
web sites and restrict connection during a specified timeframe. This version
consist DNS-protect from russian company NetPolice.

%description -l ru
Этот инструмент позволяет настраивать родительский контролью Он может блокировать
доступ к веб сайтам (используя также DNS NetPolice) и ограничивать соединение в
заданное время, а также запуск программ. 

Чтобы убрать фильтры NetPolice удалите из файла /etc/squid/squid.conf строку dns_nameservers 81.176.72.82 81.176.72.83

%prep

%post

echo "dns_nameservers 81.176.72.82 81.176.72.83" >> /etc/squid/squid.conf

%postun

sed -i 's/dns_nameservers\ 81.176.72.82\ 81.176.72.83//' /etc/squid/squid.conf

%files


%changelog
* Sun Aug 21 2011 Александр Казанцев <kazancas@mandriva.org> 0.7.7-6mdv2012.0
+ Revision: 696051
- delete fork drakguard and use only adding netpolice DNS in squid.conf

* Sun Aug 21 2011 Александр Казанцев <kazancas@mandriva.org> 0.7.7-5
+ Revision: 696047
- add drakguard to Conficts section due lopp upgrade error

* Sat Aug 20 2011 Александр Казанцев <kazancas@mandriva.org> 0.7.7-2
+ Revision: 695844
- fix description for proper select

* Sun Aug 14 2011 Sergey Zhemoitel <serg@mandriva.org> 0.7.7-1
+ Revision: 694534
- fis spec
- few modify spec
- imported package drakguard-policy

