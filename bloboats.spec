Name:		bloboats
Summary:	Boat racing game
Version:	1.0.2
Release:	%mkrel 1
Source:		http://mirror.kapsi.fi/bloboats.dy.fi/%{name}-%{version}.tar.gz
License:	GPL
Group:		Games/Arcade
URL:		http://bloboats.dy.fi/
BuildRequires:	SDL_mixer-devel SDL_image-devel SDL_net-devel
BuildRequires:	libvorbis-devel
BuildRequires:	mesaglu-devel
BuildRequires:	imagemagick
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Bloboats is a boat racing game in which the objective is to reach the
goal as fast as possible, at least faster than your friend does.

%prep
%setup -q

%build
%make DATADIR=%{_gamesdatadir}/%{name}/data

%install
rm -rf %{buildroot}
%makeinstall_std PREFIX=%{buildroot} \
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

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
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



%changelog
* Mon Nov 28 2011 Andrey Bondrov <abondrov@mandriva.org> 1.0.2-1
+ Revision: 734894
- New version 1.0.2

* Thu Dec 09 2010 Oden Eriksson <oeriksson@mandriva.com> 1.0.1-3mdv2011.0
+ Revision: 616778
- the mass rebuild of 2010.0 packages

* Wed Sep 02 2009 Thierry Vignaud <tv@mandriva.org> 1.0.1-2mdv2010.0
+ Revision: 424661
- rebuild

  + Oden Eriksson <oeriksson@mandriva.com>
    - lowercase ImageMagick

* Thu Dec 20 2007 Olivier Blin <blino@mandriva.org> 1.0.1-1mdv2008.1
+ Revision: 135856
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Thu Mar 08 2007 Olivier Blin <oblin@mandriva.com> 1.0.1-1mdv2007.1
+ Revision: 138396
- buildrequires mesaglu-devel
- install in games bindir
- wrap description
- initial bloboats package from Jose Jorge
- Create bloboats

