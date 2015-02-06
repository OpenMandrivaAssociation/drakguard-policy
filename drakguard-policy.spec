Summary:	Parental control tool with NetPolice DNS enable
Name:		drakguard-policy
Version:	0.7.7
Release:	10
License:	GPLv2+
Group:		System/Configuration/Other
Url:		http://www.rosalab.ru/
Requires(post,postun):	squid
Requires:	drakguard
BuildArch:	noarch

%description
This tool allows to configure parental control. It can block access to
web sites and restrict connection during a specified timeframe. This version
consist DNS-protect from russian company Yandex.

To disable NetPolice filters remove this line from /etc/squid/squid.conf:
dns_nameservers 77.88.8.3 77.88.8.7

%files

%post
echo "dns_nameservers 77.88.8.3 77.88.8.7" >> /etc/squid/squid.conf

%postun
sed -i 's/dns_nameservers\ 77.88.8.3\ 77.88.8.7//' /etc/squid/squid.conf

#----------------------------------------------------------------------------

%prep
# Nothing

%build
# Nothing

%install
# Nothing

