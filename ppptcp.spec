Summary:	IP tunnels over an arbitrary TCP connection [using pppd]
Name:		ppptcp
Version:	0.6
Release:	1
License:	GPL
Group:		Applications/Networking
Group(de):	Applikationen/Netzwerkwesen
Group(pl):	Aplikacje/Sieciowe
URL:		http://www.devolution.com/~slouken/projects/ppptcp/
Source0:	http://www.devolution.com/~slouken/projects/ppptcp/%{name}-%{version}.tar.gz
Patch0:		%{name}-include.patch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a peer-to-peer IP tunnel program that runs a PPP connection
over an arbitrary TCP port.

%prep
%setup -q -n %{name}-%{version}
%patch -p1

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
install ppptcp $RPM_BUILD_ROOT/%{_bindir}/ppptcp
gzip -9nf README CHANGES COPYING INSTALL README.keyring

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.gz CHANGES.gz COPYING.gz INSTALL.gz README.keyring.gz

%attr(755,root,root) %{_bindir}/ppptcp
