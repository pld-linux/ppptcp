Summary:	IP tunnels over an arbitrary TCP connection [using pppd]
Name:		ppptcp
Version:	0.6
Release:	2
License:	distributable
Group:		Applications/Networking
Group(de):	Applikationen/Netzwerkwesen
Group(pl):	Aplikacje/Sieciowe
URL:		http://www.devolution.com/~slouken/projects/ppptcp/
Source0:	http://www.devolution.com/~slouken/projects/ppptcp/%{name}-%{version}.tar.gz
Source1:	rsaref2.tar.gz
Source2:	libdes-l-4.04b.tar.gz
Patch0:		%{name}-include.patch
Patch1:		%{name}-makefiles.patch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a peer-to-peer IP tunnel program that runs a PPP connection
over an arbitrary TCP port.

%prep
%setup -q -n %{name}-%{version} 
%setup -q -a1 -a2
%patch0 -p1
%patch1 -p1 

%build
%{__make} -C des
%{__make} -C rsaref2/install/unix
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sbindir}
install ppptcp $RPM_BUILD_ROOT/%{_sbindir}/ppptcp
install ppptcp.sh $RPM_BUILD_ROOT/%{_sbindir}/ppptcp.sh
install auth.crypt/genkeys $RPM_BUILD_ROOT/%{_sbindir}/ppptcp-keygen

gzip -9nf README CHANGES COPYING INSTALL README.keyring auth.crypt/README.crypt

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.gz CHANGES.gz COPYING.gz INSTALL.gz README.keyring.gz  auth.crypt/README.crypt.gz
%attr(755,root,root) %{_sbindir}/ppptcp
%attr(755,root,root) %{_sbindir}/ppptcp.sh
%attr(755,root,root) %{_sbindir}/ppptcp-keygen
