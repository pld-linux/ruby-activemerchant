%define pkgname activemerchant
Summary:	Ruby library for dealing with Creditcards, Payments  and shipping
Summary(pl.UTF-8):	Biblioteka języka Ruby do obsługi kart kredytowych, płatności i wysyłek
Name:		ruby-activemerchant
Version:	1.9.3
Release:	1
License:	Ruby-alike
Group:		Development/Languages
Source0:	http://rubygems.org/downloads/activemerchant-%{version}.gem
# Source0-md5:	06ecf8121ec0b48f9259878917582db1
Patch0:		%{name}-paths.patch
URL:		http://www.activemerchant.org/
BuildRequires:	rpmbuild(macros) >= 1.277
BuildRequires:	ruby-modules
%{?ruby_mod_ver_requires_eq}
Provides:	ruby-ActiveMerchant
Obsoletes:	ruby-ActiveMerchant
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
%setup -q -c
%{__tar} xf %{SOURCE0} -O data.tar.gz | %{__tar} xz
find -newer README.rdoc -o -print | xargs touch --reference %{SOURCE0}
#%patch0 -p1

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
