Summary:	MDcrack - bruteforce MD4/MD5/NTLM1 hashes
Summary(pl):	MDcrack - brualne ³amanie skrótów MD4/MD5/NTLM1
Name:		mdcrack
Version:	1.2
Release:	1
License:	?
Group:		Applications
Source0:	http://membres.lycos.fr/mdcrack/download/%{name}-%{version}.tar.gz
# Source0-md5:	53d23b73bb48a3e106b8ce748d6b2bb8
URL:		http://mdcrack.multimania.com/
BuildRequires:	ncurses-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
MDcrack - bruteforce MD4/MD5/NTLM1 hashes.

%description -l pl
MDcrack - brutalne ³amanie skrótów MD4/MD5/NTLM1.

%prep
%setup -q

%build
%{__make} \
	CC=%{__cc} CFLAGS="%{rpmcflags} %{!?debug:-fomit-frame-pointer} -ffast-math -I/usr/include/ncurses" \
%ifarch %{ix86} alpha
	little
%else
	big
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install bin/mdcrack $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc BENCHMARKS CREDITS FAQ README TODO VERSIONS WWW
%attr(755,root,root) %{_bindir}/*
