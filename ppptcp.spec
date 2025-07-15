Summary:	IP tunnels over an arbitrary TCP connection (using pppd)
Summary(pl.UTF-8):	Tunele IP po dowolnym połączeniu TCP (przy użyciu pppd)
Name:		ppptcp
Version:	0.6
Release:	4
License:	GPL
Group:		Applications/Networking
Source0:	http://www.devolution.com/~slouken/projects/ppptcp/%{name}-%{version}.tar.gz
# Source0-md5:	d35df4ba1b9b5cdbe222eb0d6d961915
URL:		http://www.devolution.com/~slouken/projects/ppptcp/
Patch0:		%{name}-include.patch
Patch1:		%{name}-makefiles.patch
BuildRequires:	rsaref2-devel
BuildRequires:	libdes-l-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a peer-to-peer IP tunnel program that runs a PPP connection
over an arbitrary TCP port.

%description -l pl.UTF-8
To jest program do tuneli IP peer-to-peer uruchamiający połączenie PPP
po dowolnym porcie TCP.

%prep
%setup -q
%patch -P0 -p1
%patch -P1 -p1

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sbindir}

install ppptcp $RPM_BUILD_ROOT%{_sbindir}/ppptcp
install ppptcp.sh $RPM_BUILD_ROOT%{_sbindir}/ppptcp.sh
install auth.crypt/genkeys $RPM_BUILD_ROOT%{_sbindir}/ppptcp-keygen

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README CHANGES INSTALL README.keyring auth.crypt/README.crypt
%attr(755,root,root) %{_sbindir}/ppptcp
%attr(755,root,root) %{_sbindir}/ppptcp.sh
%attr(755,root,root) %{_sbindir}/ppptcp-keygen
