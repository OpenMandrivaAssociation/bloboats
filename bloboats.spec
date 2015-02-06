Summary:	Boat racing game
Name:		bloboats
Version:	1.0.2
Release:	3
License:	GPL
Group:		Games/Arcade
Url:		http://bloboats.dy.fi/
Source0:	http://mirror.kapsi.fi/bloboats.dy.fi/%{name}-%{version}.tar.gz
Patch0:		bloboats-1.0.2-cflags.patch
BuildRequires:	imagemagick
BuildRequires:	pkgconfig(gl)
BuildRequires:	pkgconfig(glu)
BuildRequires:	pkgconfig(SDL_image)
BuildRequires:	pkgconfig(SDL_mixer)
BuildRequires:	pkgconfig(SDL_net)
BuildRequires:	pkgconfig(vorbis)

%description
Bloboats is a boat racing game in which the objective is to reach the
goal as fast as possible, at least faster than your friend does.

%files
%doc copying.txt readme.txt
%{_gamesbindir}/%{name}
%{_sysconfdir}/bloboats.dirs
# Why does this files get 755 perms?
%attr(0644,root,root) %{_gamesdatadir}/%{name}/data/*/*.*
%attr(0644,root,root) %{_gamesdatadir}/%{name}/data/defaults/*/*.*
%attr(0644,root,root) %{_gamesdatadir}/%{name}/data/defaults/private/*/*.*
%{_datadir}/applications/*.desktop
%{_liconsdir}/%{name}.png
%{_miconsdir}/%{name}.png
%{_iconsdir}/%{name}.png

#----------------------------------------------------------------------------

%prep
%setup -q
%patch0 -p1

%build
%make \
	STRIP=true \
	CFLAGS="%{optflags}" \
	DATADIR=%{_gamesdatadir}/%{name}/data

%install
%makeinstall_std \
	PREFIX=%{buildroot} \
	BINARYDIR=%{buildroot}%{_gamesbindir} \
	DATADIR=%{buildroot}%{_gamesdatadir}/%{name}/data

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
Categories=Game;ArcadeGame;
EOF

# install icons
mkdir -p %{buildroot}{%{_liconsdir},%{_miconsdir},%{_iconsdir}}
cp data/images/icon.png %{buildroot}%{_iconsdir}/%{name}.png
convert -scale 48x48 data/images/icon.png %{buildroot}%{_liconsdir}/%{name}.png
convert -scale 16x16 data/images/icon.png %{buildroot}%{_miconsdir}/%{name}.png


