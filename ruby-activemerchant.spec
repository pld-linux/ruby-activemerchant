Summary:	Ruby library for dealing with Creditcards, Payments  and shipping
Summary(pl.UTF-8)	Biblioteka języka Ruby do obsługi kart kredytowych, płatności i wysyłek
Name:		ruby-ActiveMerchant
%define tarname activemerchant
Version:	1.0.3
Release:	1
License:	Ruby-alike
Group:		Development/Languages
Source0:	http://rubyforge.org/frs/download.php/17865/%{tarname}-%{version}.tgz
# Source0-md5:	fa6ae6d8f551974eb4676d346dfe13a1
URL:		http://www.activemerchant.org/
BuildRequires:	rpmbuild(macros) >= 1.277
BuildRequires:	ruby-modules
%{?ruby_mod_ver_requires_eq}
#BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Active Merchant is an extraction from the e-commerce system Shopify.
Shopify's requirements for a simple and unified API to access dozens
of different payment gateways with very different internal APIs was
the chief principle in designing the library.

%description -l pl.UTF-8
Active Merchant pochodzi z systemu e-commerce o nazwie Shopify.
Zaspokojenie potrzeb Shopify na zunifikowane API dostępu do dziesiątek
różnych bramek płatności z różnymi natywnymi interfejsami było główną
zasadą, jaką kierowali się projektanci tej biblioteki.

%prep
%setup -q -n %{tarname}-%{version}

%build
#rdoc --ri --op ri lib
rdoc --op rdoc lib

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_rubylibdir},%{ruby_ridir}}
cp -a lib/* $RPM_BUILD_ROOT%{ruby_rubylibdir}
#cp -a ri/* $RPM_BUILD_ROOT%{ruby_ridir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG rdoc
%{ruby_rubylibdir}/*
#%{ruby_ridir}/ActiveSupport
