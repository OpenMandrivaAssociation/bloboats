%define name	bloboats
%define version 1.0.1
%define rel	1
%define release	%mkrel %rel
%define Summary Boat racing game

Name:		%{name}
Version:	%{version}
Release:	%{release}
Source:		bloboats-1.0.1.tar.bz2
Patch0:         bloboats-1.0.1-fix-install.patch
License:	GPL
Group:		Games/Arcade
URL:		http://bloboats.dy.fi/
Summary:	%{Summary}
BuildRequires:	SDL_mixer-devel SDL_image-devel SDL_net-devel
BuildRequires:	libvorbis-devel
BuildRequires:	mesaglu-devel
BuildRequires:	ImageMagick
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Bloboats is a boat racing game in which the objective is to reach the
goal as fast as possible, at least faster than your friend does.

%prep
%setup -q
%patch0 -p1 

%build

%make

%install
rm -rf $RPM_BUILD_ROOT
%{makeinstall_std} PREFIX=$RPM_BUILD_ROOT BINARYDIR=$RPM_BUILD_ROOT%{_gamesbindir}

mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=%{name}
Comment=%{Summary}
Exec=%{name} 
Icon=%{name}
Terminal=false
StartupNotify=false
Type=Application
Categories=X-MandrivaLinux-MoreApplications-Games-Arcade;Game;ArcadeGame;
EOF

# install icons
mkdir -p $RPM_BUILD_ROOT{%{_liconsdir},%{_miconsdir},%{_iconsdir}}
cp data/images/icon.png $RPM_BUILD_ROOT%{_iconsdir}/%{name}.png
convert -scale 48x48 data/images/icon.png $RPM_BUILD_ROOT%{_liconsdir}/%{name}.png
convert -scale 16x16 data/images/icon.png $RPM_BUILD_ROOT%{_miconsdir}/%{name}.png

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc copying.txt readme.txt
%{_gamesbindir}/%{name}
%{_sysconfdir}/bloboats.dirs
%{_gamesdatadir}/%{name}/data/*
# Why does this files get 755 perms?
%attr(0644,root,root) %{_gamesdatadir}/%{name}/data/*/*.*
%attr(0644,root,root) %{_gamesdatadir}/%{name}/data/defaults/*/*.*
%attr(0644,root,root) %{_gamesdatadir}/%{name}/data/defaults/private/*/*.*

%_datadir/applications/*
%{_liconsdir}/%{name}.png
%{_miconsdir}/%{name}.png
%{_iconsdir}/%{name}.png


